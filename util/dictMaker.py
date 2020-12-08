

OBSTR = "{"
CBSTR = "}"
DQTSTR = '"'
definesStr = ""
MYDEFAULTSDICTSCNStr = ""
MYDEFAULTSDICTSQLStr = ""
MYFIELDTYPESDICTStr = ""
HEADERNAMEDICTStr = ""
NUMERICFILLERDICTStr = ""
NUMERICFILLERSStr = ""

FDOut = open("/wsource/python/earthquakeSuckerDEV/dataStuff/tinsert.py", "w")

# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# add/repair all tables prefix
# add a CMD to show calculated fields, don't set the defaults to anything except ""*
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
allTheList = [
	("AFFECTEDROWS", "DFLTINT", "DFLTINT", "INT", "AFFROWS"),
	("api", "DFLTSTR", "DFLTstr", "VARCHAR", "API",),
	("BBMAXDEPTH#5#",),
	("BBMAXLAT#4#",),
	("BBMAXLON#3#",),
	("BBMINDEPTH#2#",),
	("BBMINLAT#1#",),
	("BBMINLON#0#",),
	("bbox", "QTEMPTYDICT", "EMPTYDICT", "DICT", "BBOX",),
	("BBoxMaxDepth", "DFLTDEC", "DFLTDEC", "DECIMAL", "BBOXDN",),
	("BBoxMaxLat", "DFLTDEC", "DFLTDEC", "DECIMAL", "BBOXNTH",),
	("BBoxMaxLon", "DFLTDEC", "DFLTDEC", "DECIMAL", "BBOXWST",),
	("BBoxMinDepth", "DFLTDEC", "DFLTDEC", "DECIMAL", "BBOXUP",),
	("BBoxMinLat", "DFLTDEC", "DFLTDEC", "DECIMAL", "BBOXSTH",),
	("BBoxMinLon", "DFLTDEC", "DFLTDEC", "DECIMAL", "BBOXEST",),
	("CEQID", "DFLTINT", "DFLTINT", "INT", "CEQID",),
	("CKMFROM", "DFLTDEC", "DFLTDEC", "DECIMAL", "CKMFROM",),
	("coordinates", "QTEMPTYLIST", "EMPTYLIST", "LIST", "COORDINATES",),
	("count", "DFLTINT", "DFLTINT", "INT", "COUNT",),
	("CRID", "DFLTINT", "DFLTINT", "INT", "CRID",),
	("DEFAULTSCN#2#",),
	("DEFAULTSQL#1#",),
	("DBCONNECTION#0#",),
	("DBCURSOR#1#",),
	("detail", "DFLTSTR", "DFLTstr", "VARCHAR", "DETAIL URL",),
	("detailRID", "DFLTINT", "DFLTINT", "INT", "DRID",),
	("eventID", "DFLTSTR", "DFLTstr", "VARCHAR", "EQID",),
	("features", "QTEMPTYDICT", "QTEMPTYDICT", "dict", "FEATURES",),
	("featureType", "DFLTSTR", "DFLTstr", "VARCHAR", "FEATURE TYPE",),
	("FILEENTRY", "QTEMPTYDICT", "EMPTYDICT", "dict", "FILEENTRY",),
	("fileEntryRID", "DFLTINT", "DFLTINT", "INT", "FERID",),
	("fileType", "DFLTSTR", "DFLTstr", "VARCHAR", "FILE TYPE",),
	("generated", "DFLTSTR", "DFLTstr", "DATETIME", "timestamp",),
	("geoDepth", "DFLTDEC", "DFLTDEC", "DECIMAL", "DEPTH",),
	("geoKMFrom", "DFLTDEC", "DFLTDEC", "DECIMAL", "KM2GO",),
	("geoKMFROMHM", "DFLTDEC", "DFLTDEC", "DECIMAL", "KM2HM",),
	("geoLat", "DFLTDEC", "DFLTDEC", "DECIMAL", "LAT",),
	("geoLon", "DFLTDEC", "DFLTDEC", "DECIMAL", "LON",),
	("geometry", "QTEMPTYDICT", "EMPTYDICT", "dict", "geo",),
	("geoType", "DFLTSTR", "DFLTstr", "VARCHAR", "GEO TYPE",),
	("HEADER#4#",),
	("id_", "DFLTSTR", "DFLTstr", "VARCHAR", "ID",),
	("IJSONPREFIX#0#", "DFLTINT", "DFLTINT", "INT", "",),
	("IJSONTYPE#1#", "DFLTINT", "DFLTINT", "INT", "",),
	("IJSONVALUE#2#", "DFLTINT", "DFLTINT", "INT", "",),
	("ISLOADED", "DFLTINT", "DFLTINT", "INT", "LOADED",),
	("limit", "DFLTINT", "DFLTINT", "INT", "LIMIT",),
	("metaAPI", "DFLTSTR", "DFLTstr", "VARCHAR", "API",),
	("metadata", "QTEMPTYDICT", "EMPTYDICT", "dict", "META",),
	("metaFileRID", "DFLTINT", "DFLTINT", "INT", "METARID",),
	("metaFileStatus", "DFLTINT", "DFLTINT", "INT", "FSTAT",),
	("metaFileTitle", "DFLTSTR", "DFLTstr", "VARCHAR", "METATITLE",),
	("metaGeneratedTime", "DFLTSTR", "DFLTstr", "DATETIME", "TIMESTAMP",),
	("metaLimit", "DFLTINT", "DFLTINT", "INT", "LIMIT",),
	("metaOffset", "DFLTINT", "DFLTINT", "INT", "OFFSET",),
	("metaRecordCount", "DFLTINT", "DFLTINT", "INT", "CMETARID",),
	("metaURL", "DFLTSTR", "DFLTstr", "VARCHAR", "META URL",),
	("NAME#0#",),
	("NUMROWS", "DFLTINT", "DFLTINT", "INT", "NUMROWS",),
	("offset", "DFLTINT", "DFLTINT", "INT", "OFFSET",),
	("OFPGS", "DFLTINT", "DFLTINT", "INT", "OF PGS",),
	("parmEndTime#0#",),
	("parmLimit#1#",),
	("parmOffset#2#",),
	("parmStartTime#3#",),
	("parmUrl01#4#",),
	("parmUrl02#5#",),
	("parmUrl03#6#",),
	("parmUrl04#7#",),
	("parmUrl05#8#",),
	("PFX_", "prefix table",),
	("PFXDBTable", "DFLTSTR", "DFLTstr", "VARCHAR", "DBTABLE",),
	("PFXdescription", "DFLTSTR", "DFLTstr", "VARCHAR", "DESCR",),
	("PFXfieldNameL", "DFLTSTR", "DFLTstr", "VARCHAR", "FIELDNML",),
	("PFXfieldNameZ", "DFLTSTR", "DFLTstr", "VARCHAR", "FIELDNMZ",),
	("PFXfirstSeen", "DFLTDT", "DFLTDT", "DATETIME", "1ST SEEN",),
	("PFXkeyType", "DFLTSTR", "DFLTstr", "VARCHAR", "KEYTYPE",),
	("PFXlastSeen", "DFLTDT", "DFLTDT", "DATETIME", "LAST SEEN",),
	# ("PFXmyHashKey", "None", "None", "VARCHAR", "MY HASH KEY",),
	# ("PFXprefixKey", "None", "None", "VARCHAR", "PREFIXKEY",),
	("PFXprefixStr", "DFLTSTR", "DFLTstr", "VARCHAR", "PREFIXSTR",),
	("PFXyieldThis", "DFLTSTR", "DFLTstr", "VARCHAR", "YIELDS",),
	("PGNUM", "DFLTINT", "DFLTINT", "INT", "PG NM",),
	("PPropKey", "DFLTSTR", "DFLTstr", "VARCHAR", "PPKEY",),
	("prefix", "DFLTSTR", "DFLTstr", "VARCHAR", "IJPREFIX",),
	("prodCode", "DFLTSTR", "DFLTstr", "VARCHAR", "PRODCODE",),
	("prodID", "DFLTSTR", "DFLTstr", "VARCHAR", "PRODID",),
	("prodProps", "QTEMPTYDICT", "EMPTYDICT", "dict", "PRODPROPS",),
	("prodSource", "DFLTSTR", "DFLTstr", "VARCHAR", "PRODSRC",),
	("prodStatus", "DFLTSTR", "DFLTstr", "VARCHAR", "PRODSTAT",),
	("prodType", "DFLTSTR", "DFLTstr", "VARCHAR", "PRODTYPE",),
	("productType", "DFLTSTR", "DFLTstr", "VARCHAR", "PRODUCTTYPE",),
	("prodUpdatedZ", "DFLTDT", "DFLTDT", "DATETIME", "PRODUPDATEDZ",),
	("propAlert", "DFLTSTR", "DFLTstr", "VARCHAR", "ALERT",),
	("propCode", "DFLTSTR", "DFLTstr", "VARCHAR", "CODE",),
	("propCompDYFIIndex", "DFLTDEC", "DFLTDEC", "DECIMAL", "DYFI",),
	("propDegMinToStation", "DFLTDEC", "DFLTDEC", "DECIMAL", "DM2S",),
	("propDepthErr", "DFLTDEC", "DFLTDEC", "DECIMAL", "DNERR",),
	("propDetailUrl", "DFLTSTR", "DFLTstr", "VARCHAR", "DETAIL URL",),
	("properties", "QTEMPTYDICT", "EMPTYDICT", "dict", "PROPS",),
	("propEventType", "DFLTSTR", "DFLTstr", "VARCHAR", "EVENT TYPE",),
	("propFelt", "DFLTINT", "DFLTINT", "INT", "FELT",),
	("propHorizontalErr", "DFLTDEC", "DFLTDEC", "DECIMAL", "HORZERR",),
	("propIDsUsed", "DFLTSTR", "DFLTstr", "VARCHAR", "IDs",),
	("propLocationSrc", "DFLTSTR", "DFLTstr", "VARCHAR", "LCNSRC",),
	("propMag", "DFLTDEC", "DFLTDEC", "DECIMAL", "MAG",),
	("propMagErr", "DFLTDEC", "DFLTDEC", "DECIMAL", "MAGERR",),
	("propMagNST", "DFLTINT", "DFLTINT", "INT", "MAGNST",),
	("propMagSrc", "DFLTSTR", "DFLTstr", "VARCHAR", "MAGSRC",),
	("propMagType", "DFLTSTR", "DFLTstr", "VARCHAR", "MAGTYPE",),
	("propMaxAzmGap", "DFLTDEC", "DFLTDEC", "DECIMAL", "GAP",),
	("propMaxMeasuredIntensity", "DFLTDEC", "DFLTDEC", "DECIMAL", "MMI",),
	("propNetwork", "DFLTSTR", "DFLTstr", "VARCHAR", "NET",),
	("propNumStations", "DFLTINT", "DFLTINT", "INT", "NST",),
	("propPFDWT", "DFLTINT", "DFLTINT", "INT", "PFD WT",),
	("propPlace", "DFLTSTR", "DFLTstr", "VARCHAR", "PLACE",),
	("propProducts", "QTEMPTYDICT", "EMPTYDICT", "dict", "PRODS",),
	("propProductTypesUsed", "DFLTSTR", "DFLTstr", "VARCHAR", "PRODUCTS",),
	("propRMS", "DFLTDEC", "DFLTDEC", "DECIMAL", "RMS",),
	("propSignificanceIndex", "DFLTINT", "DFLTINT", "INT", "SIG",),
	("propSourcesUsed", "DFLTSTR", "DFLTstr", "VARCHAR", "SRCS",),
	("propStatus", "DFLTSTR", "DFLTstr", "VARCHAR", "STAT",),
	("propTimeL", "DFLTSTR", "DFLTstr", "DATETIME", "TIMEL",),
	("propTimeZ", "DFLTSTR", "DFLTstr", "DATETIME", "TIMEZ",),
	("propTitle", "DFLTSTR", "DFLTstr", "VARCHAR", "TITLE",),
	("propTsunami", "DFLTINT", "DFLTINT", "INT", "TSNMI",),
	("propTZLM", "DFLTINT", "DFLTINT", "INT", "TZM",),
	("propUpdatedL", "DFLTSTR", "DFLTstr", "DATETIME", "UPDL",),
	("propUpdatedZ", "DFLTSTR", "DFLTstr", "DATETIME", "UPDZ",),
	("propUrl", "DFLTSTR", "DFLTstr", "VARCHAR", "URL",),
	("QUERIESINRETURNTO", "DFLTSTR", "DFLTstr", "VARCHAR", "RTS",),
	("QUERIESINTITLE", "DFLTSTR", "DFLTstr", "VARCHAR", "QRYTITL",),
	("QUERYEMPTY#0#",),
	("QUERYFROMPRESET#1#",),
	("QUERYLOADED#-1#",),
	("QUERYNUM", "DFLTINT", "DFLTINT", "INT", "QRID",),
	("REGION0DESCRIPTION", "DFLTSTR", "DFLTstr", "VARCHAR", "region 0 desc",),
	("REGION0EAST", "DFLTDEC", "DFLTDEC", "DECIMAL", "R0EST",),
	("REGION0KMFROM", "DFLTDEC", "DFLTDEC", "DECIMAL", "R0KMFM",),
	("REGION0NAME", "DFLTSTR", "DFLTstr", "VARCHAR", "R0NM",),
	("REGION0NORTH", "DFLTDEC", "DFLTDEC", "DECIMAL", "R0NTH",),
	("REGION0SOUTH", "DFLTDEC", "DFLTDEC", "DECIMAL", "R0STH",),
	("REGION0WEST", "DFLTDEC", "DFLTDEC", "DECIMAL", "R0WST",),
	("REGION1DESCRIPTION", "DFLTSTR", "DFLTstr", "VARCHAR", "region 1 desc",),
	("REGION1EAST", "DFLTDEC", "DFLTDEC", "DECIMAL", "R1EST",),
	("REGION1KMFROM", "DFLTDEC", "DFLTDEC", "DECIMAL", "R1KMFMHM",),
	("REGION1NAME", "DFLTSTR", "DFLTstr", "VARCHAR", "R1NM",),
	("REGION1NORTH", "DFLTDEC", "DFLTDEC", "DECIMAL", "R1NTH",),
	("REGION1SOUTH", "DFLTDEC", "DFLTDEC", "DECIMAL", "R1STH",),
	("REGION1WEST", "DFLTDEC", "DFLTDEC", "DECIMAL", "R1WST",),
	("REGION2DESCRIPTION", "DFLTSTR", "DFLTstr", "VARCHAR", "region 2 desc",),
	("REGION2EAST", "DFLTDEC", "DFLTDEC", "DECIMAL", "R2EST",),
	("REGION2KMFROM", "DFLTDEC", "DFLTDEC", "DECIMAL", "R2KMFMHM",),
	("REGION2NAME", "DFLTSTR", "DFLTstr", "VARCHAR", "R2NM",),
	("REGION2NORTH", "DFLTDEC", "DFLTDEC", "DECIMAL", "R2NTH",),
	("REGION2SOUTH", "DFLTDEC", "DFLTDEC", "DECIMAL", "R2STH",),
	("REGION2WEST", "DFLTDEC", "DFLTDEC", "DECIMAL", "R2WST",),
	("REGION3DESCRIPTION", "DFLTSTR", "DFLTstr", "VARCHAR", "region 3 desc",),
	("REGION3EAST", "DFLTDEC", "DFLTDEC", "DECIMAL", "R3EST",),
	("REGION3KMFROM", "DFLTDEC", "DFLTDEC", "DECIMAL", "R3KMFMHM",),
	("REGION3NAME", "DFLTSTR", "DFLTstr", "VARCHAR", "R3NM",),
	("REGION3NORTH", "DFLTDEC", "DFLTDEC", "DECIMAL", "R3NTH",),
	("REGION3SOUTH", "DFLTDEC", "DFLTDEC", "DECIMAL", "R3STH",),
	("REGION3WEST", "DFLTDEC", "DFLTDEC", "DECIMAL", "R3WST",),
	("RID", "DFLTINT", "DFLTINT", "INT", "RID",),
	("ROWNUM", "DFLTINT", "DFLTINT", "INT", "ROW#",),
	("ROWSDICT", "EMPTYDICT", "EMPTYDICT", "DICT", "ROWSDICT"),
	("sincePropTimeL", "DFLTSTR", "DFLTstr", "DATETIME", "SINCELL",),
	("sincePropTimeZ", "DFLTSTR", "DFLTstr", "DATETIME", "SINCEZ",),
	("sincePropUpdatedL", "DFLTSTR", "DFLTstr", "DATETIME", "SINCEUPDL",),
	("sincePropUpdatedZ", "DFLTSTR", "DFLTstr", "DATETIME", "SINCEUPDZ",),
	("SQLGROUPBY", "DFLTSTR", "DFLTstr", "VARCHAR", "GRPBY",),
	("SQLHAVING", "DFLTSTR", "DFLTstr", "VARCHAR", "HAVE",),
	("SQLLIMIT", "DFLTSTR", "DFLTstr", "VARCHAR", "LTD",),
	("SQLORDERBY", "DFLTSTR", "DFLTstr", "VARCHAR", "SORT",),
	("SQLSELECT", "DFLTSTR", "DFLTstr", "VARCHAR", "SLCT",),
	("SQLWHERE", "DFLTSTR", "DFLTstr", "VARCHAR", "WHERE",),
	("STARTRECNUM", "DFLTINT", "DFLTINT", "INT", "STRTNUM",),
	("status", "DFLTSTR", "DFLTstr", "VARCHAR", "STAT",),
	("title", "DFLTSTR", "DFLTstr", "VARCHAR", "TITLE",),
	("TYPE#3#",),
	("type_", "DFLTSTR", "DFLTstr", "VARCHAR", "TYPE",),
	("url", "DFLTSTR", "DFLTstr", "VARCHAR", "URL",),
	('"alert"', "DFLTSTR", "DFLTstr", "VARCHAR", "",),
	('"cdi"', "DFLTINT", "DFLTINT", "INT", "",),
	('"code"', "DFLTSTR", "DFLTstr", "VARCHAR", "",),
	('"detail"', "DFLTSTR", "DFLTstr", "VARCHAR", "",),
	('"dmin"', "DFLTDEC", "DFLTDEC", "DECIMAL", "",),
	('"felt"', "DFLTINT", "DFLTINT", "INT", "",),
	('"gap"', "DFLTDEC", "DFLTDEC", "DECIMAL", "",),
	('"ids"', "DFLTSTR", "DFLTstr", "VARCHAR", "",),
	('"mag"', "DFLTDEC", "DFLTDEC", "DECIMAL", "",),
	('"magType"', "DFLTSTR", "DFLTstr", "VARCHAR", "",),
	('"mmi"', "DFLTDEC", "DFLTDEC", "DECIMAL", "",),
	('"net"', "DFLTSTR", "DFLTstr", "VARCHAR", "",),
	('"nst"', "DFLTINT", "DFLTINT", "INT", "",),
	('"place"', "DFLTSTR", "DFLTstr", "VARCHAR", "",),
	('"propNumStations"', "DFLTINT", "DFLTINT", "INT", "",),
	('"rms"', "DFLTDEC", "DFLTDEC", "DECIMAL", "",),
	('"sig"', "DFLTINT", "DFLTINT", "INT", "",),
	('"sources"', "DFLTSTR", "DFLTstr", "VARCHAR", "",),
	('"status"', "DFLTSTR", "DFLTstr", "VARCHAR", "",),
	('"time"', "DFLTDT", "DFLTDT", "INT", "",),
	('"title"', "DFLTSTR", "DFLTstr", "VARCHAR", "",),
	('"tsunami"', "DFLTINT", "DFLTINT", "INT", "",),
	('"type"', "DFLTSTR", "DFLTstr", "VARCHAR", "",),
	('"types"', "DFLTSTR", "DFLTstr", "VARCHAR", "",),
	('"type_"', "DFLTSTR", "DFLTstr", "VARCHAR", "",),
	('"tz"', "DFLTINT", "DFLTINT", "INT", "",),
	('"updated"', "DFLTINT", "DFLTINT", "INT", "",),
	('"url"', "DFLTSTR", "DFLTstr", "VARCHAR", "",),
]

MYFIELDTYPESDICTStr += f"""MYFIELDTYPESDICT = {OBSTR}
"""
MYDEFAULTSDICTSQLStr += f"""MYDEFAULTSDICTSQL = {OBSTR}
"""
MYDEFAULTSDICTSCNStr += f"""MYDEFAULTSDICTSCN = {OBSTR}
"""
HEADERNAMEDICTStr += f"""HEADERNAMEDICT = {OBSTR}
"""
NUMERICFILLERDICTStr += f"""NUMERICFILLERDICT = {OBSTR}
"""

for thisEntry in allTheList:
	myName = f"""{thisEntry[0]}"""
	if myName.find('"') == -1:
		myCmd = myName[-1]
		if myCmd == "_":
			myNewName = myName[0:-1]
			definesStr += f"""{myName} = {DQTSTR}{myNewName}{DQTSTR}
"""
			continue
		elif myCmd == "#":
			TList = myName.split("#")
			myName = TList[0]
			definesStr += f"""{TList[0]} = {DQTSTR}{TList[0]}{DQTSTR}
"""
			NUMERICFILLERDICTStr += f"""{TList[0]}: {TList[1]},
"""
			NUMERICFILLERSStr += f"""{TList[0]} = {TList[1]}
"""
			continue
		else:
			definesStr += f"""{myName} = {DQTSTR}{myName}{DQTSTR}
"""
	MYFIELDTYPESDICTStr += f"""{myName}: {thisEntry[3]},
"""
	MYDEFAULTSDICTSCNStr += f"""{myName}: {thisEntry[2]},
"""
	MYDEFAULTSDICTSQLStr += f"""{myName}: {thisEntry[1]},
"""
	HEADERNAMEDICTStr += f"""{myName}: {DQTSTR}{thisEntry[4]}{DQTSTR},
"""


definesStr += f"""
"""
MYFIELDTYPESDICTStr += f"""{CBSTR}
"""
MYDEFAULTSDICTSQLStr += f"""{CBSTR}
"""
MYDEFAULTSDICTSCNStr += f"""{CBSTR}
"""
HEADERNAMEDICTStr += f"""{CBSTR}
"""
NUMERICFILLERDICTStr += f"""{CBSTR}
"""


FDOut.write(f"""
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * top cut for the dictMaker stuff *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * all of the "defines" for the package 
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
{definesStr}
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * field default values (SQL ready) dict
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
{MYDEFAULTSDICTSQLStr}
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * field defaults (screen ready) dict
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
{MYDEFAULTSDICTSCNStr}
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * field types dict
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
{MYFIELDTYPESDICTStr}
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * header names dict
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
{HEADERNAMEDICTStr}
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * numeric (list index) filler dict
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
{NUMERICFILLERDICTStr}
{NUMERICFILLERSStr}
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * bottom cut for dictMaker #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

""")
FDOut.flush()
FDOut.close()


# FDOut = open("sortedAllTheList.py", "w")
# FDOut.write(repr(allTheList))
# FDOut.flush()
# FDOut.close()



