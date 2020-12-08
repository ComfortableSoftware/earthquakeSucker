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
	"/QGJ?", "quakesGJ",
	"/QGJ/?", "quakesGJ",
	"/form", "htmlForm",
	"/setDefault?", "setDefault",
	"/setDefault/?", "setDefault",
	"/menu", "mainMenu",
	"/zwrd?", "zwrd",
	"/zwrd/?", "zwrd",
	"/stop", "stopItAll",
	"/stop.*", "stopItAll",
	"/stop/", "stopItAll",
	"/stop/.*", "stopItAll",
	"/.*", "defaultUrl",
)
HTMLapp = web.application(HTMLurls, globals(), autoreload=True)
myCurrentQueries = C.QUERIESINDEFAULTS()
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
GTStr = ">"
LTStr = "<"
OBStr = "{"
CBStr = "}"


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * send an auto-expire no cache etc header set and load a style sheet, start the basic page, etc.
# * pass in the title to be added to the <title></title> 
# * returns the string to take a page to the </body> (including <body>)
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def sendMyHeader(myTitle, additionalStyleSheet=""):
	# web.ctx.env
	# web.header("Expires", ": Fri, 14 Oct 1989 19:30:00 GMT")
	web.header("Expires:", TDS.gmdate())
	web.header("Last-Modified:", TDS.gmdate())
	web.header("cache-control", "no-store, no-cache, must-revalidate")
	web.header("Pragma", "no-cache")
	with open('styles.css', 'r') as content_file:
		content1 = content_file.read()
	strRet = f"""
<!DOCTYPE html>
<html lang="en">
	<head>
		<title>{myTitle}</title>
		{content1}
	</head>
	<body>
		"""
	return strRet


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * display presets and things sent in via myCurrentQueries
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
class quakes:
	def GET(self):
		global myCurrentQueries
		DBLinks = DB.doOpen(C.SQLCONFIG)
		myInput = web.input(STARTRECNUM=0, QUERYNUM=C.DEFQUERYNUM)
		# C.QUERYLOADED (-1) if from select the parts
		# C.QUERYFROMPRESET (1) if from presets
		# C.QUERYEMPTY (0) if anything else
		if myInput[C.QUERYNUM] != myCurrentQueries[C.QUERYNUM]:
			myCurrentQueries = C.QUERIESINDEFAULTS()
			myCurrentQueries[C.QUERYNUM] = myInput[C.QUERYNUM]
			# C.QUERYLOADED if set by any of the query building parts,
			# C.QUERYFROMPRESET if loaded from a preset
			# C.QUERYEMPTY if "empty"
			myCurrentQueries[C.ISLOADED] = C.QUERYEMPTY
		myCurrentQueries[C.STARTRECNUM] = myInput[C.STARTRECNUM]
		myCurrentQueries[C.QUERYNUM] = myInput[C.QUERYNUM]
		myCurrentQueries[C.ROWNUM] = 0
		if myCurrentQueries[C.ISLOADED] != C.QUERYLOADED:
			SQLStr = f"""
select * from {C.QUERIESINTABLENAME}
where {C.RID} = {myCurrentQueries[C.QUERYNUM]};"""
			SQLRowsDict = DB.getSqlOne(DBLinks, SQLStr)
			myCurrentQueries = DB.upgradeDBToGQI(SQLRowsDict, myCurrentQueries)
			myCurrentQueries[C.ISLOADED] = 1
		C.REGIONNAMESDICT[C.REGION0NAME] = myCurrentQueries[C.REGION0NAME]
		C.REGIONNAMESDICT[C.REGION1NAME] = myCurrentQueries[C.REGION1NAME]
		C.REGIONNAMESDICT[C.REGION2NAME] = myCurrentQueries[C.REGION2NAME]
		C.REGIONNAMESDICT[C.REGION3NAME] = myCurrentQueries[C.REGION3NAME]
		C.REGIONDESCRIPTIONSDICT[C.REGION0DESCRIPTION] = myCurrentQueries[C.REGION0DESCRIPTION]
		C.REGIONDESCRIPTIONSDICT[C.REGION1DESCRIPTION] = myCurrentQueries[C.REGION1DESCRIPTION]
		C.REGIONDESCRIPTIONSDICT[C.REGION2DESCRIPTION] = myCurrentQueries[C.REGION2DESCRIPTION]
		C.REGIONDESCRIPTIONSDICT[C.REGION3DESCRIPTION] = myCurrentQueries[C.REGION3DESCRIPTION]
		outStr = sendMyHeader(f"""{myCurrentQueries[C.QUERIESINTITLE]}""", f"""styleChunk.css""")
		SQLStr = f"""
{myCurrentQueries[C.SQLSELECT]}
{myCurrentQueries[C.SQLWHERE]}
{myCurrentQueries[C.SQLGROUPBY]}
{myCurrentQueries[C.SQLHAVING]}
{myCurrentQueries[C.SQLORDERBY]}
"""
		SQLStr += DB.saneMakeSqlLimitStr(myCurrentQueries[C.STARTRECNUM]) + ";"
		SQLRowsDict, SQLNumRows = DB.getSqlAll(DBLinks, SQLStr)
		myCurrentQueries[C.NUMROWS] = SQLNumRows
		myCurrentQueries[C.PGNUM] = int(int(myCurrentQueries[C.STARTRECNUM]) / C.NUMROWSPERPG) + 1
		myCurrentQueries[C.OFPGS] = int(int(myCurrentQueries[C.NUMROWS]) / C.NUMROWSPERPG) + 1
		# theseRows = DB.upgradeDBToGQIMany(SQLRowsDict, C.QUERIESINGLOBALDEFAULTS)
		outStr += f"""
<span class="labels"><br />current SQLStr<br />{SQLStr}<br /></span><br />

"""
		outStr += "<table>\n"
		if myCurrentQueries[C.NUMROWS] < 1:
			outStr += f"""
<tr>
	<td class="close0r0">no entries found</td>
	<td class="close3r0"><a href="menu">click for the menu</a></td>
</tr>
<tr>
	<td class="close3r1"><a href="presets">presets</a></td>
	<td class="close2r0"><a href="quakes/?QUERYNUM={C.DEFQUERYNUM}&STARTRECNUM=0">
		for the default preset</a></td>
</tr>
<tr>
	<td class="close2r1"><a href="stop">stop the server</a></td>
	<td class="close1r0">{TDS.nowStrSql()}</td>
</tr>
</table>
</body>
</html>

"""
			return outStr
		for thisRow in SQLRowsDict:
			thisRow = DB.DTfixThisLineToDisplay(thisRow)
			lastRow = thisRow
			outStr += DB.makeTableRow(thisRow, myCurrentQueries, 0)
			myCurrentQueries[C.ROWNUM] += 1
		outStr += DB.makeTableRow(lastRow, myCurrentQueries, 1)
		outStr += f"""
		</table>
		<span class="fp">bottom of the page</span>
	</body>
</html>
"""
		return outStr


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * display presets and things sent in via myCurrentQueries
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
class quakesGJ:
	def GET(self):
		global myCurrentQueries
		DBLinks = DB.doOpen(C.SQLCONFIG)
		myInput = web.input(STARTRECNUM=0, QUERYNUM=C.DEFQUERYNUM)
		# C.QUERYLOADED (-1) if from select the parts
		# C.QUERYFROMPRESET (1) if from presets
		# C.QUERYEMPTY (0) if anything else
		if myInput[C.QUERYNUM] != myCurrentQueries[C.QUERYNUM]:
			myCurrentQueries = C.QUERIESINDEFAULTS()
			myCurrentQueries[C.QUERYNUM] = myInput[C.QUERYNUM]
			# C.QUERYLOADED if set by any of the query building parts,
			# C.QUERYFROMPRESET if loaded from a preset
			# C.QUERYEMPTY if "empty"
			myCurrentQueries[C.ISLOADED] = C.QUERYEMPTY
		myCurrentQueries[C.STARTRECNUM] = myInput[C.STARTRECNUM]
		myCurrentQueries[C.QUERYNUM] = myInput[C.QUERYNUM]
		myCurrentQueries[C.ROWNUM] = 0
		if myCurrentQueries[C.ISLOADED] != C.QUERYLOADED:
			SQLStr = f"""
select * from {C.QUERIESINTABLENAME}
where {C.RID} = {myCurrentQueries[C.QUERYNUM]};"""
			SQLRowsDict = DB.getSqlOne(DBLinks, SQLStr)
			myCurrentQueries = DB.upgradeDBToGQI(SQLRowsDict, myCurrentQueries)
			myCurrentQueries[C.ISLOADED] = 1
		C.REGIONNAMESDICT[C.REGION0NAME] = myCurrentQueries[C.REGION0NAME]
		C.REGIONNAMESDICT[C.REGION1NAME] = myCurrentQueries[C.REGION1NAME]
		C.REGIONNAMESDICT[C.REGION2NAME] = myCurrentQueries[C.REGION2NAME]
		C.REGIONNAMESDICT[C.REGION3NAME] = myCurrentQueries[C.REGION3NAME]
		C.REGIONDESCRIPTIONSDICT[C.REGION0DESCRIPTION] = myCurrentQueries[C.REGION0DESCRIPTION]
		C.REGIONDESCRIPTIONSDICT[C.REGION1DESCRIPTION] = myCurrentQueries[C.REGION1DESCRIPTION]
		C.REGIONDESCRIPTIONSDICT[C.REGION2DESCRIPTION] = myCurrentQueries[C.REGION2DESCRIPTION]
		C.REGIONDESCRIPTIONSDICT[C.REGION3DESCRIPTION] = myCurrentQueries[C.REGION3DESCRIPTION]
		outStr = sendMyHeader(f"""{myCurrentQueries[C.QUERIESINTITLE]}""", f"""styleChunk.css""")
		SQLStr = f"""
{myCurrentQueries[C.SQLSELECT]}
{myCurrentQueries[C.SQLWHERE]}
{myCurrentQueries[C.SQLGROUPBY]}
{myCurrentQueries[C.SQLHAVING]}
{myCurrentQueries[C.SQLORDERBY]}
"""
		SQLStr += DB.saneMakeSqlLimitStr(myCurrentQueries[C.STARTRECNUM]) + ";"
		SQLRowsDict, SQLNumRows = DB.getSqlAll(DBLinks, SQLStr)
		myCurrentQueries[C.NUMROWS] = SQLNumRows
		myCurrentQueries[C.PGNUM] = int(int(myCurrentQueries[C.STARTRECNUM]) / C.NUMROWSPERPG) + 1
		myCurrentQueries[C.OFPGS] = int(int(myCurrentQueries[C.NUMROWS]) / C.NUMROWSPERPG) + 1
		# theseRows = DB.upgradeDBToGQIMany(SQLRowsDict, C.QUERIESINGLOBALDEFAULTS)
		outStr += f"""
<span class="labels"><br />current SQLStr<br />{SQLStr}<br /></span><br />

"""
		outStr += "<table>\n"
		if myCurrentQueries[C.NUMROWS] < 1:
			outStr += f"""
<tr>
	<td class="close0r0">no entries found</td>
	<td class="close3r0"><a href="menu">click for the menu</a></td>
</tr>
<tr>
	<td class="close3r1"><a href="presets">presets</a></td>
	<td class="close2r0"><a href="quakes/?QUERYNUM={C.DEFQUERYNUM}&STARTRECNUM=0">
		for the default preset</a></td>
</tr>
<tr>
	<td class="close2r1"><a href="stop">stop the server</a></td>
	<td class="close1r0">{TDS.nowStrSql()}</td>
</tr>
</table>
</body>
</html>

"""
			return outStr
		for thisRow in SQLRowsDict:
			thisRow = DB.DTfixThisLineToDisplay(thisRow)
			lastRow = thisRow
			outStr += DB.makeTableRow(thisRow, myCurrentQueries, 0)
			myCurrentQueries[C.ROWNUM] += 1
		outStr += DB.makeTableRow(lastRow, myCurrentQueries, 1)
		outStr += f"""
		</table>
		{DB.makeDistance()}
		<span class="fp">bottom of the page</span>
	</body>
</html>
"""
		return outStr


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * the handler for any URL not otherwise consumed or dealt with
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
class defaultUrl:
	def GET(self):
		outStr = sendMyHeader("empty link") + """
		<span class="close0r1">
			default URL<br />
			try <a href="presets">http://192.168.0.16:8080/presets</a><br />
			or  <a href="form">http://192.168.0.16:8080/form</a><br />			
		</span>
	</body>
</html>
		"""
		return outStr


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * the handler for quitting the server
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
class stopItAll:
	def GET(self):
		outStr = sendMyHeader("empty link") + """
		<span class="close0r0">
		stopping the server<br />
		try <a href="presets">http://192.168.0.16:8080/presets</a><br />
		or  <a href="form">http://192.168.0.16:8080/form</a><br />			
		</span>
		</span>
	</body>
</html>
		"""
		HTMLapp.stop()
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
			mainMenu<br />
			try <a href="presets">192.168.0.16:8080/presets</a><br />
			or  <a href="form">192.168.0.16:8080/form</a><br />			
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
			outStr += f"""</tr>
"""
			if int(thisRow[C.RID]) == int(C.DEFQUERYNUM):
				outStr += f"""<td class="close0r0">default</td>
"""
			else:
				outStr += f"""<td class="r1"><a href="setDefault/?QUERYNUM={thisRow[C.RID]}">
make default</a></td>
"""
			outStr += f"""
<td class="r{rowState}">
<a href="quakes?STARTRECNUM=0&QUERYNUM={thisRow[C.RID]}">{thisRow[C.QUERIESINTITLE]}</a>
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
		myInput = web.input(STARTRECNUM=0, QUERYNUM=C.DEFQUERYNUM)
		print(f"forwarding to {repr(myInput)}")
		web.seeother(f"""http://192.168.0.16:8080/quakes?STARTRECNUM={myInput[C.STARTRECNUM]}&QUERYNUM={myInput[C.QUERYNUM]}""")


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
class setDefault:
	def GET(self):
		DBLinks = DB.doOpen(C.SQLCONFIG)
		myInput = web.input(QUERYNUM=C.DEFQUERYNUM)
		newDefault = myInput[C.QUERYNUM]
		outStr = sendMyHeader("set default query number")
		SQLStr = f"""
select RID from queriesIn where RID = {newDefault};"""
		SQLRowDict = DB.getSqlOne(DBLinks, SQLStr)
		if SQLRowDict is None:
			outStr += f"""
<span class = "fp">that was a fail<br /></span>
</body>
</html>"""
			return outStr
		outStr += f"""
		<span class="close0r0"><br />
		setting {newDefault} as the new DEFAULTQUERYNUM and returning to presets<br />
</body>
</html>
"""
		C.DEFQUERYNUM = newDefault
		C.PUTDEFQRID()
		web.seeother(f"""http://192.168.0.16:8080/presets""")
		return outStr



if __name__ == "__main__":
	HTMLapp.run()
	print("we made it")
