#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys
#import urllib2
import cgi
import cgitb
import sqlite3

cgitb.enable()

form=cgi.FieldStorage()

conn=sqlite3.connect('/usr/share/pyplate/database/nisrequest.db')
curs=conn.cursor()

cmdString = 'INSERT INTO requesttable values( '
if "fNo" in form:
	cmdString=cmdString+"\""+ form["fNo"].value +"\""
else:
	cmdString=cmdString+"\""+"\""
cmdString=cmdString+','
if "fCategory" in form:
        cmdString=cmdString+"\""+ form["fCategory"].value +"\""     
else:
        cmdString=cmdString+"\""+"\""
cmdString=cmdString+','
if "fRequest" in form:
	formStr = form["fRequest"].value
        cmdString=cmdString+"\""+ formStr.replace("\"","'") +"\""     
else:
        #cmdString=cmdString+"\""+"\""
	print "Content-type: text/html\n\n"
	print "you did not fill in the request, please go back and retry."
	conn.close()
	sys.exit()
cmdString=cmdString+','
if "fRemark" in form:
	formStr = form["fRemark"].value
        cmdString=cmdString+"\""+ formStr.replace("\"","'") +"\""     
else:
        cmdString=cmdString+"\""+"\""
cmdString=cmdString+','
if "fFrom" in form:
        cmdString=cmdString+"\""+ form["fFrom"].value +"\""     
else:
        cmdString=cmdString+"\""+"\""
cmdString=cmdString+','
if "fReference" in form:
        cmdString=cmdString+"\""+ form["fReference"].value +"\""     
else:
        cmdString=cmdString+"\""+"\""
cmdString=cmdString+','
if "fSchedule" in form:
        cmdString=cmdString+"\""+ form["fSchedule"].value +"\""     
else:
        cmdString=cmdString+"\""+"\""
cmdString=cmdString+','
if "fStatus" in form:
        cmdString=cmdString+"\""+ form["fStatus"].value +"\""     
else:
        cmdString=cmdString+"\""+"\""
cmdString=cmdString+','
if "fComment" in form:
        cmdString=cmdString+"\""+ form["fComment"].value +"\""     
else:
        cmdString=cmdString+"\""+"\""
cmdString=cmdString+')'
curs.execute(cmdString)
conn.commit()

conn.close()

os.system("python hello.py")
#response=urllib2.urlopen('http://www.baidu.com')


