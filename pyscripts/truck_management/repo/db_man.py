#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import pymssql
import UserDb
from datetime import datetime
from ftplib import FTP

"""
    odbc db manipulation
"""

host = None
inst = None
user = None
pswd = None
dbnm = None
ftpp = None

tabname2sqlcmd = {
    'LimitW': 0,
    'smArea': 1,
    'smHighWayDate': 2,
    'smSites': 3,
    'blacklist': 4
}

status = {
    None: '未处理',
    1: '已申请处理',
    2: '处理申请已审核',
    3: '处理已登记',
    4: '处理登记已审核'
}

init_db_cmds = [
    """ if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[LimitW]') and 
        OBJECTPROPERTY(id, N'IsUserTable') = 1)
        drop table [dbo].[LimitW]""",
    """ if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[smArea]') and 
        OBJECTPROPERTY(id, N'IsUserTable') = 1)
        drop table [dbo].[smArea]""",
    """ if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[smHighWayDate]') and 
        OBJECTPROPERTY(id, N'IsUserTable') = 1)
        drop table [dbo].[smHighWayDate]
    """,
    """ if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[smSites]') and 
        OBJECTPROPERTY(id, N'IsUserTable') = 1)
        drop table [dbo].[smSites]
    """,
    """ if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[blacklist]') and 
        OBJECTPROPERTY(id, N'IsUserTable') = 1)
        drop table [dbo].[blacklist]
    """
]

setup_db_cmds = [
    """ if not exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[LimitW]'))
        CREATE TABLE [dbo].[LimitW] (
        [VehicheType] [int] NOT NULL ,
        [LimitWeight] [int] NOT NULL
        ) ON [PRIMARY]
    """,
    """ if not exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[smArea]'))
        CREATE TABLE [dbo].[smArea] (
        [ID] [int] IDENTITY (1, 1) NOT NULL ,
        [AreaID] [int] NULL ,
        [AreaName] [nvarchar] (50) COLLATE Chinese_PRC_CI_AS NULL ,
        [AreaInfo] [nvarchar] (50) COLLATE Chinese_PRC_CI_AS NULL ,
        [SiteID] [int] NULL
        ) ON [PRIMARY]
    """,
    """ if not exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[smHighWayDate]'))
        CREATE TABLE [dbo].[smHighWayDate] (
        [Xuhao] [bigint] IDENTITY (1, 1) NOT NULL ,
        [RecordID] [bigint] NOT NULL ,
        [SiteID] [int] NOT NULL ,
        [smDevCode] [varchar] (20) COLLATE Chinese_PRC_CI_AS NULL ,
        [smTime] [datetime] NULL ,
        [VehicheCard] [varchar] (30) COLLATE Chinese_PRC_CI_AS NULL ,
        [smVehicheStr] [varchar] (20) COLLATE Chinese_PRC_CI_AS NULL ,
        [smState] [varchar] (10) COLLATE Chinese_PRC_CI_AS NULL ,
        [smWheelCount] [tinyint] NULL ,
        [smSpeed] [decimal](9, 2) NULL ,
        [smTotleAxesSpace] [decimal](9, 2) NULL ,
        [smTotalWeight] [decimal](9, 2) NULL ,
        [smRoadNum] [tinyint] NULL ,
        [smLimitWeight] [decimal](9, 2) NULL ,
        [smLimitWeightPercent] [decimal](9, 1) NULL ,
        [smPlatePath] [varchar] (200) COLLATE Chinese_PRC_CI_AS NULL ,
        [smImgPath] [varchar] (200) COLLATE Chinese_PRC_CI_AS NULL ,
        [smLengh] [decimal](9, 2) NULL ,
        [smWidth] [decimal](9, 2) NULL ,
        [smHeight] [decimal](9, 2) NULL ,
        [smOverLengh] [decimal](9, 2) NULL ,
        [smOverWidth] [decimal](9, 2) NULL ,
        [smOverHeight] [decimal](9, 2) NULL ,
        [smUser] [varchar] (20) COLLATE Chinese_PRC_CI_AS NULL ,
        [ReadFlag] [tinyint] NULL ,
        [BAKE] [varchar] (200) COLLATE Chinese_PRC_CI_AS NULL
        ) ON [PRIMARY]
    """,
    """ if not exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[smSites]'))
        CREATE TABLE [dbo].[smSites] (
        [ID] [int] IDENTITY (1, 1) NOT NULL ,   
        [SiteID] [int] NULL ,
        [SiteName] [varchar] (50) COLLATE Chinese_PRC_CI_AS NULL ,
        [SiteInfo] [varchar] (50) COLLATE Chinese_PRC_CI_AS NULL
        ) ON [PRIMARY]
    """,
    """ if not exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[blacklist]'))
        CREATE TABLE [dbo].[blacklist] (
        [SeqNum] [bigint] IDENTITY (1, 1) NOT NULL ,
        [Time] [datetime] NOT NULL ,
        [Plate] [varchar] (30) COLLATE Chinese_PRC_CI_AS NOT NULL,
        [State] [int] NOT NULL
        ) ON [PRIMARY]
    """
]

def retr_img_from_ftp(filename):
  import os
  usr, passwd = 'WeightDataService', '660328'
  hosts = ['172.16.33.3']
  ret = True
  print 'get pic'
  localfn = filename.replace('/', '_')
  with open(localfn, 'wb') as lf:
    for host in hosts:
      try:
        ftp = FTP(host, timeout=0.5)
        ftp.login(usr, passwd)
      except Exception as e:
        print e
        ret = False
      else:
        try:
          ftp.retrbinary('RETR ' + filename, lf.write)
        except Exception as e:
          print 'get pic failed', e
          ret = False
        finally:
          ftp.quit()
    if not ret:
      os.remove(localfn)
    return ret

def get_param():
    global host, inst, user, pswd, dbnm, ftpp
    with open('conf.txt', 'rb') as conf:
        for ln in conf:
            param = ln.split()
            if   param[0] == 'host': host = param[1]
            elif param[0] == 'inst': inst = param[1]
            elif param[0] == 'user': user = param[1]
            elif param[0] == 'pass': pswd = param[1]
            elif param[0] == 'dbnm': dbnm = param[1]
            elif param[0] == 'ftpp': ftpp = param[1]
            else: pass

def exec_sql_file(cur, f):
    sqlstr = ''
    with open(f, 'r') as fd:
        for line in fd:
            if len(line) < 5:
                print sqlstr
                cur.execute(sqlstr)
                sqlstr = ''
            elif 'PRINT' in line:
                print line.split("'")[1]
            else:
                sqlstr += line


def connectdb():
    conn = pymssql.connect('%s'%(host,), '%s'%(user,), pswd, dbnm, charset='utf8')
    #conn = pymssql.connect('172.16.33.3', 'WeightDataService', '660328', 'sifang', charset='utf8')
    conn.autocommit(True)
    return conn

def drop_existing_tables():
    conn = connectdb()
    cur = conn.cursor()
    for s in init_db_cmds:
        cur.execute(s)
    conn.close()

def drop_table(tn):
    conn = connectdb()
    cur = conn.cursor()
    cur.execute(init_db_cmds[tabname2sqlcmd[tn]])
    conn.close()

def create_tables():
    #drop_table('blacklist')
    conn = connectdb()
    cur = conn.cursor()
    for s in setup_db_cmds:
        cur.execute(s)
    # alter table already exists
    try: cur.execute('ALTER TABLE [dbo].[smHighWayDate] ADD ProcTime [datetime] NULL')
    except Exception as e: print e
    conn.close()

def fetch_all_veh_recs():
    conn = connectdb()
    cur = conn.cursor(as_dict=True)
    cur.execute('SELECT * FROM smHighWayDate')
    results = [UserDb.Record.TAB_HDR]
    rows = cur.fetchall()
    if rows:
        for row in rows:
            results.append((row['Xuhao'], row['RecordID'], row['SiteID'], row['smTime'], row['VehicheCard'],
                            row['smState'], row['smWheelCount'], row['smSpeed'], row['smTotalWeight'],
                            row['smRoadNum'], row['smLimitWeight'], row['smLimitWeightPercent'], row['ProcTime'],
                            row['smPlatePath'], row['smImgPath']))
    conn.close()
    return results

def fetch_all_veh_recs_brf():
    conn = connectdb()
    cur = conn.cursor(as_dict=True)
    cur.execute('SELECT * FROM smHighWayDate')
    results = [UserDb.Record.TAB_BRF_HDR]
    rows = cur.fetchall()
    if rows:
        for row in rows:
            results.append((row['Xuhao'], row['RecordID'], row['smTime'], row['VehicheCard']))
    conn.close()
    return results

def fetch_all_bad():
    conn = connectdb()
    cur = conn.cursor(as_dict=True)
    cur.execute('SELECT * FROM smHighWayDate WHERE smState=%s', u'超限')
    results = [UserDb.Record.TAB_HDR]
    rows = cur.fetchall()
    if rows:
        for row in rows:
            results.append((row['Xuhao'], row['RecordID'], row['SiteID'], row['smTime'], row['VehicheCard'],
                            row['smState'], row['smWheelCount'], row['smSpeed'], row['smTotalWeight'],
                            row['smRoadNum'], row['smLimitWeight'], row['smLimitWeightPercent'], row['ProcTime'],
                            row['smPlatePath'], row['smImgPath'], row['ReadFlag']))
    conn.close()
    return results

def fetch_all_bad_brf(n):
    conn = connectdb()
    cur = conn.cursor(as_dict=True)
    cur.execute('SELECT TOP 30 * FROM smHighWayDate WHERE smState=%s ORDER BY Xuhao DESC', u'正常')
    results = [UserDb.Record.TAB_BRF_HDR]
    rows = cur.fetchall()
    if rows:
        for row in rows:
            results.append((row['Xuhao'], get_site_name(row['SiteID']), 
                            row['smTime'], row['VehicheCard'], row['smTotalWeight']/1000,
                            row['smLimitWeightPercent'], status[row['ReadFlag']],))
    conn.close()
    return results

def fetch_all_good():
    conn = connectdb()
    cur = conn.cursor(as_dict=True)
    cur.execute('SELECT * FROM smHighWayDate WHERE smState=%s', u'正常')
    results = [UserDb.Record.TAB_HDR]
    rows = cur.fetchall()
    if rows:
        for row in rows:
            results.append((row['Xuhao'], row['RecordID'], row['SiteID'], row['smTime'], row['VehicheCard'],
                            row['smState'], row['smWheelCount'], row['smSpeed'], row['smTotalWeight'],
                            row['smRoadNum'], row['smLimitWeight'], row['smLimitWeightPercent'],
                            row['smPlatePath'], row['smImgPath'], row['ReadFlag']))
    conn.close()
    return results

def fetch_all_good_brf():
    conn = connectdb()
    cur = conn.cursor(as_dict=True)
    cur.execute('SELECT * FROM smHighWayDate WHERE smState=%s', u'正常')
    results = [UserDb.Record.TAB_BRF_HDR]
    rows = cur.fetchall()
    if rows:
        for row in rows:
            results.append((row['Xuhao'], row['RecordID'], row['smTime'], row['VehicheCard']))
    conn.close()
    return results

def fetch_recs(ow='', proc='', brf=True):
    if ow == '':
        if brf:
            return fetch_all_veh_recs_brf()
        else:
            return fetch_all_veh_recs()
    elif ow == 'yes':
        if brf:
            return fetch_all_bad_brf()
        else:
            return fetch_all_bad()
    elif ow == 'no':
        if brf:
            return fetch_all_good_brf()
        else:
            return fetch_all_good()

def fetch_cond_recs(cond, interval, brf=True):
    conn = connectdb()
    cur = conn.cursor(as_dict=True)
    if interval:
        timestr = " smTime between \'%s\' and \'%s\'"%(interval[0], interval[1])
    else: timestr = ''
    if cond[0]:
        if timestr: timestr = ' and ' + timestr
        cur.execute('SELECT * FROM smHighWayDate WHERE ' + cond[0] + timestr, cond[1])
    else:
        if timestr: timestr = ' WHERE ' + timestr
        print timestr
        cur.execute('SELECT * FROM smHighWayDate' + timestr)
    rows = cur.fetchall()
    if rows:
        if brf:
            results = [UserDb.Record.TAB_BRF_HDR]
            for row in rows:
                results.append((row['Xuhao'], get_site_name(row['SiteID']), 
                                row['smTime'], row['VehicheCard'], row['smTotalWeight']/1000,
                                row['smLimitWeightPercent'], status[row['ReadFlag']],))
        else:
            results = [UserDb.Record.TAB_HDR]
            for row in rows:
                if not os.path.isfile(row['smPlatePath'].replace(r'\\', '_')):
                    retr_img_from_ftp(row['smPlatePath'].replace(r'\\', '/'))
                if not os.path.isfile(row['smImgPath'].replace(r'\\', '_')):
                    retr_img_from_ftp(row['smImgPath'].replace(r'\\', '_'))
                results.append(
                               ((row['Xuhao'], get_site_name(row['SiteID']),
                                 datetime.strftime(row['smTime'], '%Y-%m-%d %H:%M:%S'),
                                 row['VehicheCard'], row['smTotalWeight']/1000,
                                 row['smLimitWeightPercent'], status[row['ReadFlag']],),
                                (row['Xuhao'], row['RecordID'], get_site_name(row['SiteID']), row['smTime'], row['VehicheCard'],
                                 row['smState'], row['smWheelCount'], row['smSpeed'], row['smTotalWeight']/1000,
                                 row['smRoadNum'], row['smLimitWeight'], row['smLimitWeightPercent'], row['ProcTime'],
                                 row['smPlatePath'].replace(r'\\', '_'), row['smImgPath'].replace(r'\\', '_'), 
                                 row['ReadFlag'])
                              )
                            )
    else:
        results = None

    return results

def get_site_name(siteid):
    conn = connectdb()
    cur = conn.cursor(as_dict=True)
    cur.execute('SELECT * FROM smSites WHERE SiteID=%d', siteid)
    sn = cur.fetchone()
    conn.close()
    return sn['SiteName']

def update_read_flag(seq, value):
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('UPDATE smHighWayDate SET ReadFlag=%d, ProcTime=CAST(%s AS DATETIME) WHERE Xuhao=%d', 
                (value, datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M:%S'), seq))
    conn.close()

def update_regtime(seq, ts):
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('UPDATE smHighWayDate SET ProcTime=CAST(%s AS DATETIME) WHERE Xuhao=%d', (ts, seq))
    conn.close()

def get_blacklist():
    conn = connectdb()
    cur = conn.cursor(as_dict=True)
    cur.execute('SELECT * FROM blacklist')
    res = []
    rows = cur.fetchall()
    if rows:
        for row in rows:
            res.append((row['SeqNum'], row['Plate'], row['Time'], row['State']))
    conn.close()
    return res

def update_blacklist_state(seq, state):
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('UPDATE blacklist SET State=%d WHERE SeqNum=%d', (state, seq))
    conn.close()

def get_blacklist_state(seq):
    conn = connectdb()
    cur = conn.cursor(as_dict=True)
    cur.execute('SELECT * FROM blacklist WHERE SeqNum=%d', seq)
    row = cur.fetchone()
    conn.close()
    return row['State']

def approve_blacklist(seq):
    update_blacklist_state(seq, UserDb.BlackList.APPROVED)

def add_blacklist(plate):
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('INSERT blacklist VALUES (CAST (%s AS DATETIME), %s, %d)', 
        (datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'), plate, UserDb.BlackList.REQUESTING))
    conn.close()

def del_blacklist(seq):
    conn = connectdb()
    cur = conn.cursor()
    try: cur.execute('DELETE FROM blacklist WHERE SeqNum=%d', seq)
    except Exception as e: print e
    conn.close()

def cancel_blacklist_state(seq):
    conn = connectdb()
    cur = conn.cursor()
    state = get_blacklist_state(seq)
    if state == UserDb.BlackList.REQUESTING:
        del_blacklist(seq)
    elif state == UserDb.BlackList.DELETING:
        update_blacklist_state(seq, UserDb.BlackList.APPROVED)

def confirm_blacklist_state(seq):
    conn = connectdb()
    cur = conn.cursor()
    state = get_blacklist_state(seq)
    if state == UserDb.BlackList.REQUESTING:
        update_blacklist_state(seq, UserDb.BlackList.APPROVED)
    elif state == UserDb.BlackList.DELETING:
        del_blacklist(seq)

def test_main():
    conn = connectdb()
    cur = conn.cursor()
    #exec_sql_file(cur, r'../sifang/sifang.sql')
    #cur.execute('SELECT * FROM smHighWayDate WHERE VehicheCard=%s', '无车牌'.decode('utf-8'))
    #cur.execute('SELECT * FROM smHighWayDate')
    #for r in cur.fetchall():
    #    print r
    #cur.execute('ALTER TABLE [dbo].[smHighWayDate] ADD ProcTime [datetime] NULL')
    cur.execute('INSERT blacklist VALUES (%s, %s)', ('2015-08-30 13:23:08', u'浙A124FA'))
    cur.close()
    conn.close()

if __name__ == '__main__':
    #test_main()
    get_param() 

