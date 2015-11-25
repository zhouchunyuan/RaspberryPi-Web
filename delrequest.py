#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys
#import urllib2
import cgi
import cgitb
import sqlite3

cgitb.enable()

form=cgi.FieldStorage()

try:
	conn=sqlite3.connect('/usr/share/pyplate/database/nisrequest.db')
	curs=conn.cursor()

	if "fDelete" in form:
		cmdString = 'DELETE FROM requesttable WHERE ROWID= '
		cmdString=cmdString+form["fDelete"].value
		curs.execute(cmdString)
		conn.commit()
		#print "Content-type: text/html\n\n"
		#print cmdString
		os.system("python hello.py")
		conn.close()
        	#sys.exit()
	else:
		print "Content-type: text/html\n\n"
		print "did not find fRequest error!"
		conn.close()
		sys.exit()
except Exception as e:
	print "Content-type: text/html\n\n"
	print str(e)
	conn.rollback()
	conn.close()
	raise e

