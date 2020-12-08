#!/usr/bin/python


import os
from sys import argv
import gc
import geojson as GJ
# from collections.abc import Iterable as IT


from dataStuff import constants as C
from dataStuff import webStuff as WEB
from dataStuff import timeDateStuff as TDS
from DBStuff import DBStuff as DB
from dataStuff import dataStuff as DS


gc.enable()
DBLINKS = DB.doOpen(C.SQLCONFIG)
# thisUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_[hour day week month].csv"
# geojson in case that ever becomes reality https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson
# https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_[hour day week month].geojson
# https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&eventid=nn00727575
# https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson
# myOffset = 10000
# thisUrl = """https://earthquake.usgs.gov/fdsnws/event/1/query.geojson?starttime=2020-04-21 00:00:00"""
# thisUrl += """&endtime=2020-05-21 23:59:59&minmagnitude=-1&eventtype=earthquake,acoustic noise,acoustic_noise"""
# thisUrl += """,anthropogenic_event,building collapse,chemical explosion,chemical_explosion,collapse"""
# thisUrl += """,eq,experimental explosion,explosion,ice quake,induced or triggered event,"""
# thisUrl += """industrial explosion,landslide,meteor,meteorite,mine collapse,mine_collapse"""
# thisUrl += """,mining explosion,mining_explosion,not reported,not_reported,nuclear explosion"""
# thisUrl += """,nuclear_explosion,other event,other_event,quarry,quarry blast,quarry_blast"""
# thisUrl += """,rock burst,Rock Slide,rockslide,rock_burst,snow_avalanche,sonic boom,sonicboom,sonic_boom"""
# thisUrl += f""",volcanic eruption,volcanic explosion&orderby=time&limit=10000&offset={myOffset}"""
thisUrl = """https://earthquake.usgs.gov/fdsnws/event/1/query.geojson?eventid=nn00730654"""
# thisUrl = f"""https://earthquake.usgs.gov/fdsnws/event/1/query.geojson?starttime=1900-04-21 00:00:00"""
# thisUrl += f"""&endtime=2020-05-21%2023:59:59&minmagnitude=-1&orderby=time&limit=10000&offset={myOffset}"""
# thisUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
myLocation = argv[0]

# set file names appropriately so we can dev alongside use
if myLocation.find("DEV") > -1:
	thisFilename = "/home/will/.cache/earthquakesUSGS/" + TDS.nowStr() + ".DEV.USGS.geojson"
	myTableName = f"{C.GEOJSONEVENTSTABLENAME}Test"
else:
	thisFilename = "/home/will/.cache/earthquakesUSGS/" + TDS.nowStr() + ".event.USGS.geojson"
	myTableName = f"{C.GEOJSONEVENTSTABLENAME}"

if len(argv) == 1:
	WEB.getAFile(thisUrl, thisFilename)
else:
	thisFilename = argv[1]
	thisFilename = os.path.abspath(thisFilename)
	if not os.path.isfile(thisFilename):
		print(f"something is wrong with my filename\n|{thisFilename}|")
		exit(53)

with open(thisFilename, "r") as FIn:
	GJLI = GJ.load(FIn)
	myFeatures = None
	myBoundingBox = None
	myMetadata = None
	if GJLI[C.typez] == "Feature":
		try:
			myFeatures = [GJLI]
		except KeyError:
			myFeatures = None
	elif GJLI[C.typez] == "FeatureCollection":
		try:
			myFeatures = GJLI["features"]
		except KeyError:
			myFeatures = None
		try:
			myMetadata = GJLI["metadata"]
		except KeyError:
			myMetadata = None
		try:
			myBoundingBox = GJLI["bbox"]
		except KeyError:
			myBoundingBox = None
	#try:
	#	myFeatures = GJLI["features"]
	#except KeyError:
	#	myFeatures = None
	myFileEntry = C.GEOJSONFILEENTRYEMPTYSQL()
	myFileEntry[C.fileType] = GJLI[C.typez]
	if myMetadata is not None:
		myFileEntry[C.fileMetaGeneratedTime] = TDS.TS2ISO(myMetadata[C.generated])
		myFileEntry[C.fileUrl] = myMetadata[C.url]
		myFileEntry[C.fileTitle] = myMetadata[C.title]
		myFileEntry[C.fileStatus] = myMetadata[C.status]
		myFileEntry[C.metaAPI] = myMetadata[C.api]
		myFileEntry[C.fileRecordCount] = myMetadata[C.count]
	if myBoundingBox is not None:
		myFileEntry[C.fileBBoxMinLon] = myBoundingBox[C.BBMINLON]
		myFileEntry[C.fileBBoxMinLat] = myBoundingBox[C.BBMINLAT]
		myFileEntry[C.fileBBoxMinDepth] = myBoundingBox[C.BBMINDEPTH]
		myFileEntry[C.fileBBoxMaxLon] = myBoundingBox[C.BBMAXLON]
		myFileEntry[C.fileBBoxMaxLat] = myBoundingBox[C.BBMAXLAT]
		myFileEntry[C.fileBBoxMaxDepth] = myBoundingBox[C.BBMAXDEPTH]
	SQLResult = DB.insertDict(DBLINKS, C.GEOJSONFILEENTRYTABLENAME, myFileEntry, C.MYFIELDTYPESDICT)
	if SQLResult is not None:
		print(f"""
something went wrong inserting a row
{str(myFileEntry)}
GJLI
{str(GJLI)}
SQLResult
{str(SQLResult)}
""")
		exit(1)
	myFileEntry[C.RID] = DB.getInsertID(DBLINKS)
	for thisFeature in myFeatures:
		myEventEntry = C.GEOGJSONEVENTSDEFAULTSQL()
		myProperties = thisFeature[C.properties]
		myGeometry = thisFeature[C.geometry]
		myEventEntry[C.featureType] = thisFeature[C.typez]
		myEventEntry[C.fileEntryRID] = myFileEntry[C.RID]
		myEventEntry[C.eventID] = thisFeature[C.idz]
		myEventEntry[C.geoLon] = myGeometry[C.coordinates][C.BBMINLON]
		myEventEntry[C.geoLat] = myGeometry[C.coordinates][C.BBMINLAT]
		myEventEntry[C.geoDepth] = myGeometry[C.coordinates][C.BBMINDEPTH]
		myEventEntry[C.geoType] = myGeometry[C.typez]
		myEventEntry[C.featureType] = thisFeature[C.typez]
		for sourceKey, destKey in C.GEOJSONFIELDNAMES.items():
			try:
				myEventEntry[destKey] = myProperties[sourceKey]
				if C.MYFIELDTYPESDICT[sourceKey] == "varchar":
					if not isinstance(myProperties[sourceKey], str):
						myEventEntry[destKey] = str(myProperties[sourceKey])
				if myEventEntry[destKey] is None:
					myEventEntry[destKey] = 0
				if C.MYFIELDTYPESDICT[destKey] == "datetime":
					myEventEntry[destKey] = TDS.TS2ISO(myEventEntry[destKey])
			except KeyError:
				continue
		SQLStr = f"""
select * from {C.GEOJSONEVENTSTABLENAME} where {C.eventID} = "{myEventEntry[C.eventID]}";"""
		SQLRows, numRows = DB.getSqlAll(DBLINKS, SQLStr)
		myToUpdate = False
		if numRows > 0:
			for testEvent in SQLRows:
				if testEvent[C.propUpdatedZ] == myEventEntry[C.propUpdatedZ]:
					myToUpdate = True
					break
		if myToUpdate is True:
			# we have it already, return to looking
			continue
		SQLResult = DB.insertDict(DBLINKS, myTableName, myEventEntry, C.MYFIELDTYPESDICT)


os.remove(thisFilename)


#

