

from dataStuff import constants as C
import DBStuff as DB


DBLinks = DB.doOpen(C.SQLCONFIG)
SQLStr = """select count(RID), propTimeZ, propMag, min(propTimeZ), max(propTimeZ), max(propMag) from USGSData
where propPlace like "%Utah%"
order by propTimeZ desc, propUpdatedZ desc
limit 20
"""
SQLRETURN, rowsAffected = DB.getSqlAll(DBLinks, SQLStr)
numRowsAffected = len(SQLRETURN)
print(f"{rowsAffected}")
DB.doClose(DBLinks)

