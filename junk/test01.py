

from dataStuff import constants as C
from DBStuff import DBStuff as DB

DBLinks = DB.doOpen(C.SQLCONFIG)

# SQLRows = DBLinks[C.DBCURSOR].fetchall()

# DBLinks[C.DBCONNECTION].handle_unread_result()
SQLStr = f"""select EQID, count(EQID) as CEQID from USGSData where PLACE like "%Utah%";"""

SQLRows = DB.getSqlAll(DBLinks, SQLStr)
if SQLRows:
	for key, value in SQLRows.items():
		print(f"{key}: {value},", end=" ")
	print("")


DB.doClose(DBLinks)


