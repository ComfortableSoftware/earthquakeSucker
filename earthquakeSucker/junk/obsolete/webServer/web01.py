#!/usr/bin/python


import web
from web import form
# from web.wsgiserver import CherryPyWSGIServer
import gc


from dataStuff import constants as C
from dataStuff import timeDateStuff as TDS
# from dataStuff import dataStuff as DS
from DBStuff import DBStuff as DB


gc.enable()
HTMLurls = (
	"/presets", "presets",
	"/quakes?", "quakes",
	"/quakes/?", "quakes",
	"/form", "htmlForm",
	"/menu", "mainMenu",
	"/zwrd?", "zwrd",
	"/zwrd/?", "zwrd",
	"/.*", "defaultUrl",
)
HTMLapp = web.application(HTMLurls, globals())
myCurrentQueries = C.QUERIESINGLOBALDEFAULTS
render = web.template.render('templates')  # your templates
vpass = form.regexp(r".{3,20}$", 'must be between 3 and 20 characters')
vemail = form.regexp(r".*@.*", "must be a valid email address")
register_form = form.Form(
	form.Textbox("username", description="Username"),
	form.Textbox("email", vemail, description="E-Mail"),
	form.Password("password", vpass, description="Password"),
	form.Password("password2", description="Repeat password"),
	form.Button("submit", type="submit", description="Register"),
	validators=
	[
		form.Validator("Passwords did't match", lambda i: i.password == i.password2)
	]
)


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * send an auto-expire no cache etc header set and load a style sheet, start the basic page, etc.
# * pass in the title to be added to the <title></title> 
# * returns the string to take a page to the </body> (including <body>)
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def sendMyHeader(myTitle):
	# web.ctx.env
	# web.header("Expires", ": Fri, 14 Oct 1989 19:30:00 GMT")
	web.header("Expires:", TDS.gmdate)
	web.header("Last-Modified:", TDS.gmdate)
	web.header("cache-control", "no-store, no-cache, must-revalidate")
	web.header("Pragma", "no-cache")
	with open('styles.css', 'r') as content_file:
		content = content_file.read()
	strToReturn = """
<!DOCTYPE html>
<html lang="en">
	<head>
		<title>""" + myTitle + """ </title>
"""
	strToReturn += content + """
	</head>
	<body>
		"""
	return strToReturn


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * display presets and things sent in via myCurrentQueries
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
class quakes:
	def GET(self):
		global myCurrentQueries
		DBLinks = DB.doOpen(C.SQLCONFIG)
		myInput = web.input(STARTRECNUM=0, QUERYNUM=1)
		if myInput[C.QUERYNUM] != myCurrentQueries[C.QUERYNUM]:
			myCurrentQueries = C.QUERIESINGLOBALDEFAULTS
		myCurrentQueries[C.STARTRECNUM] = myInput[C.STARTRECNUM]
		myCurrentQueries[C.QUERYNUM] = myInput[C.QUERYNUM]
		myCurrentQueries[C.ROWNUM] = 0
		SQLStr = f"""
select * from {C.QUERIESINTABLENAME}
where {C.RID} = {myCurrentQueries[C.QUERYNUM]};"""
		SQLRowsDict = DB.getSqlOne(DBLinks, SQLStr)
		myCurrentQueries = DB.upgradeDBToGQI(SQLRowsDict, C.QUERIESINGLOBALDEFAULTS)
		outStr = sendMyHeader(f"{myCurrentQueries[C.QUERIESINTITLE]}  {__file__}")
		SQLStr = f"""
{myCurrentQueries[C.SQLSELECT]}
{myCurrentQueries[C.SQLWHERE]}
{myCurrentQueries[C.SQLGROUPBY]} 
{myCurrentQueries[C.SQLORDERBY]}
"""
		SQLStr += DB.saneMakeSqlLimitStr(myCurrentQueries[C.STARTRECNUM]) + ";"
		SQLRowsDict, SQLNumRows = DB.getSqlAll(DBLinks, SQLStr)
		myCurrentQueries[C.NUMROWS] = SQLNumRows
		myCurrentQueries[C.PGNUM] = int(int(myCurrentQueries[C.STARTRECNUM]) / C.NUMROWSPERPG) + 1
		myCurrentQueries[C.OFPGS] = int(int(myCurrentQueries[C.NUMROWS]) / C.NUMROWSPERPG) + 1
		# theseRows = DB.upgradeDBToGQIMany(SQLRowsDict, C.QUERIESINGLOBALDEFAULTS)
		outStr += "<table>\n"
		for thisRow in SQLRowsDict:
			thisRow = DB.DTfixThisLineToDisplay(thisRow)
			lastRow = thisRow
			outStr += DB.makeTableRow(thisRow, myCurrentQueries, 0)
			myCurrentQueries[C.ROWNUM] += 1
		outStr += DB.makeTableRow(lastRow, myCurrentQueries, 1)
		outStr += """
		</table>
		<span class="fp">bottom of the page</span>
	</body>
</html>
"""
		return outStr


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * the handler for any URL not oitherwise consumed or dealt with
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
class defaultUrl:
	def GET(self):
		outStr = sendMyHeader("empty link") + """
		<span class="close0r1">
			try <a href="192.168.0.16:8080/presets">192.168.0.16:8080/presets</a><br />
			or  <a href="192.168.0.16:8080/form">192.168.0.16:8080/form</a><br />			
		</span>
	</body>
</html>
		"""
		return outStr


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * build a form to post queries from
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
class htmlForm:
	def GET(self):
		outStr = ""
		return outStr

	def POST(self):
		global myCurrentQueries
		if myCurrentQueries[C.ISLOADED] != 1:
			raise web.seeother("/done")


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * main menu, uses menuTable to store guts for the tmenu
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
class mainMenu:
	def GET(self):
		outStr = sendMyHeader("empty link") + """
		<span class="close0r1">
			try <a href="192.168.0.16:8080/presets">192.168.0.16:8080/presets</a><br />
			or  <a href="192.168.0.16:8080/form">192.168.0.16:8080/form</a><br />			
		</span>
	</body>
</html>
		"""
		print(outStr)
		return outStr


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * where the presets are linked to be shown, loops through the queriesIn table listing each available option
# * and send the query ID number to class quakes
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
class presets:
	def GET(self):
		global myCurrentQueries
		myCurrentQueries = C.QUERIESINGLOBALDEFAULTS
		DBLinks = DB.doOpen(C.SQLCONFIG)
		outStr = sendMyHeader("Presets")
		SQLStr = f"""
select RID, {C.QUERIESINTITLE} from {C.QUERIESINTABLENAME};"""
		SQLRows, SQLNumRows = DB.getSqlAll(DBLinks, SQLStr)
		outStr += f"""
<table>
"""
		rowCount = 0
		for thisRow in SQLRows:
			rowState = rowCount % 1
			outStr += f"""
<tr>
<td class="r{rowState}">
<a href="quakes?STARTNUM=0&QUERYNUM={thisRow[C.RID]}">{thisRow[C.QUERIESINTITLE]}</a>
</td>
</tr>
"""
			# end of for thisRow
		outStr += f"""
</table>
"""
		return outStr


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * hot forward values to quakes because web.py seems otherwise unable to link a page with passed and not passed 
# * parameters
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
class zwrd:
	def GET(self):
		myInput = web.input(STARTRECNUM=0, QUERYNUM=1)
		print(f"forwarding to {repr(myInput)}")
		web.seeother(f"""http://192.168.0.16:8080/quakes?STARTRECNUM={myInput[C.STARTRECNUM]}&QUERYNUM={myInput[C.QUERYNUM]}""")


if __name__ == "__main__":
	HTMLapp.run()
	print("we made it")
