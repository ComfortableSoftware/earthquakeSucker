

from datetime import datetime as DT
from datetime import timedelta as TD
from time import mktime as MT
from dateutil import tz as TZ
from dateutil import parser as PD
from dateutil.relativedelta import relativedelta as RD



def TS2ISO(TSIn):
	if isinstance(TSIn, str):
		return DT.strftime(PD.parse(TSIn, "%Y-%m-%d %H:%M:%S"))
	elif isinstance(TSIn, int):
		return DT.fromtimestamp(TSIn, "%Y-%m-%d %H:%M:%S")
	parsedStr = PD.parse(ISOStrIn).strftime("%Y-%m-%d %H:%M:%S")
	thisTime = MT(PD.parse(TSIn, "%Y-%m-%d %H:%M:%S"))


print(TS2ISO("1964-03-10 12:27:00"))

MYFIELDTYPESDICT = \
	{
		CEQID: "int",
		CRID: "int",
		DEPTHERROR: "decimal",
		DMIN: "decimal",
		EQID: "varchar",
		EVENTDEPTH: "int",
		eventID: "varchar",
		EVENTSTATUS: "varchar",
		EVENTTYPE: "varchar",
		featureType: "varchar",
		fileApiVersion: "varchar",
		fileBBoxMaxDepth: "decimal",
		fileBBoxMaxLat: "decimal",
		fileBBoxMaxLon: "decimal",
		fileBBoxMinDepth: "decimal",
		fileBBoxMinLat: "decimal",
		fileBBoxMinLon: "decimal",
		fileEntryRID: "int",
		fileMetaGeneratedTime: "datetime",
		fileRecordCount: "int",
		fileStatus: "int",
		fileTitle: "varchar",
		fileType: "varchar",
		fileUrl: "varchar",
		GAP: "decimal",
		geoDepth: "decimal",
		geoLat: "decimal",
		geoLon: "decimal",
		geoType: "varchar",
		HORIZONTALERROR: "decimal",
		KMFROM: "float",
		KMFROMHM: "float",
		LATITUDE: "LAT",
		LOCATIONSOURCE: "varchar",
		LONGITUDE: "LON",
		MAGNITUDE: "decimal",
		MAGNITUDEERROR: "decimal",
		MAGNITUDESOURCE: "varchar",
		MAGNITUDETYPE: "varchar",
		MAGNST: "int",
		NETWORK: "varchar",
		NST: "decimal",
		PLACE: "varchar",
		propAlert: "int",
		propCode: "varchar",
		propCompDYFIIndex: "int",
		propDegMinToStation: "decimal",
		propDetailUrl: "varchar",
		propEventType: "varchar",
		propFelt: "int",
		propIDsUsed: "varchar",
		propMag: "decimal",
		propMagType: "varchar",
		propMaxAzmGap: "decimal",
		propMaxMeasuredIntensity: "decimal",
		propNetwork: "varchar",
		propNumStations: "int",
		propPlace: "varchar",
		propProductTypesUsed: "varchar",
		propRMS: "decimal",
		propSignificanceIndex: "int",
		propSourcesUsed: "varchar",
		propStatus: "varchar",
		propTimeZ: "datetime",
		propTitle: "varchar",
		propTsunami: "int",
		propTZLM: "int",
		propUpdatedZ: "datetime",
		propUrl: "varchar",
		RID: "int",
		RMS: "decimal",
		SINCETIMEL: "datetime",
		SINCETIMEZ: "datetime",
		SINCEUPDATEDL: "datetime",
		SINCEUPDATEDZ: "datetime",
		TIMEL: "datetime",
		TIMEZ: "datetime",
		UPDATEDL: "datetime",
		UPDATEDZ: "datetime",
	}

