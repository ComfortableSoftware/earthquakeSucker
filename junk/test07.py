#!/usr/bin/python


import os
import ijson as IJ
# from re import sub as SUB


from dataStuff import constants as C
from dataStuff import constants1 as C1
from dataStuff import webStuff as WEB
from dataStuff import timeDateStuff as TDS

usefulBit = f"""{TDS.nowStr(TDS.DT.now())}.useful.txt"""
moreUsefulBit = f"""{TDS.nowStr(TDS.DT.now())}.moreUseful.txt"""
usefulName = f"""{C.CACHEDIR(usefulBit)}"""
moreUsefulName = f"""{C.CACHEDIR(moreUsefulBit)}"""
usefulKeys = C1.USEFULPREFIX
myEventID = "zzzzqqqqwwww1111"


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
MYOFFSET = 1
QUERYSTR = F"""&limit=100&starttime=2019-01-01&endtime=2020-01-01&offset={MYOFFSET}"""
# thisURL = C.GEOJSONQUERY(QUERYSTR)
IDSTR = "us70009qa3"
# thisURL = C.GEOJSONDETAIL(IDSTR)
# thisURL = C.GEOJSONDETAILQUERY(IDSTR)
# thisURL = C.GEOJSONALLSMRY(C.DAY)
filenameBits = f"""test07.{TDS.nowStr(TDS.DT.now())}.json"""
thisFilename = f"""{C.CACHEDIR(filenameBits)}"""


itemList = []
OBJStack = []
fileEntry = C.GEOJSONFILEENTRYEMPTYSQL()


def getAFile(thisURL, thisFilename):
	print(f"""
	downloading file from {thisURL}
	""")
	TStatus = WEB.getAFile(thisURL, thisFilename, isJson=True)
	if TStatus is False:
		return False
	if not os.path.isfile(thisFilename):
		print(f"something is wrong with my filename/file/etc.{C.NEWLINE}|{thisFilename}|")
		exit(53)
	return True


def doAFile(thisFilename, myEventID):
	global itemList, OBJStack, fileEntry
	FDUseful = open(usefulName, "w")
	FDUseful.write(f"""USEFULPREFIX = {C.OBSSTR}{C.NEWLINE}""")
	FDUseful.flush()
	FDUseful.close()
	with open(f"""{C.CACHEDIR}ijsonOut.json""", "w") as FDOut:
		for prefix, the_type, value in IJ.parse(open(thisFilename)):
			if prefix.find(myEventID) > -1:
				prefix = prefix.replace(myEventID, "$EVENTID$")
			thisTuple = (prefix, the_type, value)
			# itemList.append(thisTuple)
			COMBO = f"""{prefix}::{the_type}"""
			if COMBO not in usefulKeys:
				FDOut.write(str(thisTuple))
				FDOut.flush()
				usefulKeys.append(prefix)
				FDUseful = open(usefulName, "ta")
				outStr = f"""{C.TABSTR}{C.DQTSTR}{COMBO}{C.DQTSTR},{C.NEWLINE}"""
				FDUseful.write(outStr)
				FDUseful.flush()
				FDUseful.close()
				FDMoreUseful = open(moreUsefulName, "ta")
				outStr = f"""({C.DQTSTR}{prefix}{C.DQTSTR}, {C.DQTSTR}{the_type}{C.DQTSTR}, C.TYPE, """
				outStr += f"""{C.DQTSTR}headerName{C.DQTSTR}, SQLDEFAULT, SCNDEFAULT,),{C.NEWLINE}"""
				FDMoreUseful.write(f"""{str(thisTuple)}{C.NEWLINE}""")
				FDMoreUseful.flush()
				FDMoreUseful.close()
	FDUseful = open(usefulName, "ta")
	outStr = f"""{C.CBSSTR}{C.NEWLINE}"""
	FDUseful.write(outStr)
	FDUseful.flush()
	FDUseful.close()


USEFULPREFIX = C1.USEFULPREFIX
for thisID in eventIDs:
	usefulBit = f"""{TDS.nowStr(TDS.DT.now())}.{thisID}.detail.txt"""
	moreUsefulBit = f"""{TDS.nowStr(TDS.DT.now())}.{thisID}.detailPlus.txt"""
	usefulName = f"""{C.CACHEDIR(usefulBit)}"""
	moreUsefulName = f"""{C.CACHEDIR(moreUsefulBit)}"""
	filenameBits = f"""detail.{thisID}.{TDS.nowStr(TDS.DT.now())}.json"""
	thisFilename = f"""{C.CACHEDIR(filenameBits)}"""
	thisURL = C.GEOJSONDETAIL(thisID)
	if getAFile(thisURL, thisFilename) is True:
		doAFile(thisFilename, thisID)
