#!/bin/python
#-*- coding: utf-8 -*-

"""
  Simple web server for local application management, based on bottle framework
  Author: haitong.chen@gmail.com
"""

import sys

import time, urllib2, sqlite3, re, socket, os
import time, urllib2, sqlite3
#import SqlCmdHelper
from datetime import datetime
from subprocess import Popen
from multiprocessing import Process
from bottle import route, request, redirect, template,static_file, run, app, hook
from ftplib import FTP
from beaker.middleware import SessionMiddleware
import UserDb


session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 3600,
    'session.data_dir': './data',
    'session.auto': True
}
app = SessionMiddleware(app(), session_opts)

def set_act_user(usrname):
  request.session['logged_in'] = usrname

def get_act_user():
  if 'logged_in' in request.session:
    return request.session['logged_in']
  else:
    return None

def cons_query_where_clause(query_mapping):
  conds = ['=:'.join([col, col]) for col in query_mapping.keys()]
  cond_str = ' and '.join(conds)
  return cond_str

def cons_query_interval(start, end):
  timefmt = '%Y-%m-%d'
  try:
    [datetime.strptime(t, timefmt) for t in (start, end)]
  except ValueError:
    return None
  else:
    return start + ' 00:00:00', end + ' 23:59:59'

def validate_from_db(usr, passwd):
  user = UserDb.get(usr)
  if user is not None and user.usrname == usr and user.password == passwd:
    ret = True, user
  else:
    ret = False, user
  return ret

def init_user_db():
  UserDb.create_user_table()
  UserDb.create_role_table()
  UserDb.add_root()
  UserDb.add_default_roles()
  UserDb.put_admin()

@hook('before_request')
def setup_request():
    request.session = request.environ['beaker.session']

@route('/')
def root():
  if get_act_user() is None:
    redirect('/login')
  else:
    redirect('/index')

@route('/login')
def login():
  return template('./view/bsfiles/view/signin.tpl',
                  custom_hdr="./view/bsfiles/view/signin_cus_file.tpl")

@route('/login', method='POST')
def do_login():
  #print request.get('REMOTE_ADDR'), ' connected'
  forgot = None
  usrname = request.forms.get('usrname')
  passwd = request.forms.get('passwd')
  rememberme = request.forms.get('rememberme')

  isvalid, user = validate_from_db(usrname, passwd)
  if isvalid:
    set_act_user(usrname)
    redirect('/index')
  else:
    redirect('/')

@route('/logout')
def logout():
  request.session.delete()
  redirect('/')

@route('/index')
def page_index():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  return template('./view/bsfiles/view/dashboard.tpl',
                  custom_hdr='./view/bsfiles/view/dashboard_cus_file.tpl',
                  user=act_user, query_results=None)

@route('/user_roles')
def role_mng():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  return template('./view/setting.tpl', setting='role_mng',
                  roles=UserDb.get_roles(),
                  privs=UserDb.get_privilege(act_user.role),
                  curr_user=get_act_user())

@route('/add_role', method='POST')
def add_role():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  rolename = request.forms.get('rn')
  op = request.forms.get('create')
  if op and rolename:
    r = UserDb.Role(rolename=rolename)
    #UserDb.add_role(r)
    r.put()
    redirect('/user_roles')
  else:
    op = request.forms.get('query')
    if op:
      redirect('/user_roles')

@route('/del_role/<rolename>')
def del_role(rolename):
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  UserDb.del_role(rolename)
  return rolename, '已删除'

@route('/edit_role/<rolename>')
def edit_role(rolename):
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  return template('./view/setting.tpl', setting='edit_role',
                  roles=UserDb.get_roles(), privs=UserDb.get_privilege(act_user.role),
                  role2edit=rolename, curr_user=get_act_user())

@route('/edit_role/<rolename>', method='POST')
def edit_role(rolename):
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  desc = request.forms.get('desc')
  status = request.forms.get('status')
  print desc, status, rolename
  UserDb.update_role_status_desc(rolename, status, desc)
  redirect('/user_roles')

@route('/access_control')
def access_control():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  return template('./view/setting.tpl', setting='access_granting',
                  roles=UserDb.get_roles(),
                  privs=UserDb.get_privilege(act_user.role),
                  curr_user=get_act_user())

@route('/access_grant', method='POST')
def grant():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  privs = ['sys', 'query', 'vehicle', 'driver', 'company', 'ship']
  granted = []
  for priv in privs:
    if request.forms.get(priv):
      granted.append(priv)
  role = request.forms.get('grant')
  print role
  UserDb.update_privilege(role, granted)

@route('/account_mngn')
def account_mngn():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  return template('./view/bsfiles/view/usr_mng.tpl',
                  custom_hdr='./view/bsfiles/view/dashboard_cus_file.tpl',
                  user=act_user,
                  usrs=UserDb.fetch_users())

@route('/del_user/<usrname>', method='POST')
def del_user(usrname):
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  print usrname, 'is going to be deleted'
  UserDb.del_user(usrname)
  redirect('/account_mngn')

@route('/edit_user/<usrname>')
def edit_user(usrname):
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  return template('./view/setting.tpl', setting='edit_user',
                  privs=UserDb.get_privilege(act_user.role),
                  usrname=usrname, roles=UserDb.get_roles(),
                  curr_user=get_act_user())

@route('/edit_user/<usrname>', method='POST')
def edit_user(usrname):
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  nickname = request.forms.get('nickname')
  desc = request.forms.get('desc')
  role = request.forms.get('role')
  print usrname, nickname, desc, role
  UserDb.change_user_info(usrname, desc, role, nickname)
  redirect('/account_mngn')

@route('/account_query', method="POST")
def account_query():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  user = request.forms.get('account')
  if request.forms.get('query'):
    return template('./view/setting.tpl', setting="accounts",
                    users=[UserDb.get(user)],
                    privs=UserDb.get_privilege(act_user.role),
                    curr_user=get_act_user())
  elif request.forms.get('create'):
    redirect('/user_update')

@route('/user_update')
def update_user():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  return template('./view/setting.tpl', setting="adduser",
                  roles=UserDb.get_roles(),
                  privs=UserDb.get_privilege(act_user.role),
                  curr_user=get_act_user())

@route('/update_user', method='POST')
def update_user():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  print 'update user'
  if request.forms.get('op') == 'update':
    usrname = request.forms.get('usrname')
    passwd  = request.forms.get('passwd')
    role    = request.forms.get('role')
    desc    = request.forms.get('desc')
    nickname= request.forms.get('nickname')
    print usrname, nickname
    newuser = UserDb.User(usrname, passwd, nickname=nickname, desc=desc, role=role)
    newuser.put()
  else:
    print 'user update cancelled!'
  redirect('/account_mngn')

@route('/del_user/<usrname>')
def del_user(usrname):
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  UserDb.del_user(usrname)
  redirect('/account_mngn')

@route('/change_passwd')
def change_passwd():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  return template('./view/setting.tpl', setting="change_password",
                  privs=UserDb.get_privilege(act_user.role),
                  curr_user=get_act_user())

@route('/change_passwd', method='POST')
def update_passwd():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  passwd = request.forms.get('newpass')
  cnfm_passwd = request.forms.get('confirmedpass')
  if passwd != cnfm_passwd:
    return '新密码两次输入不一致，请返回重试!'
  UserDb.change_passwd(act_user.usrname, passwd)
  redirect('/account_mngn')

@route('/static/<filename:path>')
def send_static(filename):
  return static_file(filename, root='./')


def main():
  #sdb.main()
  init_user_db()
  #dbporc = Process(target=sdb.run_sock_svr, args=())
  #dbporc.start()
  websvr = Process(target=run, args=(app, 'wsgiref', '0.0.0.0', '8081'))
  websvr.start()
  #dbporc.join()
  websvr.join()
  #run(host='localhost', port=8081, Debug=True, reloader=False)
  #run(host='localhost', port=80, Debug=True)


if __name__ == '__main__':
  main()
  #test_ftp()
