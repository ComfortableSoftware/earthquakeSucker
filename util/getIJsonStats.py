#!/usr/bin/python


import ijson as IJ
from sys import argv
import getopt as GO
# from re import sub as SUB


from DBStuff import DBStuff as DB
from dataStuff import constants as C
from dataStuff import constants1 as C1
from dataStuff import dataStuff as DS
from dataStuff import timeDateStuff as TDS
from dataStuff import webStuff as WEB


usefulBit = f"""temp/{TDS.nowStr(TDS.DT.now())}.useful.txt"""
moreUsefulBit = f"""temp/{TDS.nowStr(TDS.DT.now())}.moreUseful.txt"""
usefulName = f"""{C.CACHEDIR(usefulBit)}"""
moreUsefulName = f"""{C.CACHEDIR(moreUsefulBit)}"""
fileEntry = C.GEOJSONFILEENTRYEMPTYSQL()


def writeTheConstants():
	return
	outSTR = ""
	fileName = f"""{TDS.nowStr(TDS.DT.now())}.Constants1.py"""
	FDOut = open(C.CACHEDIR(fileName), "w")
	outSTR += f"""
	USEFULPREFIX = {C.OBSSTR}
"""
	for thisPrefix in usefulKeys:
		outSTR += f"""{C.TABSTR}{C.DQTSTR}{thisPrefix}{C.DQTSTR},
"""
	outSTR += f"""{C.CBSSTR}


"""
	FDOut.write(outSTR)
	FDOut.flush()
	FDOut.close()


def doAFile(thisFilename, myEventID=""):
	global fileEntry, usefulName, moreUsefulName, usefulBit, moreUsefulBit
	DBLinks = DB.doOpen(C.SQLCONFIG)
	FDUseful = open(usefulName, "w")
	FDUseful.write(f"""USEFULPREFIX = {C.OBSSTR}{C.NEWLINE}""")
	FDUseful.flush()
	FDUseful.close()
	outName = f"""ijsonOut.{TDS.nowStr(TDS.DT.now())}.json"""
	with open(C.CACHEDIR(outName), "w") as FDOut:
		for prefix, the_type, value in IJ.parse(open(thisFilename)):
			if prefix == "" or prefix is None:
				continue
			if prefix.find(myEventID) > -1 and myEventID != "":
				prefix = prefix.replace(myEventID, "$EVENTID$")
			thisTuple = (prefix, the_type, value)
			# itemList.append(thisTuple)
			COMBO = f"""{prefix}::{the_type}"""
			FDOut.write(str(thisTuple))
			FDOut.flush()
			if DB.checkUpdatePrefix(DBLinks, prefix) is False:
				emptyPFXDict = C.PREFIXEMPTYDICT()
				emptyPFXDict[C.PFXlastSeen] = TDS.nowStrSql(TDS.DT.now())
				emptyPFXDict[C.PFXfirstSeen] = TDS.nowStrSql(TDS.DT.now())
				emptyPFXDict[C.PFXprefixStr] = prefix
				emptyPFXDict[C.PFXkeyType] = the_type
				DB.insertDict(DBLinks, C.GEOJSONPREFIXTABLENAME, emptyPFXDict, C.MYFIELDTYPESDICT)
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
	writeTheConstants()


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def doAFileOfEventIDs(filename):
	filename = DS.ABSPATH(filename)
	if not DS.PATH.isfile(filename):
		print(f"""
the filename {filename} is invalid
""")
		exit(1)
	with open(filename, "r") as FDIDIn:
		while True:
			thisID = FDIDIn.readline()
			if not thisID:
				quit(0)
			thisID = thisID[1:-2]
			thisURL = C.GEOJSONDETAIL(thisID)
			filename = f"""temp/ID{thisID}.DEETSL.{TDS.nowStr(TDS.DT.now())}.geojson"""
			thisFilename = f"""{C.CACHEDIR(filename)}"""
			thisResult = WEB.getAFile(thisURL, thisFilename, isJson=True)
			if thisResult is True:
				doAFile(thisFilename, thisID)


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def __main__():
	ARGV = argv[1:]
	# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
	# *	"-D": O_DETAILS,
	# *	"-Q": O_QUERYDETAILS,
	# *	"-d": O_ALLDAYSMRY,
	# *	"-f": O_FILE,
	# *	"-h": O_ALLHOURSMRY,
	# *	"-L": O_EVENTIDLIST,
	# *	"-m": O_ALLMONTHSMRY,
	# *	"-q": O_QUERY,
	# *	"-w": O_ALLWEEKSMRY,
	# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
	OPTS, ARGS = GO.getopt(ARGV, f"""D:Q:d:f:h:L:m:q:w:""")
	# print(f"""
	# opts {OPTS}
	# args {ARGS}
	# """)
	thisEventID = ""
	thisFilename = ""
	thisURL = ""
	thisFilePrefix = ""
	OPTSDICT = C1.OPTSTTDICT(OPTS)
	ARGSDICT = C1.ARGSTTDICT(ARGS)
	if OPTSDICT[C1.O_DETAILS] != "":
		thisEventID = OPTSDICT[C1.O_DETAILS]
		thisFilePrefix = "DEET"
		thisURL = C.GEOJSONDETAIL(thisEventID)
	elif OPTSDICT[C1.O_QUERYDETAILS] != "":
		thisEventID = OPTSDICT[C1.O_QUERYDETAILS]
		thisFilePrefix = "QDEET"
		thisURL = C.GEOJSONDETAILQUERY(thisEventID)
	elif OPTSDICT[C1.O_ALLDAYSMRY] != "":
		thisFilePrefix = "DAY"
		thisURL = C.GEOJSONALLSMRY("day")
	elif OPTSDICT[C1.O_FILE] != "":
		thisFilePrefix = "FILE"
		thisURL = ""
		thisFilename = OPTSDICT[C1.O_FILE]
	elif OPTSDICT[C1.O_ALLHOURSMRY] != "":
		thisFilePrefix = "HOUR"
		thisURL = C.GEOJSONALLSMRY("hour")
	elif OPTSDICT[C1.O_EVENTIDLIST] != "":
		doAFileOfEventIDs(OPTSDICT[C1.O_EVENTIDLIST])
		exit(0)
	elif OPTSDICT[C1.O_ALLMONTHSMRY] != "":
		thisFilePrefix = "MONTH"
		thisURL = C.GEOJSONALLSMRY("month")
	elif OPTSDICT[C1.O_QUERY] != "":
		thisFilePrefix = "QUERY"
		thisURL = C.GEOJSONQUERY(OPTSDICT[C1.O_QUERY])
	elif OPTSDICT[C1.O_ALLWEEKSMRY] != "":
		thisFilePrefix = "WEEK"
		thisURL = C.GEOJSONALLSMRY("week")
	else:
		print(f"""
Invalid opt set
OPTS {str(OPTS)}
ARGS {str(ARGS)}
argv {str(argv)}
""")
		exit(1)
	if thisURL != C.EMPTYSTR:
		thisPARM = f"""temp/ijsonST.{thisFilePrefix}.{TDS.nowStr(TDS.DT.now())}.json"""
		thisFilename = C.CACHEDIR(thisPARM)
		thisResult = WEB.getAFile(thisURL, thisFilename, isJson=True)
		if thisResult is False:
			print(f"""
failed to get the file {thisFilename}
from the URL {thisURL}

""")
			exit(1)
		if thisFilename != "":
			doAFile(thisFilename, myEventID=thisEventID)


if __name__ == "__main__":
	__main__()

#
