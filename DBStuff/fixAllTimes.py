import DBStuff as DB
from dataStuff import timeDateStuff as TDS
from dataStuff import constants as C


DBConnIn = DB.doOpen(C.SQLCONFIG)
DBConnOut = DB.doOpen(C.SQLCONFIG)
SQLStr = f"select * from `{C.DATATABLENAME}`"
SQLResult, DBConnIn = DB.getSqlGetStart(DBConnIn, SQLStr)
DBConnIn, thisRow = DB.getNextSqlDict(DBConnIn)

while thisRow:
	# thisRow = DB.tupleToDict(thisRow)
	thisTIMEZ = thisRow[C.DATAFIELDNAMES[C.propTimeZ]]
	thisTIMEL = thisRow[C.DATAFIELDNAMES[C.propTimeL]]

	if thisTIMEL == thisTIMEZ:
		thisTIMEL = TDS.mysql2LocalTime(thisTIMEZ)
		thisUPDATEDZ = thisRow[C.DATAFIELDNAMES[C.propUpdatedZ]]
		thisUPDATEDL = TDS.mysql2LocalTime(thisUPDATEDZ)
		thisRow[C.DATAFIELDNAMES[C.propTimeL]] = thisTIMEL
		thisRow[C.DATAFIELDNAMES[C.propUpdatedL]] = thisUPDATEDL
		thisRow = DB.fixDictToAddUpd(thisRow)
		SQLRows = DB.updateDict(DBConnOut, C.DATATABLENAME, thisRow)

	DBConnIn, thisRow = DB.getNextSqlDict(DBConnIn)

