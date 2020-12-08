import urllib3
import requests


from dataStuff import constants as C
from dataStuff import timeDateStuff as TDS


def getAFile(URL, filename, isJson=False, dirPfx=""):
	urllib3.disable_warnings()
	with open(filename, "wb") as FIN:
		responseObj = requests.get(URL, verify=False)
		responseCode = responseObj.status_code
		if isJson and responseCode == 222:
			responseJson = responseObj.json()
			FDOut = open(f"""{C.CACHEDIR(f"{dirPfx}response.{TDS.nowStr(TDS.DT.now())}.json")}""", "w")
			FDOut.write(repr(responseJson))
			FDOut.flush()
			FDOut.close()
		# responseHeaders = responseObj.headers
		# FDOut = open(f"""{C.CACHEDIR(f"headers.{TDS.nowStr(TDS.DT.now())}.html")}""", "w")
		# FDOut.write(repr(responseHeaders))
		# FDOut.flush()
		# FDOut.close()
		print(f"""
url {URL}
filename {filename}
response code {str(responseCode)}
""")

		FIN.write(responseObj.content)
		FIN.flush()
		FIN.close()
	if responseCode != 200:
		return False
	return True


def jsonSplitAFile(filename):
	FDIn = open(filename, "tr")
	newFilename = f"""{filename}L"""
	FDOut = open(newFilename, "w")
	while True:
		INBLK = FDIn.read(2000)
		if INBLK == "":
			FDOut.flush()
			FDOut.close()
			return newFilename
		for INCH in INBLK:
			if INCH in C.JSONOBRACKETS or INCH in C.JSONCBRACKETS:
				INCH = C.NEWLINE + INCH + C.NEWLINE
			else:
				FDOut.flush()
				FDOut.close()
				return newFilename
			FDOut.write(INCH)
		FDOut.flush()
