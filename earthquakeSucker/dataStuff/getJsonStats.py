#!/usr/bin/python


import ijson as IJ
# from re import sub as SUB


import constants as C  # from dataStuff
import constants1 as C1  # from dataStuff
import timeDateStuff as TDS  # from dataStuff

usefulBit = f"""{TDS.nowStr(TDS.DT.now())}.useful.txt"""
moreUsefulBit = f"""{TDS.nowStr(TDS.DT.now())}.moreUseful.txt"""
usefulName = f"""{C.CACHEDIR(usefulBit)}"""
moreUsefulName = f"""{C.CACHEDIR(moreUsefulBit)}"""
usefulKeys = C1.USEFULPREFIX
fileEntry = C.GEOJSONFILEENTRYEMPTYSQL()


def doAFile(thisFilename, myEventID):
	global itemList, OBJStack, fileEntry, usefulName, moreUsefulName, usefulBit, moreUsefulBit
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
