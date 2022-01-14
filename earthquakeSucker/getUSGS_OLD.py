#!/usr/bin/python


import gc
from csv import reader
import os
from sys import argv


from dataStuff import constants as C
from dataStuff import webStuff as WEB
from dataStuff import timeDateStuff as TDS
from DBStuff import DBStuff as DB
from dataStuff import dataStuff as DS


gc.enable()
DBLINKS = DB.doOpen(C.SQLCONFIG)
myLocation = argv[0]

# thisUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_[hour day week month].csv"
# geojson in case that ever becomes reality https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson
thisUrl = C.CSVFEEDALL("hour")
# thisUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.csv"

# set csv file names appropriately so we can dev alongside use
if myLocation.find("DEV") > -1:
	thisFilename = "/home/will/.cache/earthquakesUSGS/" + TDS.nowStr() + ".DEV.USGS.csv"
else:
	thisFilename = "/home/will/.cache/earthquakesUSGS/" + TDS.nowStr() + ".USGS.csv"


if len(argv) == 1:
	if WEB.getAFile(thisUrl, thisFilename) is False:
		print(f"""file download was not successful""")
		exit(1)
else:
	thisFilename = argv[1]
	thisFilename = os.path.abspath(thisFilename)
	if not os.path.isfile(thisFilename):
		print(f"something is wrong with my filename\n|{thisFilename}|")
		exit(53)


with open(thisFilename) as inputFile:
	for lineNum, thisLine in enumerate(reader(inputFile)):
		if len(thisLine) != 22 or len(thisLine[0]) != 24:
			continue
		if C.DEBUGME:
			print(f"{DS.getDebugInfo(thisLine)} {repr(thisLine)}")
		thisDict = DB.fixThisLineToSQL(thisLine)
		if C.DEBUGME:
			print(f"{DS.getDebugInfo('thisDict')} {repr(thisDict):s}")
			print(f"{DS.getDebugInfo('propTimeZ')} {thisDict['propTimeZ']:s}")
		SQLStr = f"select * from `{C.DATATABLENAME}` where `eventID` = '{thisDict['eventID']}'"
		SQLRowDicts, SQLNumRows = DB.getSqlAll(DBLINKS, SQLStr)
		if not SQLRowDicts or not DB.checkForDupe(thisDict, SQLRowDicts):
			SQLResult = DB.insertDict(DBLINKS, C.DATATABLENAME, thisDict, C.MYFIELDTYPESDICT)
			if C.DEBUGME:
				print(f"{DS.getDebugInfo('SQLResult')} {repr(SQLResult)}")


os.remove(thisFilename)

