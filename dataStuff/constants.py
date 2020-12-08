

DEBUGME = 0

CACHEDIR = lambda FILENAME: f"""/home/will/.cache/earthquakesUSGS/{FILENAME}"""
CSVFEEDALL = lambda TERM: f"""https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_{TERM}.csv"""
GEOJSONALLSMRY = lambda TERM: f"""https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_{TERM}.geojson"""
GEOJSONDETAIL = lambda ID: f"""https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/{ID}.geojson"""
GEOJSONDETAILQUERY = lambda ID: f"""https://earthquake.usgs.gov/fdsnws/event/1/query?eventid={ID}&format=geojson"""
GEOJSONQUERY = lambda QUERY: f"""https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson{QUERY}"""

DATATABLENAME = "USGSData"
STATSTABLENAME = "USGSStats"
QUERIESINTABLENAME = "queriesIn"
GEOJSONFILEENTRYTABLENAME = "geoJsonFileEntries"
GEOJSONEVENTSTABLENAME = "geoJsonEvents"
GEOJSONPREFIXTABLENAME = "PFXprefix"
NUMROWSPERPG = 150
NUMLINESPERSEG = 15

BSSTR = '\\'
CBSSTR = "]"
CBSTR = "}"
DBLQT = '"'
DQTSTR = '"'
INDENTIN = ' -=> '
INDENTOUT = ' <=- '
NEWLINE = "\n"
OBSSTR = "["
OBSTR = "{"
SGLQT = "'"
TABSTR = "\t"

EMPTYDICT = {}
EMPTYLIST = []
EMPTYSTR = ""
EMPTYTUPLE = ()
DEFLAT = 41.0
DEFLON = -112.0
DEFQUERYNUM = 1
DFLTDEC = 0.0
DFLTDT = '"1970-01-01 00:00:01"'
DFLTFLOAT = 0.0
DFLTINT = 0
DFLTSTR = SGLQT + DQTSTR + DQTSTR + SGLQT
DFLTstr = ""
DFlTSTR = DQTSTR + SGLQT + SGLQT + DQTSTR
DFlTstr = ''

JSONCBRACKETS = [CBSTR, CBSSTR]
JSONOBRACKETS = [OBSTR, OBSSTR]
QTEMPTYDICT = DBLQT + "{}" + DBLQT
QTEMPTYLIST = DBLQT + "[]" + DBLQT
QTEMPTYTUPLE = DBLQT + "()" + DBLQT
SQLLIMITSSTR = " limit 0, 100"

DATETIME = "datetime"
DECIMAL = "decimal"
DICT = "dict"
FLOAT = "float"
INT = "int"
KEY = "key"
LIST = "list"
TUPLE = "tuple"
VARCHAR = "varchar"


SQLCONFIG = \
	{
		'user': 'seismicUser',
		'password': 'A5HG51HqT67m20NwM8X8',
		'host': 'localhost',
		'database': 'seismicData',
	}



# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * top cut for the dictMaker stuff *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * all of the "defines" for the package
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
AFFECTEDROWS = "AFFECTEDROWS"
api = "api"
BBMAXDEPTH = "BBMAXDEPTH"
BBMAXLAT = "BBMAXLAT"
BBMAXLON = "BBMAXLON"
BBMINDEPTH = "BBMINDEPTH"
BBMINLAT = "BBMINLAT"
BBMINLON = "BBMINLON"
bbox = "bbox"
BBoxMaxDepth = "BBoxMaxDepth"
BBoxMaxLat = "BBoxMaxLat"
BBoxMaxLon = "BBoxMaxLon"
BBoxMinDepth = "BBoxMinDepth"
BBoxMinLat = "BBoxMinLat"
BBoxMinLon = "BBoxMinLon"
CEQID = "CEQID"
CKMFROM = "CKMFROM"
coordinates = "coordinates"
count = "count"
CRID = "CRID"
DEFAULTSCN = "DEFAULTSCN"
DEFAULTSQL = "DEFAULTSQL"
DBCONNECTION = "DBCONNECTION"
DBCURSOR = "DBCURSOR"
detail = "detail"
detailRID = "detailRID"
eventID = "eventID"
features = "features"
featureType = "featureType"
FILEENTRY = "FILEENTRY"
fileEntryRID = "fileEntryRID"
fileType = "fileType"
generated = "generated"
geoDepth = "geoDepth"
geoKMFrom = "geoKMFrom"
geoKMFROMHM = "geoKMFROMHM"
geoLat = "geoLat"
geoLon = "geoLon"
geometry = "geometry"
geoType = "geoType"
HEADER = "HEADER"
id_ = "id"
IJSONPREFIX = "IJSONPREFIX"
IJSONTYPE = "IJSONTYPE"
IJSONVALUE = "IJSONVALUE"
ISLOADED = "ISLOADED"
limit = "limit"
metaAPI = "metaAPI"
metadata = "metadata"
metaFileRID = "metaFileRID"
metaFileStatus = "metaFileStatus"
metaFileTitle = "metaFileTitle"
metaGeneratedTime = "metaGeneratedTime"
metaLimit = "metaLimit"
metaOffset = "metaOffset"
metaRecordCount = "metaRecordCount"
metaURL = "metaURL"
NAME = "NAME"
NUMROWS = "NUMROWS"
offset = "offset"
OFPGS = "OFPGS"
parmEndTime = "parmEndTime"
parmLimit = "parmLimit"
parmOffset = "parmOffset"
parmStartTime = "parmStartTime"
parmUrl01 = "parmUrl01"
parmUrl02 = "parmUrl02"
parmUrl03 = "parmUrl03"
parmUrl04 = "parmUrl04"
parmUrl05 = "parmUrl05"
PFX_ = "PFX"
PFXDBTable = "PFXDBTable"
PFXdescription = "PFXdescription"
PFXfieldNameL = "PFXfieldNameL"
PFXfieldNameZ = "PFXfieldNameZ"
PFXfirstSeen = "PFXfirstSeen"
PFXkeyType = "PFXkeyType"
PFXlastSeen = "PFXlastSeen"
PFXprefixStr = "PFXprefixStr"
PFXyieldThis = "PFXyieldThis"
PGNUM = "PGNUM"
PPropKey = "PPropKey"
prefix = "prefix"
prodCode = "prodCode"
prodID = "prodID"
prodProps = "prodProps"
prodSource = "prodSource"
prodStatus = "prodStatus"
prodType = "prodType"
productType = "productType"
prodUpdatedZ = "prodUpdatedZ"
propAlert = "propAlert"
propCode = "propCode"
propCompDYFIIndex = "propCompDYFIIndex"
propDegMinToStation = "propDegMinToStation"
propDepthErr = "propDepthErr"
propDetailUrl = "propDetailUrl"
properties = "properties"
propEventType = "propEventType"
propFelt = "propFelt"
propHorizontalErr = "propHorizontalErr"
propIDsUsed = "propIDsUsed"
propLocationSrc = "propLocationSrc"
propMag = "propMag"
propMagErr = "propMagErr"
propMagNST = "propMagNST"
propMagSrc = "propMagSrc"
propMagType = "propMagType"
propMaxAzmGap = "propMaxAzmGap"
propMaxMeasuredIntensity = "propMaxMeasuredIntensity"
propNetwork = "propNetwork"
propNumStations = "propNumStations"
propPFDWT = "propPFDWT"
propPlace = "propPlace"
propProducts = "propProducts"
propProductTypesUsed = "propProductTypesUsed"
propRMS = "propRMS"
propSignificanceIndex = "propSignificanceIndex"
propSourcesUsed = "propSourcesUsed"
propStatus = "propStatus"
propTimeL = "propTimeL"
propTimeZ = "propTimeZ"
propTitle = "propTitle"
propTsunami = "propTsunami"
propTZLM = "propTZLM"
propUpdatedL = "propUpdatedL"
propUpdatedZ = "propUpdatedZ"
propUrl = "propUrl"
QUERIESINRETURNTO = "QUERIESINRETURNTO"
QUERIESINTITLE = "QUERIESINTITLE"
QUERYEMPTY = "QUERYEMPTY"
QUERYFROMPRESET = "QUERYFROMPRESET"
QUERYLOADED = "QUERYLOADED"
QUERYNUM = "QUERYNUM"
REGION0DESCRIPTION = "REGION0DESCRIPTION"
REGION0EAST = "REGION0EAST"
REGION0KMFROM = "REGION0KMFROM"
REGION0NAME = "REGION0NAME"
REGION0NORTH = "REGION0NORTH"
REGION0SOUTH = "REGION0SOUTH"
REGION0WEST = "REGION0WEST"
REGION1DESCRIPTION = "REGION1DESCRIPTION"
REGION1EAST = "REGION1EAST"
REGION1KMFROM = "REGION1KMFROM"
REGION1NAME = "REGION1NAME"
REGION1NORTH = "REGION1NORTH"
REGION1SOUTH = "REGION1SOUTH"
REGION1WEST = "REGION1WEST"
REGION2DESCRIPTION = "REGION2DESCRIPTION"
REGION2EAST = "REGION2EAST"
REGION2KMFROM = "REGION2KMFROM"
REGION2NAME = "REGION2NAME"
REGION2NORTH = "REGION2NORTH"
REGION2SOUTH = "REGION2SOUTH"
REGION2WEST = "REGION2WEST"
REGION3DESCRIPTION = "REGION3DESCRIPTION"
REGION3EAST = "REGION3EAST"
REGION3KMFROM = "REGION3KMFROM"
REGION3NAME = "REGION3NAME"
REGION3NORTH = "REGION3NORTH"
REGION3SOUTH = "REGION3SOUTH"
REGION3WEST = "REGION3WEST"
RID = "RID"
ROWNUM = "ROWNUM"
ROWSDICT = "ROWSDICT"
sincePropTimeL = "sincePropTimeL"
sincePropTimeZ = "sincePropTimeZ"
sincePropUpdatedL = "sincePropUpdatedL"
sincePropUpdatedZ = "sincePropUpdatedZ"
SQLGROUPBY = "SQLGROUPBY"
SQLHAVING = "SQLHAVING"
SQLLIMIT = "SQLLIMIT"
SQLORDERBY = "SQLORDERBY"
SQLSELECT = "SQLSELECT"
SQLWHERE = "SQLWHERE"
STARTRECNUM = "STARTRECNUM"
status = "status"
title = "title"
TYPE = "TYPE"
type_ = "type"
url = "url"


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * field default values (SQL ready) dict
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
MYDEFAULTSDICTSQL = {
	AFFECTEDROWS: DFLTINT,
	api: DFLTSTR,
	bbox: QTEMPTYDICT,
	BBoxMaxDepth: DFLTDEC,
	BBoxMaxLat: DFLTDEC,
	BBoxMaxLon: DFLTDEC,
	BBoxMinDepth: DFLTDEC,
	BBoxMinLat: DFLTDEC,
	BBoxMinLon: DFLTDEC,
	CEQID: DFLTINT,
	CKMFROM: DFLTDEC,
	coordinates: QTEMPTYLIST,
	count: DFLTINT,
	CRID: DFLTINT,
	detail: DFLTSTR,
	detailRID: DFLTINT,
	eventID: DFLTSTR,
	features: QTEMPTYDICT,
	featureType: DFLTSTR,
	FILEENTRY: QTEMPTYDICT,
	fileEntryRID: DFLTINT,
	fileType: DFLTSTR,
	generated: DFLTSTR,
	geoDepth: DFLTDEC,
	geoKMFrom: DFLTDEC,
	geoKMFROMHM: DFLTDEC,
	geoLat: DFLTDEC,
	geoLon: DFLTDEC,
	geometry: QTEMPTYDICT,
	geoType: DFLTSTR,
	ISLOADED: DFLTINT,
	limit: DFLTINT,
	metaAPI: DFLTSTR,
	metadata: QTEMPTYDICT,
	metaFileRID: DFLTINT,
	metaFileStatus: DFLTINT,
	metaFileTitle: DFLTSTR,
	metaGeneratedTime: DFLTSTR,
	metaLimit: DFLTINT,
	metaOffset: DFLTINT,
	metaRecordCount: DFLTINT,
	metaURL: DFLTSTR,
	NUMROWS: DFLTINT,
	offset: DFLTINT,
	OFPGS: DFLTINT,
	PFXDBTable: DFLTSTR,
	PFXdescription: DFLTSTR,
	PFXfieldNameL: DFLTSTR,
	PFXfieldNameZ: DFLTSTR,
	PFXfirstSeen: DFLTDT,
	PFXkeyType: DFLTSTR,
	PFXlastSeen: DFLTDT,
	PFXprefixStr: DFLTSTR,
	PFXyieldThis: DFLTSTR,
	PGNUM: DFLTINT,
	PPropKey: DFLTSTR,
	prefix: DFLTSTR,
	prodCode: DFLTSTR,
	prodID: DFLTSTR,
	prodProps: QTEMPTYDICT,
	prodSource: DFLTSTR,
	prodStatus: DFLTSTR,
	prodType: DFLTSTR,
	productType: DFLTSTR,
	prodUpdatedZ: DFLTDT,
	propAlert: DFLTSTR,
	propCode: DFLTSTR,
	propCompDYFIIndex: DFLTDEC,
	propDegMinToStation: DFLTDEC,
	propDepthErr: DFLTDEC,
	propDetailUrl: DFLTSTR,
	properties: QTEMPTYDICT,
	propEventType: DFLTSTR,
	propFelt: DFLTINT,
	propHorizontalErr: DFLTDEC,
	propIDsUsed: DFLTSTR,
	propLocationSrc: DFLTSTR,
	propMag: DFLTDEC,
	propMagErr: DFLTDEC,
	propMagNST: DFLTINT,
	propMagSrc: DFLTSTR,
	propMagType: DFLTSTR,
	propMaxAzmGap: DFLTDEC,
	propMaxMeasuredIntensity: DFLTDEC,
	propNetwork: DFLTSTR,
	propNumStations: DFLTINT,
	propPFDWT: DFLTINT,
	propPlace: DFLTSTR,
	propProducts: QTEMPTYDICT,
	propProductTypesUsed: DFLTSTR,
	propRMS: DFLTDEC,
	propSignificanceIndex: DFLTINT,
	propSourcesUsed: DFLTSTR,
	propStatus: DFLTSTR,
	propTimeL: DFLTSTR,
	propTimeZ: DFLTSTR,
	propTitle: DFLTSTR,
	propTsunami: DFLTINT,
	propTZLM: DFLTINT,
	propUpdatedL: DFLTSTR,
	propUpdatedZ: DFLTSTR,
	propUrl: DFLTSTR,
	QUERIESINRETURNTO: DFLTSTR,
	QUERIESINTITLE: DFLTSTR,
	QUERYNUM: DFLTINT,
	REGION0DESCRIPTION: DFLTSTR,
	REGION0EAST: DFLTDEC,
	REGION0KMFROM: DFLTDEC,
	REGION0NAME: DFLTSTR,
	REGION0NORTH: DFLTDEC,
	REGION0SOUTH: DFLTDEC,
	REGION0WEST: DFLTDEC,
	REGION1DESCRIPTION: DFLTSTR,
	REGION1EAST: DFLTDEC,
	REGION1KMFROM: DFLTDEC,
	REGION1NAME: DFLTSTR,
	REGION1NORTH: DFLTDEC,
	REGION1SOUTH: DFLTDEC,
	REGION1WEST: DFLTDEC,
	REGION2DESCRIPTION: DFLTSTR,
	REGION2EAST: DFLTDEC,
	REGION2KMFROM: DFLTDEC,
	REGION2NAME: DFLTSTR,
	REGION2NORTH: DFLTDEC,
	REGION2SOUTH: DFLTDEC,
	REGION2WEST: DFLTDEC,
	REGION3DESCRIPTION: DFLTSTR,
	REGION3EAST: DFLTDEC,
	REGION3KMFROM: DFLTDEC,
	REGION3NAME: DFLTSTR,
	REGION3NORTH: DFLTDEC,
	REGION3SOUTH: DFLTDEC,
	REGION3WEST: DFLTDEC,
	RID: DFLTINT,
	ROWNUM: DFLTINT,
	ROWSDICT: EMPTYDICT,
	sincePropTimeL: DFLTSTR,
	sincePropTimeZ: DFLTSTR,
	sincePropUpdatedL: DFLTSTR,
	sincePropUpdatedZ: DFLTSTR,
	SQLGROUPBY: DFLTSTR,
	SQLHAVING: DFLTSTR,
	SQLLIMIT: DFLTSTR,
	SQLORDERBY: DFLTSTR,
	SQLSELECT: DFLTSTR,
	SQLWHERE: DFLTSTR,
	STARTRECNUM: DFLTINT,
	status: DFLTSTR,
	title: DFLTSTR,
	url: DFLTSTR,
	"alert": DFLTSTR,
	"cdi": DFLTINT,
	"code": DFLTSTR,
	"detail": DFLTSTR,
	"dmin": DFLTDEC,
	"felt": DFLTINT,
	"gap": DFLTDEC,
	"ids": DFLTSTR,
	"mag": DFLTDEC,
	"magType": DFLTSTR,
	"mmi": DFLTDEC,
	"net": DFLTSTR,
	"nst": DFLTINT,
	"place": DFLTSTR,
	"propNumStations": DFLTINT,
	"rms": DFLTDEC,
	"sig": DFLTINT,
	"sources": DFLTSTR,
	"status": DFLTSTR,
	"time": DFLTDT,
	"title": DFLTSTR,
	"tsunami": DFLTINT,
	"type": DFLTSTR,
	"types": DFLTSTR,
	"type_": DFLTSTR,
	"tz": DFLTINT,
	"updated": DFLTINT,
	"url": DFLTSTR,
}

# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * field defaults (screen ready) dict
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
MYDEFAULTSDICTSCN = {
	AFFECTEDROWS: DFLTINT,
	api: DFLTstr,
	bbox: EMPTYDICT,
	BBoxMaxDepth: DFLTDEC,
	BBoxMaxLat: DFLTDEC,
	BBoxMaxLon: DFLTDEC,
	BBoxMinDepth: DFLTDEC,
	BBoxMinLat: DFLTDEC,
	BBoxMinLon: DFLTDEC,
	CEQID: DFLTINT,
	CKMFROM: DFLTDEC,
	coordinates: EMPTYLIST,
	count: DFLTINT,
	CRID: DFLTINT,
	detail: DFLTstr,
	detailRID: DFLTINT,
	eventID: DFLTstr,
	features: QTEMPTYDICT,
	featureType: DFLTstr,
	FILEENTRY: EMPTYDICT,
	fileEntryRID: DFLTINT,
	fileType: DFLTstr,
	generated: DFLTstr,
	geoDepth: DFLTDEC,
	geoKMFrom: DFLTDEC,
	geoKMFROMHM: DFLTDEC,
	geoLat: DFLTDEC,
	geoLon: DFLTDEC,
	geometry: EMPTYDICT,
	geoType: DFLTstr,
	ISLOADED: DFLTINT,
	limit: DFLTINT,
	metaAPI: DFLTstr,
	metadata: EMPTYDICT,
	metaFileRID: DFLTINT,
	metaFileStatus: DFLTINT,
	metaFileTitle: DFLTstr,
	metaGeneratedTime: DFLTstr,
	metaLimit: DFLTINT,
	metaOffset: DFLTINT,
	metaRecordCount: DFLTINT,
	metaURL: DFLTstr,
	NUMROWS: DFLTINT,
	offset: DFLTINT,
	OFPGS: DFLTINT,
	PFXDBTable: DFLTstr,
	PFXdescription: DFLTstr,
	PFXfieldNameL: DFLTstr,
	PFXfieldNameZ: DFLTstr,
	PFXfirstSeen: DFLTDT,
	PFXkeyType: DFLTstr,
	PFXlastSeen: DFLTDT,
	PFXprefixStr: DFLTstr,
	PFXyieldThis: DFLTstr,
	PGNUM: DFLTINT,
	PPropKey: DFLTstr,
	prefix: DFLTstr,
	prodCode: DFLTstr,
	prodID: DFLTstr,
	prodProps: EMPTYDICT,
	prodSource: DFLTstr,
	prodStatus: DFLTstr,
	prodType: DFLTstr,
	productType: DFLTstr,
	prodUpdatedZ: DFLTDT,
	propAlert: DFLTstr,
	propCode: DFLTstr,
	propCompDYFIIndex: DFLTDEC,
	propDegMinToStation: DFLTDEC,
	propDepthErr: DFLTDEC,
	propDetailUrl: DFLTstr,
	properties: EMPTYDICT,
	propEventType: DFLTstr,
	propFelt: DFLTINT,
	propHorizontalErr: DFLTDEC,
	propIDsUsed: DFLTstr,
	propLocationSrc: DFLTstr,
	propMag: DFLTDEC,
	propMagErr: DFLTDEC,
	propMagNST: DFLTINT,
	propMagSrc: DFLTstr,
	propMagType: DFLTstr,
	propMaxAzmGap: DFLTDEC,
	propMaxMeasuredIntensity: DFLTDEC,
	propNetwork: DFLTstr,
	propNumStations: DFLTINT,
	propPFDWT: DFLTINT,
	propPlace: DFLTstr,
	propProducts: EMPTYDICT,
	propProductTypesUsed: DFLTstr,
	propRMS: DFLTDEC,
	propSignificanceIndex: DFLTINT,
	propSourcesUsed: DFLTstr,
	propStatus: DFLTstr,
	propTimeL: DFLTstr,
	propTimeZ: DFLTstr,
	propTitle: DFLTstr,
	propTsunami: DFLTINT,
	propTZLM: DFLTINT,
	propUpdatedL: DFLTstr,
	propUpdatedZ: DFLTstr,
	propUrl: DFLTstr,
	QUERIESINRETURNTO: DFLTstr,
	QUERIESINTITLE: DFLTstr,
	QUERYNUM: DFLTINT,
	REGION0DESCRIPTION: DFLTstr,
	REGION0EAST: DFLTDEC,
	REGION0KMFROM: DFLTDEC,
	REGION0NAME: DFLTstr,
	REGION0NORTH: DFLTDEC,
	REGION0SOUTH: DFLTDEC,
	REGION0WEST: DFLTDEC,
	REGION1DESCRIPTION: DFLTstr,
	REGION1EAST: DFLTDEC,
	REGION1KMFROM: DFLTDEC,
	REGION1NAME: DFLTstr,
	REGION1NORTH: DFLTDEC,
	REGION1SOUTH: DFLTDEC,
	REGION1WEST: DFLTDEC,
	REGION2DESCRIPTION: DFLTstr,
	REGION2EAST: DFLTDEC,
	REGION2KMFROM: DFLTDEC,
	REGION2NAME: DFLTstr,
	REGION2NORTH: DFLTDEC,
	REGION2SOUTH: DFLTDEC,
	REGION2WEST: DFLTDEC,
	REGION3DESCRIPTION: DFLTstr,
	REGION3EAST: DFLTDEC,
	REGION3KMFROM: DFLTDEC,
	REGION3NAME: DFLTstr,
	REGION3NORTH: DFLTDEC,
	REGION3SOUTH: DFLTDEC,
	REGION3WEST: DFLTDEC,
	RID: DFLTINT,
	ROWNUM: DFLTINT,
	ROWSDICT: EMPTYDICT,
	sincePropTimeL: DFLTstr,
	sincePropTimeZ: DFLTstr,
	sincePropUpdatedL: DFLTstr,
	sincePropUpdatedZ: DFLTstr,
	SQLGROUPBY: DFLTstr,
	SQLHAVING: DFLTstr,
	SQLLIMIT: DFLTstr,
	SQLORDERBY: DFLTstr,
	SQLSELECT: DFLTstr,
	SQLWHERE: DFLTstr,
	STARTRECNUM: DFLTINT,
	status: DFLTstr,
	title: DFLTstr,
	url: DFLTstr,
	"alert": DFLTstr,
	"cdi": DFLTINT,
	"code": DFLTstr,
	"detail": DFLTstr,
	"dmin": DFLTDEC,
	"felt": DFLTINT,
	"gap": DFLTDEC,
	"ids": DFLTstr,
	"mag": DFLTDEC,
	"magType": DFLTstr,
	"mmi": DFLTDEC,
	"net": DFLTstr,
	"nst": DFLTINT,
	"place": DFLTstr,
	"propNumStations": DFLTINT,
	"rms": DFLTDEC,
	"sig": DFLTINT,
	"sources": DFLTstr,
	"status": DFLTstr,
	"time": DFLTDT,
	"title": DFLTstr,
	"tsunami": DFLTINT,
	"type": DFLTstr,
	"types": DFLTstr,
	"type_": DFLTstr,
	"tz": DFLTINT,
	"updated": DFLTINT,
	"url": DFLTstr,
}

# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * field types dict
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
MYFIELDTYPESDICT = {
	AFFECTEDROWS: INT,
	api: VARCHAR,
	bbox: DICT,
	BBoxMaxDepth: DECIMAL,
	BBoxMaxLat: DECIMAL,
	BBoxMaxLon: DECIMAL,
	BBoxMinDepth: DECIMAL,
	BBoxMinLat: DECIMAL,
	BBoxMinLon: DECIMAL,
	CEQID: INT,
	CKMFROM: DECIMAL,
	coordinates: LIST,
	count: INT,
	CRID: INT,
	detail: VARCHAR,
	detailRID: INT,
	eventID: VARCHAR,
	features: dict,
	featureType: VARCHAR,
	FILEENTRY: dict,
	fileEntryRID: INT,
	fileType: VARCHAR,
	generated: DATETIME,
	geoDepth: DECIMAL,
	geoKMFrom: DECIMAL,
	geoKMFROMHM: DECIMAL,
	geoLat: DECIMAL,
	geoLon: DECIMAL,
	geometry: dict,
	geoType: VARCHAR,
	ISLOADED: INT,
	limit: INT,
	metaAPI: VARCHAR,
	metadata: dict,
	metaFileRID: INT,
	metaFileStatus: INT,
	metaFileTitle: VARCHAR,
	metaGeneratedTime: DATETIME,
	metaLimit: INT,
	metaOffset: INT,
	metaRecordCount: INT,
	metaURL: VARCHAR,
	NUMROWS: INT,
	offset: INT,
	OFPGS: INT,
	PFXDBTable: VARCHAR,
	PFXdescription: VARCHAR,
	PFXfieldNameL: VARCHAR,
	PFXfieldNameZ: VARCHAR,
	PFXfirstSeen: DATETIME,
	PFXkeyType: VARCHAR,
	PFXlastSeen: DATETIME,
	PFXprefixStr: VARCHAR,
	PFXyieldThis: VARCHAR,
	PGNUM: INT,
	PPropKey: VARCHAR,
	prefix: VARCHAR,
	prodCode: VARCHAR,
	prodID: VARCHAR,
	prodProps: dict,
	prodSource: VARCHAR,
	prodStatus: VARCHAR,
	prodType: VARCHAR,
	productType: VARCHAR,
	prodUpdatedZ: DATETIME,
	propAlert: VARCHAR,
	propCode: VARCHAR,
	propCompDYFIIndex: DECIMAL,
	propDegMinToStation: DECIMAL,
	propDepthErr: DECIMAL,
	propDetailUrl: VARCHAR,
	properties: dict,
	propEventType: VARCHAR,
	propFelt: INT,
	propHorizontalErr: DECIMAL,
	propIDsUsed: VARCHAR,
	propLocationSrc: VARCHAR,
	propMag: DECIMAL,
	propMagErr: DECIMAL,
	propMagNST: INT,
	propMagSrc: VARCHAR,
	propMagType: VARCHAR,
	propMaxAzmGap: DECIMAL,
	propMaxMeasuredIntensity: DECIMAL,
	propNetwork: VARCHAR,
	propNumStations: INT,
	propPFDWT: INT,
	propPlace: VARCHAR,
	propProducts: dict,
	propProductTypesUsed: VARCHAR,
	propRMS: DECIMAL,
	propSignificanceIndex: INT,
	propSourcesUsed: VARCHAR,
	propStatus: VARCHAR,
	propTimeL: DATETIME,
	propTimeZ: DATETIME,
	propTitle: VARCHAR,
	propTsunami: INT,
	propTZLM: INT,
	propUpdatedL: DATETIME,
	propUpdatedZ: DATETIME,
	propUrl: VARCHAR,
	QUERIESINRETURNTO: VARCHAR,
	QUERIESINTITLE: VARCHAR,
	QUERYNUM: INT,
	REGION0DESCRIPTION: VARCHAR,
	REGION0EAST: DECIMAL,
	REGION0KMFROM: DECIMAL,
	REGION0NAME: VARCHAR,
	REGION0NORTH: DECIMAL,
	REGION0SOUTH: DECIMAL,
	REGION0WEST: DECIMAL,
	REGION1DESCRIPTION: VARCHAR,
	REGION1EAST: DECIMAL,
	REGION1KMFROM: DECIMAL,
	REGION1NAME: VARCHAR,
	REGION1NORTH: DECIMAL,
	REGION1SOUTH: DECIMAL,
	REGION1WEST: DECIMAL,
	REGION2DESCRIPTION: VARCHAR,
	REGION2EAST: DECIMAL,
	REGION2KMFROM: DECIMAL,
	REGION2NAME: VARCHAR,
	REGION2NORTH: DECIMAL,
	REGION2SOUTH: DECIMAL,
	REGION2WEST: DECIMAL,
	REGION3DESCRIPTION: VARCHAR,
	REGION3EAST: DECIMAL,
	REGION3KMFROM: DECIMAL,
	REGION3NAME: VARCHAR,
	REGION3NORTH: DECIMAL,
	REGION3SOUTH: DECIMAL,
	REGION3WEST: DECIMAL,
	RID: INT,
	ROWNUM: INT,
	ROWSDICT: DICT,
	sincePropTimeL: DATETIME,
	sincePropTimeZ: DATETIME,
	sincePropUpdatedL: DATETIME,
	sincePropUpdatedZ: DATETIME,
	SQLGROUPBY: VARCHAR,
	SQLHAVING: VARCHAR,
	SQLLIMIT: VARCHAR,
	SQLORDERBY: VARCHAR,
	SQLSELECT: VARCHAR,
	SQLWHERE: VARCHAR,
	STARTRECNUM: INT,
	status: VARCHAR,
	title: VARCHAR,
	url: VARCHAR,
	"alert": VARCHAR,
	"cdi": INT,
	"code": VARCHAR,
	"detail": VARCHAR,
	"dmin": DECIMAL,
	"felt": INT,
	"gap": DECIMAL,
	"ids": VARCHAR,
	"mag": DECIMAL,
	"magType": VARCHAR,
	"mmi": DECIMAL,
	"net": VARCHAR,
	"nst": INT,
	"place": VARCHAR,
	"propNumStations": INT,
	"rms": DECIMAL,
	"sig": INT,
	"sources": VARCHAR,
	"status": VARCHAR,
	"time": INT,
	"title": VARCHAR,
	"tsunami": INT,
	"type": VARCHAR,
	"types": VARCHAR,
	"type_": VARCHAR,
	"tz": INT,
	"updated": INT,
	"url": VARCHAR,
}

# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * header names dict
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
HEADERNAMEDICT = {
	AFFECTEDROWS: "AFFROWS",
	api: "API",
	bbox: "BBOX",
	BBoxMaxDepth: "BBOXDN",
	BBoxMaxLat: "BBOXNTH",
	BBoxMaxLon: "BBOXWST",
	BBoxMinDepth: "BBOXUP",
	BBoxMinLat: "BBOXSTH",
	BBoxMinLon: "BBOXEST",
	CEQID: "CEQID",
	CKMFROM: "CKMFROM",
	coordinates: "COORDINATES",
	count: "COUNT",
	CRID: "CRID",
	detail: "DETAIL URL",
	detailRID: "DRID",
	eventID: "EQID",
	features: "FEATURES",
	featureType: "FEATURE TYPE",
	FILEENTRY: "FILEENTRY",
	fileEntryRID: "FERID",
	fileType: "FILE TYPE",
	generated: "timestamp",
	geoDepth: "DEPTH",
	geoKMFrom: "KM2GO",
	geoKMFROMHM: "KM2HM",
	geoLat: "LAT",
	geoLon: "LON",
	geometry: "geo",
	geoType: "GEO TYPE",
	ISLOADED: "LOADED",
	limit: "LIMIT",
	metaAPI: "API",
	metadata: "META",
	metaFileRID: "METARID",
	metaFileStatus: "FSTAT",
	metaFileTitle: "METATITLE",
	metaGeneratedTime: "TIMESTAMP",
	metaLimit: "LIMIT",
	metaOffset: "OFFSET",
	metaRecordCount: "CMETARID",
	metaURL: "META URL",
	NUMROWS: "NUMROWS",
	offset: "OFFSET",
	OFPGS: "OF PGS",
	PFXDBTable: "DBTABLE",
	PFXdescription: "DESCR",
	PFXfieldNameL: "FIELDNML",
	PFXfieldNameZ: "FIELDNMZ",
	PFXfirstSeen: "1ST SEEN",
	PFXkeyType: "KEYTYPE",
	PFXlastSeen: "LAST SEEN",
	PFXprefixStr: "PREFIXSTR",
	PFXyieldThis: "YIELDS",
	PGNUM: "PG NM",
	PPropKey: "PPKEY",
	prefix: "IJPREFIX",
	prodCode: "PRODCODE",
	prodID: "PRODID",
	prodProps: "PRODPROPS",
	prodSource: "PRODSRC",
	prodStatus: "PRODSTAT",
	prodType: "PRODTYPE",
	productType: "PRODUCTTYPE",
	prodUpdatedZ: "PRODUPDATEDZ",
	propAlert: "ALERT",
	propCode: "CODE",
	propCompDYFIIndex: "DYFI",
	propDegMinToStation: "DM2S",
	propDepthErr: "DNERR",
	propDetailUrl: "DETAIL URL",
	properties: "PROPS",
	propEventType: "EVENT TYPE",
	propFelt: "FELT",
	propHorizontalErr: "HORZERR",
	propIDsUsed: "IDs",
	propLocationSrc: "LCNSRC",
	propMag: "MAG",
	propMagErr: "MAGERR",
	propMagNST: "MAGNST",
	propMagSrc: "MAGSRC",
	propMagType: "MAGTYPE",
	propMaxAzmGap: "GAP",
	propMaxMeasuredIntensity: "MMI",
	propNetwork: "NET",
	propNumStations: "NST",
	propPFDWT: "PFD WT",
	propPlace: "PLACE",
	propProducts: "PRODS",
	propProductTypesUsed: "PRODUCTS",
	propRMS: "RMS",
	propSignificanceIndex: "SIG",
	propSourcesUsed: "SRCS",
	propStatus: "STAT",
	propTimeL: "TIMEL",
	propTimeZ: "TIMEZ",
	propTitle: "TITLE",
	propTsunami: "TSNMI",
	propTZLM: "TZM",
	propUpdatedL: "UPDL",
	propUpdatedZ: "UPDZ",
	propUrl: "URL",
	QUERIESINRETURNTO: "RTS",
	QUERIESINTITLE: "QRYTITL",
	QUERYNUM: "QRID",
	REGION0DESCRIPTION: "region 0 desc",
	REGION0EAST: "R0EST",
	REGION0KMFROM: "R0KMFM",
	REGION0NAME: "R0NM",
	REGION0NORTH: "R0NTH",
	REGION0SOUTH: "R0STH",
	REGION0WEST: "R0WST",
	REGION1DESCRIPTION: "region 1 desc",
	REGION1EAST: "R1EST",
	REGION1KMFROM: "R1KMFMHM",
	REGION1NAME: "R1NM",
	REGION1NORTH: "R1NTH",
	REGION1SOUTH: "R1STH",
	REGION1WEST: "R1WST",
	REGION2DESCRIPTION: "region 2 desc",
	REGION2EAST: "R2EST",
	REGION2KMFROM: "R2KMFMHM",
	REGION2NAME: "R2NM",
	REGION2NORTH: "R2NTH",
	REGION2SOUTH: "R2STH",
	REGION2WEST: "R2WST",
	REGION3DESCRIPTION: "region 3 desc",
	REGION3EAST: "R3EST",
	REGION3KMFROM: "R3KMFMHM",
	REGION3NAME: "R3NM",
	REGION3NORTH: "R3NTH",
	REGION3SOUTH: "R3STH",
	REGION3WEST: "R3WST",
	RID: "RID",
	ROWNUM: "ROW#",
	ROWSDICT: "ROWSDICT",
	sincePropTimeL: "SINCELL",
	sincePropTimeZ: "SINCEZ",
	sincePropUpdatedL: "SINCEUPDL",
	sincePropUpdatedZ: "SINCEUPDZ",
	SQLGROUPBY: "GRPBY",
	SQLHAVING: "HAVE",
	SQLLIMIT: "LTD",
	SQLORDERBY: "SORT",
	SQLSELECT: "SLCT",
	SQLWHERE: "WHERE",
	STARTRECNUM: "STRTNUM",
	status: "STAT",
	title: "TITLE",
	url: "URL",
	"alert": "",
	"cdi": "",
	"code": "",
	"detail": "",
	"dmin": "",
	"felt": "",
	"gap": "",
	"ids": "",
	"mag": "",
	"magType": "",
	"mmi": "",
	"net": "",
	"nst": "",
	"place": "",
	"propNumStations": "",
	"rms": "",
	"sig": "",
	"sources": "",
	"status": "",
	"time": "",
	"title": "",
	"tsunami": "",
	"type": "",
	"types": "",
	"type_": "",
	"tz": "",
	"updated": "",
	"url": "",
}

# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * numeric (list index) filler dict
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
NUMERICFILLERDICT = {
	BBMAXDEPTH: 5,
	BBMAXLAT: 4,
	BBMAXLON: 3,
	BBMINDEPTH: 2,
	BBMINLAT: 1,
	BBMINLON: 0,
	DEFAULTSCN: 2,
	DEFAULTSQL: 1,
	DBCONNECTION: 0,
	DBCURSOR: 1,
	HEADER: 4,
	IJSONPREFIX: 0,
	IJSONTYPE: 1,
	IJSONVALUE: 2,
	NAME: 0,
	parmEndTime: 0,
	parmLimit: 1,
	parmOffset: 2,
	parmStartTime: 3,
	parmUrl01: 4,
	parmUrl02: 5,
	parmUrl03: 6,
	parmUrl04: 7,
	parmUrl05: 8,
	QUERYEMPTY: 0,
	QUERYFROMPRESET: 1,
	QUERYLOADED: -1,
	TYPE: 3,
}

BBMAXDEPTH = 5
BBMAXLAT = 4
BBMAXLON = 3
BBMINDEPTH = 2
BBMINLAT = 1
BBMINLON = 0
DEFAULTSCN = 2
DEFAULTSQL = 1
DBCONNECTION = 0
DBCURSOR = 1
HEADER = 4
IJSONPREFIX = 0
IJSONTYPE = 1
IJSONVALUE = 2
NAME = 0
parmEndTime = 0
parmLimit = 1
parmOffset = 2
parmStartTime = 3
parmUrl01 = 4
parmUrl02 = 5
parmUrl03 = 6
parmUrl04 = 7
parmUrl05 = 8
QUERYEMPTY = 0
QUERYFROMPRESET = 1
QUERYLOADED = -1
TYPE = 3

# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * bottom cut for dictMaker #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#


DATAFIELDDEFAULTSSQLTUPL = (
	(RID, 0,),
	(propTimeZ, DFLTSTR,),
	(geoLat, 0.0,),
	(geoLon, 0.0,),
	(geoDepth, 0.0,),
	(propMag, 0.0,),
	(propMagType, DFLTSTR,),
	(propNumStations, 0,),
	(propMaxAzmGap, 0.0,),
	(propDegMinToStation, 0.0,),
	(propRMS, 0.0,),
	(propNetwork, DFLTSTR,),
	(eventID, DFLTSTR,),
	(propUpdatedZ, DFLTSTR,),
	(propPlace, DFLTSTR,),
	(propEventType, DFLTSTR,),
	(propHorizontalErr, 0.0,),
	(propDepthErr, 0.0,),
	(propMagErr, 0.0,),
	(propMagNST, 0,),
	(propStatus, DFLTSTR,),
	(propLocationSrc, DFLTSTR,),
	(propMagSrc, DFLTSTR,),
)


def DATAFIELDDEFAULTSSQL():
	return dict((x, y) for x, y in DATAFIELDDEFAULTSSQLTUPL)


DATAINNAMES = \
	[
		propTimeZ,
		geoLon,
		geoLat,
		geoDepth,
		propMag,
		propMagType,
		propNumStations,
		propMaxAzmGap,
		propDegMinToStation,
		propRMS,
		propNetwork,
		eventID,
		propUpdatedZ,
		propPlace,
		propEventType,
		propHorizontalErr,
		propDepthErr,
		propMagErr,
		propMagNST,
		propStatus,
		propLocationSrc,
		propMagSrc,
	]


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * mysql default string only, never works with anything except adding records
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
QUERIESINGLOBALDEFAULTSTUPLE = \
	(
		(RID, 0),
		(QUERIESINTITLE, ""),
		(QUERIESINRETURNTO, ""),
		(SQLSELECT, ""),
		(SQLWHERE, ""),
		(SQLGROUPBY, ""),
		(SQLHAVING, ""),
		(SQLORDERBY, ""),
		(SQLLIMIT, ""),
		(STARTRECNUM, 0),
		(QUERYNUM, 1),
		(NUMROWS, 0),
		(ROWNUM, 0),
		(REGION0NAME, ""),
		(REGION0DESCRIPTION, ""),
		(REGION0KMFROM, 0.0),
		(REGION0NORTH,  0.0),
		(REGION0WEST,  0.0),
		(REGION0SOUTH,  0.0),
		(REGION0EAST,  0.0),
		(REGION1NAME, ""),
		(REGION1DESCRIPTION, ""),
		(REGION1KMFROM, 0.0),
		(REGION1NORTH,  0.0),
		(REGION1WEST,  0.0),
		(REGION1SOUTH,  0.0),
		(REGION1EAST,  0.0),
		(REGION2NAME, ""),
		(REGION2DESCRIPTION, ""),
		(REGION2KMFROM, 0.0),
		(REGION2NORTH,  0.0),
		(REGION2WEST,  0.0),
		(REGION2SOUTH,  0.0),
		(REGION2EAST,  0.0),
		(REGION3NAME, ""),
		(REGION3DESCRIPTION, ""),
		(REGION3KMFROM, 0.0),
		(REGION3NORTH,  0.0),
		(REGION3WEST,  0.0),
		(REGION3SOUTH,  0.0),
		(REGION3EAST,  0.0),
		(PGNUM, 1),
		(OFPGS, 1),
		(ISLOADED, 0),
	)


def QUERIESINDEFAULTS():
	return dict((x, y) for x, y in QUERIESINGLOBALDEFAULTSTUPLE)


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * region names dict loaded /quakes and kept here as a psuedo constant
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
REGIONNAMESDICT = \
	{
		REGION0NAME: "",
		REGION1NAME: "",
		REGION2NAME: "",
		REGION3NAME: "",
	}
REGIONDESCRIPTIONSDICT = \
	{
		REGION0DESCRIPTION: "",
		REGION1DESCRIPTION: "",
		REGION2DESCRIPTION: "",
		REGION3DESCRIPTION: "",
	}


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * dict translating USGS GEOJSON to my field names as the entry is copied from myProperties  to myEventEntry
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
GEOJSONFIELDNAMES = \
	{
		"mag": propMag,
		"time": propTimeZ,
		"updated": propUpdatedZ,
		"tz": propTZLM,
		"url": propUrl,
		"detail": propDetailUrl,
		"felt": propFelt,
		"cdi": propCompDYFIIndex,
		"mmi": propMaxMeasuredIntensity,
		"alert": propAlert,
		"status": propStatus,
		"tsunami": propTsunami,
		"sig": propSignificanceIndex,
		"net": propNetwork,
		"code": propCode,
		"ids": propIDsUsed,
		"sources": propSourcesUsed,
		"types": propProductTypesUsed,
		"nst": propNumStations,
		"dmin": propDegMinToStation,
		"rms": propRMS,
		"gap": propMaxAzmGap,
		"magType": propMagType,
		"type": propEventType,
		"title": propTitle,
		"place": propPlace,
	}


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * tuple to create dict from for default SQL values
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
GEOJSONDEFENTRYSQL = \
	(
		(RID, 0),
		(eventID, DFLTSTR),
		(propPlace, DFLTSTR),
		(fileEntryRID, 0),
		(geoType, DFLTSTR),
		(geoLon, 0.0),
		(geoLat, 0.0),
		(geoDepth, 0.0),
		(featureType, DFLTSTR),
		(propMag, 0.0),
		(propTimeZ, DFLTSTR),
		(propUpdatedZ, DFLTSTR),
		(propTZLM, 0),
		(propUrl, DFLTSTR),
		(propDetailUrl, DFLTSTR),
		(propFelt, 0),
		(propCompDYFIIndex, 0),
		(propMaxMeasuredIntensity, 0.0),
		(propAlert, 0),
		(propStatus, DFLTSTR),
		(propTsunami, 0),
		(propSignificanceIndex, 0),
		(propNetwork, DFLTSTR),
		(propCode, DFLTSTR),
		(propIDsUsed, DFLTSTR),
		(propSourcesUsed, DFLTSTR),
		(propProductTypesUsed, DFLTSTR),
		(propNumStations, 0),
		(propDegMinToStation, 0.0),
		(propRMS, 0.0),
		(propMaxAzmGap, 0.0),
		(propMagType, DFLTSTR),
		(propEventType, DFLTSTR),
		(propTitle, DFLTSTR),
	)


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * make a default dict from the tuples above
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def GEOGJSONEVENTSDEFAULTSQL():
	return dict((x, y) for x, y in GEOJSONDEFENTRYSQL)


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * tuple to dict bits for file entries
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
GEOJSONFILEENTRYTUPLE = \
	(
		(RID, 0),
		(fileType, DFLTSTR),
		(metaGeneratedTime, DFLTSTR),
		(metaURL, DFLTSTR),
		(metaFileTitle, DFLTSTR),
		(metaFileStatus, 0),
		(metaAPI, DFLTSTR),
		(metaRecordCount, 0),
		(BBoxMinLon, 0.0),
		(BBoxMinLat, 0.0),
		(BBoxMinDepth, 0.0),
		(BBoxMaxLon, 0.0),
		(BBoxMaxLat, 0.0),
		(BBoxMaxDepth, 0.0),
	)


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * make a default dict from the tuples above
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def GEOJSONFILEENTRYEMPTYSQL():
	return dict((x, y) for x, y in GEOJSONFILEENTRYTUPLE)


def GETDEFQRID():
	global DEFQUERYNUM
	FDIn = open("""/home/will/.cache/earthquakesUSGS/defaultQueryNum.txt""", "r")
	DEFQUERYNUM = FDIn.read()
	FDIn.close()


def PUTDEFQRID():
	global DEFQUERYNUM
	FDOut = open("""/home/will/.cache/earthquakesUSGS/defaultQueryNum.txt""", "w")
	FDOut.write(str(DEFQUERYNUM))
	FDOut.close()


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
METADATAEMPTYTUPLE = \
	(
		(generated, metaGeneratedTime,),
		(url, metaURL,),
		(title, metaFileTitle,),
		(status, metaFileStatus,),
		(api, metaAPI,),
		(limit, metaLimit,),
		(offset, metaOffset,),
		(count, metaRecordCount,),
	)


def METADATAEMPTY():
	return dict((x, y) for x, y in METADATAEMPTYTUPLE)


BBOXEMPTYTUPLE = \
	(
		(BBMINLON, BBoxMinLon,),
		(BBMINLAT, BBoxMinLat,),
		(BBMINDEPTH, BBoxMinDepth,),
		(BBMAXLON, BBoxMaxLon,),
		(BBMAXLAT, BBoxMaxLat,),
		(BBMAXDEPTH, BBoxMaxDepth,),
	)


def BBOXEMPTY():
	return dict((x, y) for x, y in BBOXEMPTYTUPLE)


PREFIXEMPTYTUPLE = (
	(RID, MYDEFAULTSDICTSQL[RID],),
	(PFXfirstSeen, MYDEFAULTSDICTSQL[PFXfirstSeen],),
	(PFXlastSeen, MYDEFAULTSDICTSQL[PFXlastSeen],),
	(PFXDBTable, MYDEFAULTSDICTSQL[PFXDBTable],),
	(PFXfieldNameL, MYDEFAULTSDICTSQL[PFXfieldNameL],),
	(PFXfieldNameZ, MYDEFAULTSDICTSQL[PFXfieldNameZ],),
	(PFXprefixStr, MYDEFAULTSDICTSQL[PFXprefixStr],),
	(PFXkeyType, MYDEFAULTSDICTSQL[PFXkeyType],),
	(PFXdescription, MYDEFAULTSDICTSQL[PFXdescription],),
	(PFXyieldThis, MYDEFAULTSDICTSQL[PFXyieldThis],),
)


def PREFIXEMPTYDICT():
	return dict((x, y) for x, y in PREFIXEMPTYTUPLE)


GETDEFQRID()


#

