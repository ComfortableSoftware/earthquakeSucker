

import datedelta
import datetime
from datetime import datetime as DT
from datetime import timedelta as TD
from time import mktime as MT
from dateutil import tz as TZ
from dateutil import parser as PD
from dateutil.relativedelta import relativedelta as RD
# from time import sleep

from dataStuff import dataStuff as DS
from dataStuff import constants as C


def now():
	return DT.now()


def nowZ():
	return DT.utcnow()


def nowStr(dtObj=DT.now()):
	return dtObj.strftime("%Y%m%d.%H%M%S")


def nowZStr(dtObj=DT.utcnow()):
	return dtObj.strftime("%Y%m%d.%H%M%S")


def nowZStrSql(dtObj=DT.utcnow()):
	return dtObj.strftime("%Y-%m-%d %H:%M:%S")


def nowStrSql(dtObj=DT.now()):
	return dtObj.strftime("%Y-%m-%d %H:%M:%S")


def nowTimeStr(dtObj=DT.now()):
	return dtObj.strftime("%H%M%S")


def today():
	return DT.today()


def todayStr(dtObj=DT.today()):
	return dtObj.strftime("%Y%m%d")


def yesterday(dtObj=DT.today()):
	return dtObj + TD(days=-1)


def yesterdayStr(dtObj=yesterday(DT.today())):
	return dtObj.strftime("%Y%m%d")


def tomorrow(dtObj=today()):
	return dtObj + TD(days=1)


def tomorrowStr(dtObj=tomorrow()):
	return dtObj.strftime("%Y%m%d")


def gmdate(dtObj=DT.now()):
	return dtObj.strftime('D, d M Y H:i:s GMT')


def toStr(TDIn):
	if isinstance(TDIn, str):
		return TDIn
	else:
		return TDIn.strftime("%Y-%m-%d %H:%M:%S")


def ISO2TS(ISOStrIn):
	return MT(DT.strptime(ISOStrIn, "%Y-%m-%d %H:%M:%S").timetuple())


def TS2ISO(TSIn):
	if isinstance(TSIn, str):
		thisTime = PD.parse(TSIn).strftime("%Y-%m-%d %H:%M:%S")
	elif isinstance(TSIn, int):
		thisTime = DT.fromtimestamp(TSIn / 1000).strftime("%Y-%m-%d %H:%M:%S")
	return thisTime
	# elif isinstance(TSIn, int):
	#	return DT.fromtimestamp(TSIn, "%Y-%m-%d %H:%M:%S")

	return None


def timeHoler(timeStr):
	start = DT.strptime(PD.parse(timeStr), '%Y-%m-%d %H:%M:%S')
	parsedStr = PD.parse(ISOStrIn).strftime("%Y-%m-%d %H:%M:%S")


def USGS2MysqlTime(USGSDate):
	tdt1 = PD.parse(USGSDate)
	return tdt1.strftime("%Y-%m-%d %H:%M:%S")
	if USGSDate[10] != "T":
		return USGSDate
	TDString = USGSDate[:-5]
	TDate = DT.strptime(TDString, "%Y-%m-%dT%H:%M:%S")
	return TDate.strftime("%Y-%m-%d %H:%M:%S")


def mysql2LocalTime(SQLTIMEZ):
	if SQLTIMEZ[10] == "T":
		SQLTIMEZ = SQLTIMEZ[0:9] + " " + SQLTIMEZ[10:-5]
	if C.DEBUGME:
		print(f"timeDateStuff.42 TDString {SQLTIMEZ:s}")
	fromZone = TZ.gettz('UTC')
	toZone = TZ.gettz('MST7MDT')
	TDate = DT.strptime(SQLTIMEZ, "%Y-%m-%d %H:%M:%S")
	TDate = TDate.replace(tzinfo=fromZone)
	localTDate = TDate.astimezone(toZone)
	if C.DEBUGME:
		print(f"timeDateStuff.49 localTDate {localTDate.strftime('%Y-%m-%d %H:%M:%S'):s}")
	return f"{localTDate.strftime('%Y-%m-%d %H:%M:%S'):s}"


def USGS2LocalTime(usgsTimeZ):
	TDString = usgsTimeZ[:-5]
	if C.DEBUGME:
		print(f"timeDateStuff.42 TDString {TDString:s}")
	fromZone = TZ.gettz('UTC')
	toZone = TZ.gettz('MST7MDT')
	TDate = DT.strptime(TDString, "%Y-%m-%dT%H:%M:%S")
	TDate = TDate.replace(tzinfo=fromZone)
	localTDate = TDate.astimezone(toZone)
	if C.DEBUGME:
		print(f"timeDateStuff.49 localTDate {localTDate.strftime('%Y-%m-%d %H:%M:%S'):s}")
	return f"{localTDate.strftime('%Y-%m-%d %H:%M:%S'):s}"


def dateToStr(dateIn):
	if isinstance(dateIn, str):
		return dateIn
	returnStr = dateIn.strftime('%Y-%m-%d %H:%M:%S')
	return returnStr


def relDateDiff(startTS, endTS):
	if isinstance(startTS, str):
		start = DT.strptime(nowZStrSql(PD.parse(startTS)), '%Y-%m-%d %H:%M:%S')
	elif isinstance(startTS, int):
		start = DT.strptime(startTS, '%Y-%m-%d %H:%M:%S')
	else:
		return None
	if isinstance(endTS, str):
		ends = DT.strptime(nowZStrSql(PD.parse(endTS)), '%Y-%m-%d %H:%M:%S')
	elif isinstance(endTS, int):
		ends = DT.strptime(endTS, '%Y-%m-%d %H:%M:%S')
	else:
		return None
	diff = RD(start, ends)
	return f"{diff.years:04d}-{diff.months:02d}-{diff.days:02d} {diff.hours:02d}:{diff.minutes:02d}:{diff.seconds:02d}"


def relDateDiffStripped(startTS, endTS):
	startTS = DS.justTheNumbers(startTS)
	endTS = DS.justTheNumbers(endTS)
	start = DT.strptime(startTS, '%Y%m%d%H%M%S')
	ends = DT.strptime(endTS, '%Y%m%d%H%M%S')
	diff = RD(start, ends)
	return f"{diff.years:04d}{diff.months:02d}{diff.days:02d}{diff.hours:02d}{diff.minutes:02d}{diff.seconds:02d}"


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def dateIntvlM(dateToUse, months):
	if isinstance(dateToUse, str):
		dateToUseA = PD(dateToUse)
	elif isinstance(dateToUse, datetime.datetime):
		dateToUseA = dateToUse
	dateToRet = dateToUseA + datedelta.MONTH(months=months)
	if isinstance(dateToUse, str):
		dateToRet = DT.strftime("%Y-%m%d %H:%M:%S")
	return dateToRet

#

