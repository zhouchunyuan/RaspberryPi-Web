#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3

conn=sqlite3.connect('nisrequest.db')
curs=conn.cursor()
table = 'requesttable'
fields=['fNo',\
	'fCategory',\
	'fRequest',\
	'fRemark',\
	'fFrom',\
	'fReference',\
	'fSchedule',\
	'fStatus',\
	'fComment']
cmd = 'CREATE TABLE ' + table + ' ('
for index,field in enumerate(fields):
	cmd=cmd+field+' TEXT'
	if field=="fRequest":
		cmd=cmd+' primary key'
	if( index<len(fields)-1 ):
		cmd=cmd+','
cmd=cmd+')'
print cmd
curs.execute(cmd)

content=['Type(软硬件)',\
        'Category',\
        'Request',\
        'Remark',\
        'From',\
        'Reference',\
        'Schedule',\
        'Status',\
        'Comment']

cmd = ' INSERT INTO ' + table + ' values('
for index,field in enumerate(content):
	cmd=cmd+"\""+field+"\""
	if( index<len(content)-1 ):
		cmd=cmd+','
cmd=cmd+')'
print cmd
curs.execute(cmd)
conn.commit()

conn.close()

