#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymssql
import UserDb

"""
    odbc db manipulation
"""

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
	"""
]

setup_db_cmds = [
	""" CREATE TABLE [dbo].[LimitW] (
    	[VehicheType] [int] NOT NULL ,
    	[LimitWeight] [int] NOT NULL
		) ON [PRIMARY]
	""",
	""" CREATE TABLE [dbo].[smArea] (
    	[ID] [int] IDENTITY (1, 1) NOT NULL ,
    	[AreaID] [int] NULL ,
    	[AreaName] [nvarchar] (50) COLLATE Chinese_PRC_CI_AS NULL ,
    	[AreaInfo] [nvarchar] (50) COLLATE Chinese_PRC_CI_AS NULL ,
    	[SiteID] [int] NULL
		) ON [PRIMARY]
	""",
	""" CREATE TABLE [dbo].[smHighWayDate] (
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
	""" CREATE TABLE [dbo].[smSites] (
		[ID] [int] IDENTITY (1, 1) NOT NULL ,   
		[SiteID] [int] NULL ,
		[SiteName] [varchar] (50) COLLATE Chinese_PRC_CI_AS NULL ,
		[SiteInfo] [varchar] (50) COLLATE Chinese_PRC_CI_AS NULL
		) ON [PRIMARY]
	"""
]


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
	conn = pymssql.connect(r'192.168.0.6\sqlexpress', r'.\haitong', r'111111', r'mytestdb')
	#conn = pymssql.connect(r'10.140.163.132\sqlexpress', r'.\quentin', r'111111', r'ssss')
	conn.autocommit(True)
	return conn

def drop_existing_tables():
	conn = connectdb()
	cur = conn.cursor()
	for s in init_db_cmds:
		cur.execute(s)
	conn.close()

def create_tables():
	conn = connectdb()
	cur = conn.cursor()
	for s in setup_db_cmds:
		cur.execute(s)
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
							row['smRoadNum'], row['smLimitWeight'], row['smLimitWeightPercent'],
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
							row['smRoadNum'], row['smLimitWeight'], row['smLimitWeightPercent'],
							row['smPlatePath'], row['smImgPath']))
	conn.close()
	return results

def fetch_all_bad_brf():
	conn = connectdb()
	cur = conn.cursor(as_dict=True)
	cur.execute('SELECT * FROM smHighWayDate WHERE smState=%s', u'超限')
	results = [UserDb.Record.TAB_BRF_HDR]
	rows = cur.fetchall()
	if rows:
		for row in rows:
			results.append((row['Xuhao'], row['RecordID'], row['smTime'], row['VehicheCard']))
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
							row['smPlatePath'], row['smImgPath']))
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

def test_main():
	conn = connectdb()
	cur = conn.cursor()
	#exec_sql_file(cur, r'../sifang/sifang.sql')
	cur.execute('SELECT * FROM smHighWayDate')
	for r in cur.fetchall():
		print r[0], r[1]
	cur.close()
	conn.close()

if __name__ == '__main__':
	test_main()	

