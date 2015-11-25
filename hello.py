#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3

print "Content-type: text/html\n\n"
print "<html>"
print "<head><meta charset='UTF-8'></head>"
print "<body>"
print "<h1>NIS Request List 需求列表</h1>"
print '''<script>
function confirmDel(n){
	var form;
	if(confirm("确认删除此条吗?")){
		form = document.createElement('form');
		document.body.appendChild(form);
		var input = document.createElement('input');
		input.setAttribute('type','hidden');
		input.setAttribute('name','fDelete');
		input.setAttribute('value',n);
		form.appendChild(input);
		form.setAttribute('action',"/cgi-bin/delrequest.py")
		form.setAttribute('method','post');
		form.submit();
		
	}
}
</script>
'''
conn=sqlite3.connect('/usr/share/pyplate/database/nisrequest.db')
curs=conn.cursor()
rows=curs.execute("SELECT ROWID,* FROM requesttable")
print "<table border='1'>"
for index,row in enumerate(rows):
	ftype=row[1]
	if ftype=="software":
		print "<tr bgcolor=#fff0f0>"
        elif ftype=="hardwareA":
                print "<tr bgcolor=#f0fff0>"
        elif ftype=="hardwareB":
                print "<tr bgcolor=#f0f0ff>"
	else:
		print "<tr>"
	print "<td>"+str(index)+"</td>"
        for s in row[1:]:#rowid is int type
		print "<td>"
                print s.encode('utf-8')
		print "</td>"
	if index!=0:
		print "<td><button onclick=confirmDel('%s')>x</button></td>" %str(row[0])#row[0] is rowid
	print "</tr>"
print "</table>"
conn.close()

html_form = '''

<form action="/cgi-bin/getrequest.py" methord="POST">
<table>
<tr>
	<td>
	Type
	</td>
	<td>
	<select name="fNo">
	<option value="software">Software</option>
        <option value="hardwareA">HardwareA (laser system)</option>
        <option value="hardwareB">HardwareB (normal system)</option>
	</select>
	<td>
</tr>
<tr>
	<td>
	Category
	</td>
	<td>
	<select name="fCategory">
	<option value="Confocal">Confocal</option>
	<option value="A1">A1/A1R</option>
	<option value="MP">A1R MP</option>
	<option value="C2">C2</option>
	<option value="SR">Super resolution</option>
	<option value="STORM">STORM</option>
	<option value="SIM">SIM</option>
	<option value="STORMSIM">STORM/SIM</option>
	<option value="LAPP">LAPP</option>
	<option value="HCA">HCA</option>
	<option value="LU">Laser unit</option>
	<option value="Others">Others</option>
	</select>
	</td>
</tr>
<tr>
	<td>
	Request
	</td>
	<td>
	<textarea name="fRequest" cols=20 rows=5></textarea>
	</td>
</tr>
<tr>
	<td>
	Remark
	</td>
	<td>
	<textarea name="fRemark" cols=20 rows=5></textarea>
	</td>
</tr>
<tr>
	<td>
	From
	</td>
	<td>
	<textarea name="fFrom" cols=20 rows=1></textarea>
	</td>
</tr>
<tr>
	<td>
	Reference
	</td>
	<td>
	<textarea name="fReference" cols=20 rows=1></textarea>
	</td>
</tr>
<tr>
	<td>
	Schedule
	</td>
	<td>
	<textarea name="fSchedule" cols=20 rows=1></textarea>
	</td>
</tr>
<tr>
	<td>
	Status
	</td>
	<td>
	<textarea name="fStatus" cols=20 rows=1></textarea>
	</td>
</tr>
<tr>
	<td>
	Comment
	</td>
	<td>
	<textarea name="fComment" cols=20 rows=1></textarea>
	</td>
</tr>
<tr>
	<td>
	<input type="submit" value="Submit">
	</td>
	<td>
	<input type="reset" value="Reset">
	</td>
</tr>
</table>
</form>

'''

print html_form

print "</body>"
print "</html>"
