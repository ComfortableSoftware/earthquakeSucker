#!/usr/bin/python


from csv import reader
import os
import getopt as GO
from sys import argv
import gc
import geojson as GJ
# from collections.abc import Iterable as IT


from dataStuff import constants as C
from dataStuff import dataStuff as DS
from dataStuff import webStuff as WEB
from dataStuff import timeDateStuff as TDS
from DBStuff import DBStuff as DB


gc.enable()


myOffset = 10000
# thisUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_[hour day week month].csv"
# geojson in case that ever becomes reality https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson
# thisUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv"
# thisUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_[hour day week month].[csv geojson]"
if myOffset == 0:
	thisUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
elif myOffset > 0:
	thisUrl = f"""https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&limit=10000&starttime=2020-03-01"""
	thisUrl += f"""&endtime=2020-04-01&offset={myOffset}"""
# elif myOffset == -1:
#   reserved for detail queries and then I can go out both directions for further expansion if needed
myLocation = argv[0]
ARGV = argv[1:]
OPTS, ARGS = GO.getopt(ARGV, f"""""")
# g:geoJsonHour i:eventID s:startDate e:endDate l:limit o:offset

destProgressBar = f"""24681246822468324684246852468624687246882468924680
"""
DBLINKS = DB.doOpen(C.SQLCONFIG)
# 4
listOfFileKeys = ['type', 'metadata', 'bbox', 'features']
# 4
listOf1stKeys = ['type', 'id', 'geometry', 'properties']
# 8
listOfMetaKeys = ['generated', 'url', 'title', 'status', 'api', 'count', 'limit', 'offset']
# 2
listOfGeoKeys = ['type', 'coordinates']
# 0
listOfFeatureKeys = []
# 26
listOfPropertyKeys = ['mag', 'place', 'time', 'updated', 'tz', 'url', 'detail', 'felt', 'cdi', 'mmi', 'alert',
                      'status', 'tsunami', 'sig', 'net', 'code', 'ids', 'sources', 'types', 'nst', 'dmin', 'rms',
                      'gap', 'magType', 'type', 'title']
# 0
listOfProductTypes = []
# 0
listOfProdTypes = []
# 0
listOfProdKeys = []
# 0
listOfProdPropKeys = []
# 0
listOfProdCntKeys = []

if myLocation.find("DEV") > -1:
	thisFilename = "/home/will/.cache/earthquakesUSGS/" + TDS.nowStr() + ".DEV.USGS.geojson"
	myTableName = f"{C.GEOJSONEVENTSTABLENAME}Test"
else:
	thisFilename = "/home/will/.cache/earthquakesUSGS/" + TDS.nowStr() + ".USGS.geojson"
	myTableName = f"{C.GEOJSONEVENTSTABLENAME}"

if len(argv) == 1:
	WEB.getAFile(thisUrl, thisFilename)
else:
	thisFilename = argv[1]
	thisFilename = os.path.abspath(thisFilename)


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def getAFile(thisUrl, thisFilename):
	print(f"""
downloading file from {thisUrl}
""")
	WEB.getAFile(thisUrl, thisFilename)
	if not os.path.isfile(thisFilename):
		print(f"something is wrong with my filename\n|{thisFilename}|")
		exit(53)


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * functions
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def addKeys(iterableToAdd, toWhichListName):
	global listOfBBoxKeys, listOfPropertyKeys, listOfGeoKeys, listOfFileKeys, listOfMetaKeys, listOf1stKeys, \
		listOfFeatureKeys
	toWhichList = []
	if toWhichListName == "listOfFileKeys":
		toWhichList = listOfFileKeys
	elif toWhichListName == "listOf1stKeys":
		toWhichList = listOf1stKeys
	elif toWhichListName == "listOfMetaKeys":
		toWhichList = listOfMetaKeys
	elif toWhichListName == "listOfGeoKeys":
		toWhichList = listOfGeoKeys
	elif toWhichListName == "listOfPropertyKeys":
		toWhichList = listOfPropertyKeys
	elif toWhichListName == "listOfFeatureKeys":
		toWhichList = listOfFeatureKeys
	for key in iterableToAdd:
		if key not in toWhichList:
			toWhichList.append(key)
	if toWhichListName == "listOfFileKeys":
		listOfFileKeys = toWhichList
	elif toWhichListName == "listOf1stKeys":
		listOf1stKeys = toWhichList
	elif toWhichListName == "listOfBBoxKeys":
		listOfBBoxKeys = toWhichList
	elif toWhichListName == "listOfMetaKeys":
		listOfMetaKeys = toWhichList
	elif toWhichListName == "listOfGeoKeys":
		listOfGeoKeys = toWhichList
	elif toWhichListName == "listOfPropertyKeys":
		listOfPropertyKeys = toWhichList
	elif toWhichListName == "listOfFeatureKeys":
		 listOfFeatureKeys = toWhichList


def getGeojson():
	thisRowNum = 0
	addedRows = 0
	# set file names appropriately so we can dev alongside use
	global listOfPropertyKeys, listOfGeoKeys, listOfFileKeys, listOfMetaKeys, listOf1stKeys
	global listOfFeatureKeys
	print(f"""
opening file""")
	with open(thisFilename, "r") as FIn:
		print(f"""
loading file""")
		GJLI = GJ.load(FIn)
		print(f"""
doing file level stats""")
		addKeys(GJLI, "listOfFileKeys")
		myFileEntry = C.GEOJSONFILEENTRYEMPTYSQL()
		myFileEntry[C.fileType] = GJLI[C.type_]
		if myFileEntry[C.fileType] == "FeatureCollection":
			try:
				myMetadata = GJLI[C.metadata]
				myFileEntry[C.metaGeneratedTime] = TDS.TS2ISO(myMetadata[C.generated])
				print(f"""records returned {GJLI["metadata"]["count"]}/{len(GJLI[C.features])}
	generated {myFileEntry[C.metaGeneratedTime]}""")
				addKeys(myMetadata, "listOfMetaKeys")
			except KeyError:
				myMetadata = None
				myFileEntry[C.metaGeneratedTime] = ""
			try:
				myFeatures = GJLI[C.features]
			except KeyError:
				myFeatures = None
			try:
				myBoundingBox = GJLI[C.bbox]
			except KeyError:
				myBoundingBox = None
		if myMetadata is not None:
			myFileEntry[C.metaGeneratedTime] = TDS.TS2ISO(myMetadata[C.generated])
			for srcKey, destKey in C.METADATAEMPTY().items():
				try:
					myFileEntry[destKey] = myMetadata[srcKey]
				except KeyError:
					myFileEntry[destKey] = destKey
		else:
			myMetadata = C.METADATAEMPTY()
			for srcKey, destKey in myMetadata.items():
				myFileEntry[destKey] = myMetadata[srcKey]
		if myBoundingBox is not None:
			TBBox = C.BBOXEMPTY()
			for srcKey, destKey in TBBox.items():
				try:
					myFileEntry[destKey] = myBoundingBox[srcKey]
				except KeyError:
					myFileEntry[destKey] = destKey
		SQLResult = DB.insertDict(DBLINKS, C.GEOJSONFILEENTRYTABLENAME, myFileEntry, C.MYFIELDTYPESDICT)
		if SQLResult is not None:
			print(f"""
	something went wrong inserting a file entry row
	{str(myFileEntry)}
	GJLI
	{str(GJLI)}
	SQLResult
	{str(SQLResult)}
	""")
			exit(1)
		myFileEntry[C.RID] = DB.getInsertID(DBLINKS)
		print(f"""
processing entries
{destProgressBar}""", end="")
		for thisFeature in myFeatures:
			addKeys(thisFeature, listOfFeatureKeys)
			myEventEntry = C.GEOGJSONEVENTSDEFAULTSQL()
			myProperties = thisFeature[C.properties]
			addKeys(myProperties, "listOfPropertyKeys")
			myGeometry = thisFeature[C.geometry]
			addKeys(myGeometry, "listOfGeoKeys")
			myEventEntry[C.featureType] = thisFeature[C.type_]
			myEventEntry[C.fileEntryRID] = myFileEntry[C.RID]
			myEventEntry[C.eventID] = thisFeature[C.id_]
			myEventEntry[C.geoLon] = myGeometry[C.coordinates][C.BBMINLON]
			myEventEntry[C.geoLat] = myGeometry[C.coordinates][C.BBMINLAT]
			myEventEntry[C.geoDepth] = myGeometry[C.coordinates][C.BBMINDEPTH]
			myEventEntry[C.geoType] = myGeometry[C.type_]
			myEventEntry[C.featureType] = thisFeature[C.type_]
			for sourceKey, destKey in C.GEOJSONFIELDNAMES.items():
				myEventEntry[destKey] = myProperties[sourceKey]
				if C.MYFIELDTYPESDICT[sourceKey] == "varchar":
					if not isinstance(myProperties[sourceKey], str):
						myEventEntry[destKey] = str(myProperties[sourceKey])
				if myEventEntry[destKey] is None:
					myEventEntry[destKey] = 0
				if C.MYFIELDTYPESDICT[destKey] == "datetime":
					myEventEntry[destKey] = TDS.TS2ISO(myEventEntry[destKey])
			thisRowNum += 1
			if (thisRowNum % 200) == 0:
				print(".", end="", flush=True)
			SQLStr = f"""select * from {C.GEOJSONEVENTSTABLENAME} where {C.eventID} = "{myEventEntry[C.eventID]}";"""
			SQLRows, numRows = DB.getSqlAll(DBLINKS, SQLStr)
			myToUpdate = False
			if numRows > 0:
				for testEvent in SQLRows:
					returnedUpdate = TDS.toStr(testEvent[C.propUpdatedZ])
					entryDate = TDS.toStr(myEventEntry[C.propUpdatedZ])
					if returnedUpdate == entryDate:
						myToUpdate = True
						break
			if myToUpdate is True:
				# we have it already, return to looking
				continue
			SQLResult = DB.insertDict(DBLINKS, myTableName, myEventEntry, C.MYFIELDTYPESDICT)
			if SQLResult is None:
				addedRows += 1
		# end of for * in myFeatures
	# end of with geojson file
	os.remove(thisFilename)
	print(f"""
listOfFileKeys {len(listOfFileKeys)} {str(listOfFileKeys)}
listOf1stKeys {len(listOf1stKeys)} {str(listOf1stKeys)}
listOfMetaKeys {len(listOfMetaKeys)} {str(listOfMetaKeys)}
listOfGeoKeys {len(listOfGeoKeys)} {str(listOfGeoKeys)}
listOfFeatureKeys {len(listOfFeatureKeys)} {str(listOfFeatureKeys)}
listOfPropertyKeys {len(listOfPropertyKeys)} {str(listOfPropertyKeys)}
rows added {addedRows}
""")

def getCSV():
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


if __name__ == "__main__":
	__main__()

#

