

from DBStuff import DBStuff as DB

RID = "RID"
myKey = "myKey"
prefix = "prefix"
keyType = "keyType"
description ="description"
sampleData = "sampleData"

# * D)details
# * Q)query details
# * d)day
# * h)hour
# * L)list of eventID to process
# * m)month
# * q)query
# * w)week
# * f)file
# * I)eventID

O_ALLDAYSMRY = "ALLDAYSMRY"
O_ALLHOURSMRY = "ALLHOURSMRY"
O_ALLMONTHSMRY = "ALLMONTHSMRY"
O_ALLWEEKSMRY = "ALLWEEKSMRY"
O_DETAILS = "DETAILS"
O_EVENTID = "EVENTID"
O_EVENTIDLIST = "EVENTIFLIST"
O_FILE = "FILE"
O_QUERY = "QUERY"
O_QUERYDETAILS = "QUERYDETAILS"


OPTSTDICT = {
	"-D": O_DETAILS,
	"-I": O_EVENTID,
	"-Q": O_QUERYDETAILS,
	"-d": O_ALLDAYSMRY,
	"-f": O_FILE,
	"-h": O_ALLHOURSMRY,
	"-L": O_EVENTIDLIST,
	"-m": O_ALLMONTHSMRY,
	"-q": O_QUERY,
	"-w": O_ALLWEEKSMRY,
}

OPTSTTUPLE = (
	(O_ALLDAYSMRY, ""),
	(O_ALLHOURSMRY, ""),
	(O_ALLMONTHSMRY, ""),
	(O_ALLWEEKSMRY, ""),
	(O_DETAILS, ""),
	(O_EVENTID, ""),
	(O_EVENTIDLIST, ""),
	(O_FILE, ""),
	(O_QUERY, ""),
	(O_QUERYDETAILS, ""),
)


def OPTSTTDICT(optsIn):
	dictToRtn = dict((x, y) for x, y in OPTSTTUPLE)
	for anOPT in optsIn:
		try:
			myLeft = anOPT[0]
			myRight = anOPT[1]
			dictToRtn[OPTSTDICT[myLeft]] = myRight
		except KeyError:
			continue
	return dictToRtn


ARGSTDICT = {
	"-I": O_EVENTID,
}


ARGSTTUPLE = (
	(O_EVENTID, "",),
)


def ARGSTTDICT(optsIn):
	dictToRtn = dict((x, y) for x, y in ARGSTTUPLE)
	for anOPT in optsIn:
		try:
			myLeft = anOPT[0]
			myRight = anOPT[1]
			dictToRtn[ARGSTDICT[myLeft]] = myRight
		except KeyError:
			continue
	return dictToRtn


#

