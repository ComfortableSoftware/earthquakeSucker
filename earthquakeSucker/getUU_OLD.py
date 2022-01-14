#!/usr/bin/python


import urllib3
import requests
import datetime
import subprocess as SP
import os
from sys import argv


numArgs = len(argv)
if numArgs == 2:
	numDays = int(argv.pop(1))
else:
	numDays = 1


timeStamps = \
	{
		"now": "",
		"nowStr": "",
		"nowTimeStr": "",
		"today": "",
		"todayStr": "",
		"yesterday": "",
		"yesterdayStr": "",
		"tomorrow": "",
		"tomorrowStr": "",
	}
outFilePath = "/rcr/3-backup/eq/"


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def fillDatesFromNow():
	global timeStamps

	timeStamps["now"] = datetime.datetime.now()
	timeStamps["nowStr"] = timeStamps["now"].strftime("%c")
	timeStamps["nowTimeStr"] = timeStamps["now"].strftime("%H%M%S")
	timeStamps["today"] = timeStamps["now"].today()
	timeStamps["todayStr"] = timeStamps["today"].strftime("%Y%m%d")
	timeStamps["yesterday"] = timeStamps["today"] + datetime.timedelta(days=-1)
	timeStamps["yesterdayStr"] = timeStamps["yesterday"].strftime("%Y%m%d")
	timeStamps["tomorrow"] = timeStamps["today"] + datetime.timedelta(days=1)
	timeStamps["tomorrowStr"] = timeStamps["tomorrow"].strftime("%Y%m%d")


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def fillDatesFromYesterday():
	global timeStamps

	timeStamps["now"] = timeStamps["yesterday"]
	timeStamps["nowStr"] = timeStamps["now"].strftime("%c")
	timeStamps["nowTimeStr"] = timeStamps["now"].strftime("%H%M%S")
	timeStamps["today"] = timeStamps["now"].today()
	timeStamps["todayStr"] = timeStamps["today"].strftime("%Y%m%d")
	timeStamps["yesterday"] = timeStamps["today"] + datetime.timedelta(days=-1)
	timeStamps["yesterdayStr"] = timeStamps["yesterday"].strftime("%Y%m%d")
	timeStamps["tomorrow"] = timeStamps["today"] + datetime.timedelta(days=1)
	timeStamps["tomorrowStr"] = timeStamps["tomorrow"].strftime("%Y%m%d")


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def fillDatesFromTomorrow():
	global timeStamps

	timeStamps["now"] = timeStamps["tomorrow"]
	timeStamps["nowStr"] = timeStamps["now"].strftime("%c")
	timeStamps["nowTimeStr"] = timeStamps["now"].strftime("%H%M%S")
	timeStamps["today"] = timeStamps["now"].today()
	timeStamps["todayStr"] = timeStamps["today"].strftime("%Y%m%d")
	timeStamps["yesterday"] = timeStamps["today"] + datetime.timedelta(days=-1)
	timeStamps["yesterdayStr"] = timeStamps["yesterday"].strftime("%Y%m%d")
	timeStamps["tomorrow"] = timeStamps["today"] + datetime.timedelta(days=1)
	timeStamps["tomorrowStr"] = timeStamps["tomorrow"].strftime("%Y%m%d")


TDestDir = "/home/will/.cache/earthquakesUU/"
finalDestDir = "/storage/zz_toburn/eq/"
myStations = \
	[
		"BMUT_EHZ_UU",
		"CTU_SHZ_UU",
		"GMU_EHZ_UU",
		"GZU_EHZ_UU",
		"HVU_SHZ_UU",
		"MPU_SHZ_UU",
		"MSU_EHZ_UU",
		"NAIU_EHZ_UU",
		"VEC_SNZ_UU",
	]



def getStations():
	global timeStamps
	for thisStation in myStations:
		urllib3.disable_warnings()
		thisUrl = "https://quake.utah.edu/station/heli2/" + timeStamps["yesterdayStr"] + "/" + thisStation + "_01-"
		thisUrl += timeStamps["yesterdayStr"] + ".png"
		thisFilename = TDestDir + thisStation + "_01-" + timeStamps["yesterdayStr"] + ".png"
		with open(thisFilename, "wb") as f:
			response = requests.get(thisUrl, verify=False)
			f.write(response.content)
			f.flush()
			f.close()


def makeArchive(outFilename):
	execSet = ["/usr/bin/7z", "a", outFilename, TDestDir, "-m0=lzma2:a1", "-mx=9", "-l",]
	result = SP.run(execSet, capture_output=True)

	if result.returncode == 0:
		execSet = ["/usr/bin/par2", "c", "-r20", outFilename + "-pars", outFilename]
		result = SP.run(execSet, capture_output=True)

		if result.returncode == 0:
			for thisDir in os.walk(TDestDir):
				for thisFile in thisDir[2]:
					os.remove(TDestDir + thisFile)
		else:
			print(f"an error occurred making par2 files\nreturn code: {result.returncode}")
			print(f"nargs:{result.args}")
			print(f"stdout:{result.stdout}")
			print(f"stderr:{result.stderr}")

	else:
		print(f"an error occurred making archive\nreturn code: {result.returncode}")
		print(f"nargs:{result.args}")
		print(f"stdout:{result.stdout}")
		print(f"stderr:{result.stderr}")

def __main__():
	getStations()
	myFName = outFilePath + timeStamps["yesterdayStr"] + "."
	myFName += timeStamps["todayStr"] + "." + timeStamps["nowTimeStr"] + ".7z"
	makeArchive(myFName)


if __name__ == "__main__":
	fillDatesFromNow()

	if numDays == 1:
		__main__()
	else:

		for TI1 in range(numDays):
			fillDatesFromYesterday()
			__main__()
