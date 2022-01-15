

import DBStuff
from dataStuff import constants as C
from dataStuff import dataStuff as DS


DB = DBStuff
DBCONN = DB.doOpen(C.SQLCONFIG)

DB.dropTableIfExists(DBCONN, C.DATATABLENAME)
SQLStr = DB.makeTableStr(C.DATATABLENAME, C.DATAFIELDNAMES, C.MYFIELDTYPESDICT)
SQLRows = DB.doSqlAll(DBCONN, SQLStr)
if SQLRows:
	outStr = DS.getDebugInfo("SQLRows")
	print(f"{outStr}{repr(SQLRows)})")
	outStr = DS.getDebugInfo("SQLStr")
	print(f"{outStr}{repr(SQLStr)})")
	exit(1)

SQLStr = f"create index\nif not exists 'XEQID'\non {C.DATATABLENAME}(EQID)"
SQLRows = DB.doSqlAll(DBCONN, SQLStr)
if SQLRows:
	outStr = DS.getDebugInfo("SQLRows")
	print(f"{outStr}{repr(SQLRows)})")
	outStr = DS.getDebugInfo("SQLStr")
	print(f"{outStr}{repr(SQLStr)})")
	exit(1)

DB.dropTableIfExists(DBCONN, C.STATSTABLENAME)
SQLStr = DB.makeTableStr(C.STATSTABLENAME, C.STATSFIELDNAMES, C.STATSFIELDTYPES)
SQLRows = DB.doSqlAll(DBCONN, SQLStr)
if SQLRows:
	outStr = DS.getDebugInfo("SQLRows")
	print(f"{outStr}{repr(SQLRows)})")
	outStr = DS.getDebugInfo("SQLStr")
	print(f"{outStr}{repr(SQLStr)})")
	exit(1)
