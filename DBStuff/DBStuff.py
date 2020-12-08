

# from collections import deque as DQ
import gc
# import itertools
from datetime import datetime as DT
from mysql import connector as SQL


from dataStuff import timeDateStuff as TDS
from dataStuff import constants as C
from dataStuff import dataStuff as DS


gc.enable()


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * fix and add times, time=>propTimeZ+propTimeL+SINSETIMEZ+sinceTimeL
# ** updated=>propUpdatedZ+propUpdatedL+sinceUpdatedZ+sinceUpdatedL
# * only use on raw text input ever
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def DTfixThisLineToDisplay(lineIn):
	dictToRtn = {}
	for index, value in lineIn.items():
		if value != "":
			dictToRtn[index] = value
		if C.MYFIELDTYPESDICT[index] == "datetime":
			dictToRtn[index] = TDS.dateToStr(dictToRtn[index])
			myNow = TDS.nowStrSql(DT.now())
			mySinceName = f"""since{index[0].upper()}{index[1:]}"""
			if mySinceName.find("Z") >= 0:
				dictToRtn[mySinceName] = TDS.relDateDiff(myNow, dictToRtn[index])
	return dictToRtn


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * fix and add times,
# +SINSETIMEZ+sinceTimeLupdated=>propUpdatedZ+propUpdatedL+sinceUpdatedZ+sinceUpdatedL
# * only use on raw text input ever
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def fixThisLineToSQL(lineIn):
	dictToRtn = C.DATAFIELDDEFAULTSSQL()
	for index, value in enumerate(lineIn):
		myKey = C.DATAINNAMES[index]
		if value != "":
			dictToRtn[myKey] = value
		if C.MYFIELDTYPESDICT[myKey] == "datetime":
			# dictToRtn should be golden now, lets add things
			dictToRtn[myKey] = TDS.USGS2MysqlTime(dictToRtn[myKey])
	return dictToRtn


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * upgrade QUERIESINTABLE to QUERIESINGLOBAL
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def upgradeDBToGQI(queriesInRow, queriesInGlobal):
	for key, value in queriesInRow.items():
		if value != "":
			queriesInGlobal[key] = value
	return queriesInGlobal


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * upgrade QUERIESINTABLE to QUERIESINGLOBAL
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def upgradeDBToGQIMany(queriesInRows, queriesInGlobal):
	for Tindex in queriesInRows:
		for key, value in Tindex.items():
			queriesInGlobal[Tindex][key] = value
	return queriesInGlobal


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def fixSQLStr(strToChk):
	if strToChk[-1] != ";":
		strToChk += ";"
	if strToChk.find("SQL_CALC_FOUND_ROWS") == -1 and strToChk.casefold().find("select") > -1:
		strToChk = strToChk[0:7] + " SQL_CALC_FOUND_ROWS " + strToChk[7:]
	return strToChk


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def doOpen(thisConfig):
	TDBConn = SQL.connect(user=thisConfig["user"], host=thisConfig["host"], password=thisConfig["password"],
		database=thisConfig["database"])
	TDBCursor = TDBConn.cursor(buffered=True, dictionary=True)
	return {C.DBCONNECTION: TDBConn, C.DBCURSOR: TDBCursor, }


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def doClose(TDBLinks):
	TDBLinks[C.DBCONNECTION].close()


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def doBail(TDBLinks, exitText):
	print(f"\n{DS.getDebugInfo('exitText')}\n{exitText}")
	doClose(TDBLinks)
	quit(1)


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def doBlobSqlAll(TDBLinks, SQLStr, myBlob):
	SQLStr = fixSQLStr(SQLStr)
	TDBLinks[C.DBCURSOR].execute(SQLStr, myBlob)
	SQLRows = TDBLinks[C.DBCURSOR].fetchall()
	if len(SQLRows) > 0:
		SQLStr = """select found_rows() as FR;"""
		TDBLinks[C.DBCURSOR].execute(SQLStr)
		SQLNumRows = TDBLinks[C.DBCURSOR].fetchall()[0]["FR"]
	else:
		SQLRows = []
		SQLNumRows = 0
	return SQLRows, SQLNumRows


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def getSqlOne(TDBLinks, SQLStr):
	SQLStr = fixSQLStr(SQLStr)
	# TDBLinks[C.DBCURSOR].mysql_reset_connection()
	SQLResultReturned = TDBLinks[C.DBCURSOR].execute(SQLStr)
	if not SQLResultReturned:
		SQLRow = TDBLinks[C.DBCURSOR].fetchone()
	else:
		# TDBLinks[C.DBCONNECTION].commit()
		SQLRow = None

	return SQLRow


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def getSqlAll(TDBLinks, SQLStr):
	SQLStr = fixSQLStr(SQLStr)
	TDBLinks[C.DBCURSOR].execute(SQLStr)
	if SQLStr.casefold().find("select") > -1:
		SQLRows = TDBLinks[C.DBCURSOR].fetchall()
		if len(SQLRows) > 0:
			SQLStr = """select found_rows() as FR;"""
			TDBLinks[C.DBCURSOR].execute(SQLStr)
			TRow = TDBLinks[C.DBCURSOR].fetchall()
			SQLNumRows = TRow[0]["FR"]
		else:
			SQLRows = []
			SQLNumRows = 0
	else:
		SQLRows = []
		SQLNumRows = 0
	return SQLRows, SQLNumRows


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def dropTableIfExists(TDBLinks, tableName):
	SQLStr = 'drop table if exists `' + tableName + '`'
	SQLRow = getSqlOne(TDBLinks, SQLStr)
	return SQLRow


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# 
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeSelectStr(fieldList, SQLTable, SQLSelectField, SQLValue):
	SQLStr = 'select '

	for TField in fieldList:
		SQLStr += '`' + C.DATAFIELDNAMES[TField] + '`, '

	SQLStr = SQLStr[0:-2]
	SQLStr += 'from `' + SQLTable + '` where `' + C.DATAFIELDNAMES[SQLSelectField]
	SQLStr += '` is ' + C.SGLQT + SQLValue + C.SGLQT
	return SQLStr


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def dateToStr(rowToFix):
	for thisKey, thisType in rowToFix.items():
		if thisType == "datetime" and not isinstance(rowToFix[thisKey], str):
			rowToFix[thisKey] = TDS.dateToStr(rowToFix[thisKey])
	return rowToFix


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def tupleToDict(tupleToFix):
	TDict = C.DATAFIELDDEFAULTSSQL
	listToFix = list(tupleToFix)

	for index in range(len(listToFix)):
		thisName = C.DATAFIELDNAMES[index]
		TDict[thisName] = listToFix[index]
		if TDict[thisName] == "":
			TDict[thisName] = C.DATAFIELDDEFAULTS[thisName]
	if C.DEBUGME:
		print(f"{DS.getDebugInfo('TDict')} {repr(TDict)}")
	TDict["propTimeZ"] = TDS.toStr(TDict["propTimeZ"])
	TDict["propUpdatedZ"] = TDS.toStr(TDict["propUpdatedZ"])
	if C.DEBUGME:
		print(f"{DS.getDebugInfo('TDict')} {repr(TDict)}")
	return TDict


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def getSqlGetStart(TDBLinks, SQLStr):
	SQLStr = fixSQLStr(SQLStr)
	SQLResultReturned = TDBLinks[C.DBCURSOR].execute(SQLStr)
	return SQLResultReturned, TDBLinks


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def getNextSqlDict(TDBLinks):
	rowIn = TDBLinks[C.DBCURSOR].fetchone()
	return TDBLinks, rowIn


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def insertDict(TDBLinks, myTable, myDict, myTypes):
	# myDict = fixDictToAddUpd(myDict)
	for key in myDict:
		tempType = myTypes[key]
		if C.DEBUGME == 42:
			print(f"""{str(DS.getDebugInfo(""))}
key {key} tempType {tempType}
myDict[key] {repr(myDict[key])}
""")
		if tempType in ["datetime", "varchar"]:
			if isinstance(myDict[key], int):
				myDict[key] = TDS.TS2ISO(myDict[key])
			elif isinstance(myDict[key], str):
				myDict[key] = TDS.toStr(myDict[key])
			if myDict[key].find(C.DBLQT) == -1:
				myDict[key] = C.DBLQT + myDict[key] + C.DBLQT
			if tempType == "datetime" and myDict[key] == C.DFLTSTR:
				myDict[key] = TDS.nowStrSql(DT.now())
			if myDict[key].find(C.DBLQT) == -1:
				myDict[key] = C.DBLQT + myDict[key] + C.DBLQT
		if myDict[key] is None:
			myDict[key] = 0
		myDict[key] = str(myDict[key])
	dataStr = ', '.join(myDict.values())
	columns = ', '.join(myDict.keys())
	SQLStr = f"INSERT INTO {myTable} ({columns}) VALUES ({dataStr});"
	if C.DEBUGME == 42:
		print(f"{DS.getDebugInfo('SQLStr')} {SQLStr:s}")
	SQLResultReturned = TDBLinks[C.DBCURSOR].execute(SQLStr)
	if C.DEBUGME:
		print(f"{DS.getDebugInfo('SQLResultReturned')} {repr(SQLResultReturned)}")
	if not SQLResultReturned:
		SQLResultReturned = TDBLinks[C.DBCONNECTION].commit()
		if C.DEBUGME:
			print(f"{DS.getDebugInfo('SQLRESULT')} {repr(SQLResultReturned)}")
		if not SQLResultReturned:
			return None
		SQLRows = TDBLinks[C.DBCURSOR].fetchall()
		return SQLRows


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def updateDict(TDBLinks, myTable, myDict):
	# myDict = fixDictToAddUpd(myDict)
	SQLStr = f"UPDATE {myTable}\n\t SET "
	for key, value in myDict.items():
		SQLStr += f"{key} = {value},\n\t"
	SQLStr = SQLStr[:-3] + f"\n\twhere RID = {myDict['RID']}"
	if C.DEBUGME:
		print(f"{DS.getDebugInfo('SQLStr')} {SQLStr:s}")
	SQLResultReturned = TDBLinks[C.DBCURSOR].execute(SQLStr)
	if C.DEBUGME:
		print(f"{DS.getDebugInfo('SQLResultReturned')} {repr(SQLResultReturned)}")
	if not SQLResultReturned:
		SQLResultReturned = TDBLinks[C.DBCONNECTION].commit()
		if C.DEBUGME:
			print(f"{DS.getDebugInfo('SQLRESULT')} {repr(SQLResultReturned)}")
		if not SQLResultReturned:
			return None

		SQLRows = TDBLinks[C.DBCURSOR].fetchall()
		return SQLRows


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def tstMagnitude(SQLRowDict, lineToCheckAgainst):

	for thisRowDict in SQLRowDict:
		thisRowDict = dateToStr(thisRowDict)

		if thisRowDict["propMag"] == lineToCheckAgainst["propMag"]\
				and thisRowDict["propUpdatedZ"] == lineToCheckAgainst["propUpdatedZ"]:
			return True

	return False


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * check updated dates between a new SQL line and existing records
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def checkForDupe(thisDict, existingRecords):
	if not existingRecords:
		return False
	for thisRowDict in existingRecords:
		if TDS.toStr(thisRowDict[C.propUpdatedZ]) == TDS.toStr(thisDict[C.propUpdatedZ]):
			return True
	return False


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeTableStr(tableName, fieldNamesDict, fieldTypesDict):

	if len(fieldTypesDict) != len(fieldNamesDict):
		return None

	SQLStr = f"create table {tableName} ( \n"
	for index in fieldNamesDict.keys():
		SQLStr += f"{fieldNamesDict[index]} {fieldTypesDict[index]},\n"
	SQLStr = SQLStr[:-2] + ");"
	if C.DEBUGME:
		outStr = DS.getDebugInfo("SQLStr")
		print(f"{outStr}{repr(SQLStr)}")
	return SQLStr


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * sanemakeLimitStr
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def saneMakeSqlLimitStr(newStartNum):
	returnStr = f"limit {newStartNum}, {C.NUMROWSPERPG}"
	return returnStr


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * make an html table start
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeTableStart():
	return """
	<table>

	"""


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * make the class for regional highlighting
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeClass(rowIn, globalQueryStuff):
	rowStatus = globalQueryStuff[C.ROWNUM] & 1
	locRowNorth = float(rowIn[C.geoLat])
	locRowWest = float(rowIn[C.geoLon])

	loc0North = float(globalQueryStuff[C.REGION0NORTH])
	loc0West = float(globalQueryStuff[C.REGION0WEST])
	loc0South = float(globalQueryStuff[C.REGION0SOUTH])
	loc0East = float(globalQueryStuff[C.REGION0EAST])
	loc0KMFROM = float(globalQueryStuff[C.REGION0KMFROM])

	loc1North = float(globalQueryStuff[C.REGION1NORTH])
	loc1West = float(globalQueryStuff[C.REGION1WEST])
	loc1South = float(globalQueryStuff[C.REGION1SOUTH])
	loc1East = float(globalQueryStuff[C.REGION1EAST])
	loc1KMFROM = float(globalQueryStuff[C.REGION1KMFROM])

	loc2North = float(globalQueryStuff[C.REGION2NORTH])
	loc2West = float(globalQueryStuff[C.REGION2WEST])
	loc2South = float(globalQueryStuff[C.REGION2SOUTH])
	loc2East = float(globalQueryStuff[C.REGION2EAST])
	loc2KMFROM = float(globalQueryStuff[C.REGION2KMFROM])

	loc3North = float(globalQueryStuff[C.REGION3NORTH])
	loc3West = float(globalQueryStuff[C.REGION3WEST])
	loc3South = float(globalQueryStuff[C.REGION3SOUTH])
	loc3East = float(globalQueryStuff[C.REGION3EAST])
	loc3KMFROM = float(globalQueryStuff[C.REGION3KMFROM])

	if DS.vGreatCircleDistance(loc0North, loc0West, locRowNorth, locRowWest) <= loc0KMFROM:
		myClass = f"close0r{rowStatus}"
	elif (loc0North >= locRowNorth >= loc0South) and (loc0West <= locRowWest <= loc0East) and loc0KMFROM == 0:
		myClass = f"close0r{rowStatus}"

	elif DS.vGreatCircleDistance(loc1North, loc1West, locRowNorth, locRowWest) <= loc1KMFROM:
		myClass = f"close1r{rowStatus}"
	elif (loc1North >= locRowNorth >= loc1South) and (loc1West <= locRowWest <= loc1East) and loc1KMFROM == 0:
		myClass = f"close1r{rowStatus}"

	elif DS.vGreatCircleDistance(loc2North, loc2West, locRowNorth, locRowWest) <= loc2KMFROM:
		myClass = f"close2r{rowStatus}"
	elif (loc2North >= locRowNorth >= loc2South) and (loc2West <= locRowWest <= loc2East) and loc2KMFROM == 0:
		myClass = f"close2r{rowStatus}"

	elif DS.vGreatCircleDistance(loc3North, loc3West, locRowNorth, locRowWest) <= loc3KMFROM:
		myClass = f"close3r{rowStatus}"
	elif (loc3North >= locRowNorth >= loc3South) and (loc3West <= locRowWest <= loc3East) and loc3KMFROM == 0:
		myClass = f"close3r{rowStatus}"

	else:
		myClass = f"r{rowStatus}"

	return myClass


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * last hour, day, week, fortnight, month, quarter, half, year, 5y, 10y, 15y, 25y, 50y
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeDistance():
	outStr = f"""
	<tr>
		<td class="close3r0", colspan="121">
			<table>
				<tr>
					<td class="L00">M5+</td>
					<td class="L04">m4.5+</td>
					<td class="L08">m4.0+</td>
					<td class="L0C">m3.5+</td>
					<td class="L10">m3.0+</td>
					<td class="L14">m2.5+</td>
					<td class="L18">m2.0+</td>
					<td class="fp">&nbsp;</td>
					<td class="L00">100km-</td>
					<td class="L04">200km-</td>
					<td class="L08">300km-</td>
					<td class="L0C">400km-</td>
					<td class="L10">500km-</td>
					<td class="L14">600km-</td>
					<td class="L18">800km-</td>
					<td class="L1C">1000km-</td>
					<td class="fp">&nbsp;</td>
					<td class="L00">1hr-</td>
					<td class="L04">6hr-</td>
					<td class="L08">12hr-</td>
					<td class="L0C">day-</td>
					<td class="L10">week-</td>
					<td class="L14">fortnight-</td>
					<td class="L18">qtr-</td>
					<td class="L1C">hyr-</td>
					<td class="L1F">yr-</td>
				</tr>
			</table>
		</td>
	</tr>
"""
	return outStr


def makeHeaders(rowIn, PREVSTARTRECNUM, NEXTSTARTRECNUM, QUERYNUM, thisPgNum, ofPgsNum):
	if int(QUERYNUM) == int(C.DEFQUERYNUM):
		classStr = "close0r0"
	else:
		classStr = "r0"
	headerStr = f"""
	<tr>
		<td class="close0r0">{TDS.nowStrSql(DT.now())}</td>
		<td class="{classStr}"><a href="http://192.168.0.16:8080/quakes?STARTRECNUM=0&QUERYNUM={C.DEFQUERYNUM}">default
preset</a></td>
		<td class="L10"></td>
	</tr>
	<tr>
	<td><a href="http://192.168.0.16:8080/zwrd?STARTRECNUM={PREVSTARTRECNUM}&QUERYNUM={QUERYNUM}">prev
	pg</a>&nbsp;&nbsp;<a href="http://192.168.0.16:8080/zwrd?STARTRECNUM={NEXTSTARTRECNUM}&QUERYNUM={QUERYNUM}">next
	pg</a></td>
	<td><a href="http://192.168.0.16:8080/presets">rtn to caller</a></td>
	<td class="labels">labels</td>
	<td class="r0">r0</td>
	<td class="close3r0">{C.REGIONNAMESDICT[C.REGION3NAME]}r0</td>
	<td class="close2r0">{C.REGIONNAMESDICT[C.REGION2NAME]}r0</td>
	<td class="close1r0">{C.REGIONNAMESDICT[C.REGION1NAME]}r0</td>
	<td class="close0r0">{C.REGIONNAMESDICT[C.REGION0NAME]}r0</td>
	</tr>
	<tr>
	<td class="close0r0"><a href="stop">stop</a></td>
	<td>pgs {thisPgNum}/{ofPgsNum}</td>
	<td class="fp">fp</td>
	<td class="r1">r1</td>
	<td class="close3r1">{C.REGIONNAMESDICT[C.REGION3NAME]}r1</td>
	<td class="close2r1">{C.REGIONNAMESDICT[C.REGION2NAME]}r1</td>
	<td class="close1r1">{C.REGIONNAMESDICT[C.REGION1NAME]}r1</td>
	<td class="close0r1">{C.REGIONNAMESDICT[C.REGION0NAME]}r1</td>
	</tr>
	<tr>
	{makeDistance()}
	"""
	for key, value in rowIn.items():
		try:
			newName = C.HEADERNAMEDICT[key]
		except KeyError:
			newName = key
		headerStr += f"""
	<th>{newName}</th>
	"""
	headerStr += """
	</tr>
	<tr>
	"""
	return headerStr


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * make an html table row from a rowDict
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeTableRow(rowIn, globalQueryStuff, justTheHeaders):
	returnRowStr = ""
	thisRowNum = globalQueryStuff[C.ROWNUM]
	thisNumRows = globalQueryStuff[C.NUMROWS]
	thisHeaderState = thisRowNum % C.NUMLINESPERSEG
	THISPGNUM = globalQueryStuff[C.PGNUM]
	OFPGSNUM = globalQueryStuff[C.OFPGS]
	QUERYNUM = globalQueryStuff[C.QUERYNUM]
	NEXTSTARTRECNUM = int(globalQueryStuff[C.STARTRECNUM]) + int(C.NUMROWSPERPG)
	if NEXTSTARTRECNUM > globalQueryStuff[C.NUMROWS]:
		NEXTSTARTRECNUM = 0
	PREVSTARTRECNUM = int(globalQueryStuff[C.STARTRECNUM]) - int(C.NUMROWSPERPG)
	if PREVSTARTRECNUM < 0:
		PREVSTARTRECNUM = thisNumRows - (thisNumRows % 100)
	if thisHeaderState == 0 or justTheHeaders == 1:
		returnRowStr += makeHeaders(rowIn, PREVSTARTRECNUM, NEXTSTARTRECNUM, QUERYNUM, THISPGNUM, OFPGSNUM)
	if justTheHeaders != 1:
		myClass = makeClass(rowIn, globalQueryStuff)
		for key, value in rowIn.items():
			distStr = ""
			if key == C.sincePropTimeZ:
				wholeInt = int(DS.justTheNumbers(rowIn[C.sincePropTimeZ]))
				if wholeInt <= 10000:
					distStr = "L00"
				elif wholeInt <= 60000:
					distStr = "L04"
				elif wholeInt <= 120000:
					distStr = "L08"
				elif wholeInt <= 1000000:
					distStr = "L0C"
				elif wholeInt <= 7000000:
					distStr = "L10"
				elif wholeInt <= 14000000:
					distStr = "L14"
				elif wholeInt <= 100000000:
					distStr = "L18"
				elif wholeInt <= 300000000:
					distStr = "L1C"
				elif wholeInt <= 600000000:
					distStr = "L1F"
			elif key == C.propMag:
				tempMag = float(rowIn[C.propMag])
				if tempMag >= 5.0:
					distStr = "L00"
				elif tempMag >= 4.5:
					distStr = "L04"
				elif tempMag >= 4.0:
					distStr = "L08"
				elif tempMag >= 3.5:
					distStr = "L0C"
				elif tempMag >= 3.0:
					distStr = "L10"
				elif tempMag >= 2.5:
					distStr = "L14"
				elif tempMag >= 2.0:
					distStr = "L18"
			elif key == C.geoKMFROMHM:
				kmFromHM = float(rowIn[C.geoKMFROMHM])
				if kmFromHM <= 100.0:
					distStr = "L00"
				elif kmFromHM <= 200.0:
					distStr = "L04"
				elif kmFromHM <= 300.0:
					distStr = "L08"
				elif kmFromHM <= 400.0:
					distStr = "L0C"
				elif kmFromHM <= 500.0:
					distStr = "L10"
				elif kmFromHM <= 600.0:
					distStr = "L14"
				elif kmFromHM <= 800.0:
					distStr = "L18"
				elif kmFromHM <= 1000.0:
					distStr = "L1C"
			# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
			# * yyyymmddhhmmss 00000000000000-99999999999999
			# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
			returnRowStr += f"""
<td class="{myClass} {distStr}">{value}</td>
"""
		returnRowStr += "</tr>\n"
	return returnRowStr


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * returns the last inserted ID on the cursor
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def getInsertID(TDBLinks):
	return TDBLinks[C.DBCURSOR].lastrowid


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def deDupeEvents(TDBLinks):
	SQLStr = f"""
select {C.eventID}, count(*) as NUMRID from {C.DATATABLENAME}
group by {C.eventID}
having NUMRID > 1;"""
	myEventIDs, numDEQID = getSqlAll(TDBLinks, SQLStr)
	for thisEvent in myEventIDs:
		SQLStr = f"""
select {C.RID}, {C.propUpdatedZ} from `{C.DATATABLENAME}`
where `{C.eventID}` = {C.DBLQT}{thisEvent[C.eventID]}{C.DBLQT}
order by {C.propUpdatedZ} desc, {C.RID};"""
		suspectRows, numRows = getSqlAll(TDBLinks, SQLStr)
		propUpdatedZList = []
		RIDList = []
		for thisRow in suspectRows:
			propUpdatedZList.append(thisRow[C.propUpdatedZ])
			RIDList.append(thisRow[C.RID])
		while len(propUpdatedZList) > 1:
			if propUpdatedZList[0] == propUpdatedZList[1]:
				print(f"""deleting RID {RIDList[0]}""")
				SQLStr = f"""delete from {C.DATATABLENAME}
where {C.RID} = "{RIDList[0]}";"""
				getSqlAll(TDBLinks, SQLStr)
			propUpdatedZList.pop(0)
			RIDList.pop(0)
		# end while thisIndex
	# end for thisEventID
	SQLStr = f"""
select {C.eventID}, count(*) as NUMRID from {C.GEOJSONEVENTSTABLENAME}
group by {C.eventID}
having NUMRID > 1;"""
	myEventIDs, numDEQID = getSqlAll(TDBLinks, SQLStr)
	for thisEvent in myEventIDs:
		SQLStr = f"""
select {C.RID}, {C.propUpdatedZ} from `{C.DATATABLENAME}`
where `{C.eventID}` = {C.DBLQT}{thisEvent[C.eventID]}{C.DBLQT}
order by {C.propUpdatedZ} desc, {C.RID};"""
		suspectRows, numRows = getSqlAll(TDBLinks, SQLStr)
		propUpdatedZList = []
		RIDList = []
		for thisRow in suspectRows:
			propUpdatedZList.append(thisRow[C.propUpdatedZ])
			RIDList.append(thisRow[C.RID])
		while len(propUpdatedZList) > 1:
			if propUpdatedZList[0] == propUpdatedZList[1]:
				print(f"""deleting RID {RIDList[0]}""")

				SQLStr = f"""delete from {C.GEOJSONEVENTSTABLENAME}
where {C.RID} = "{RIDList[0]}";"""
				getSqlAll(TDBLinks, SQLStr)
			propUpdatedZList.pop(0)
			RIDList.pop(0)
			if len(propUpdatedZList) == 1:
				propUpdatedZList.pop(0)
		# end while thisIndex
	# end for thisEventID


def checkAPrefix(TDBLinks, prefixToCk):
	SQLStr = f"""select RID from `prefix`
where `{C.PFXprefixStr}` = "{prefixToCk}";"""
	SQLDict, numRecords = getSqlOne(TDBLinks, SQLStr)
	if numRecords == 0:
		return False
	else:
		return True


def checkUpdatePrefix(TDBLinks, prefixToCk):
	SQLStr = f"""select * from `{C.GEOJSONPREFIXTABLENAME}`
where `{C.PFXprefixStr}` = "{prefixToCk}";"""
	SQLDict = getSqlOne(TDBLinks, SQLStr)
	if SQLDict is None:
		return False
	else:
		SQLStr = f"""update {C.GEOJSONPREFIXTABLENAME} set {C.PFXlastSeen} = "{TDS.nowStrSql(TDS.DT.now())}";"""
		getSqlOne(TDBLinks, SQLStr)
		return SQLDict


def addAPrefix(TDBLinks, prefixIn, typeIn):
	SQLStr = f"""insert into {C.GEOJSONPREFIXTABLENAME}
({C.PFXprefixStr}, {C.PFXkeyType}, {C.PFXfirstSeen}, {C.PFXlastSeen})
values
("{prefixIn}", "{typeIn}", "{TDS.nowStrSql()}", "{TDS.nowStrSql()}");
"""
	SQLResult = getSqlOne(TDBLinks, SQLStr)
	if not SQLResult:
		return True
	else:
		return False


#

