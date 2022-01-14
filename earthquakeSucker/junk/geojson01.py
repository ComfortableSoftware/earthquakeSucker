


import gc
import geojson as GJ


gc.enable()


FDOut = open("reimagine.txt", "w")
emptyDict = {}
with open("geojson/all_month.geojson", "r") as FIn:
	GJLI = GJ.load(FIn)
	for entry in GJLI["features"]:
		for key, value in entry.items():
			emptyDict[key] = value
FDOut.write(f"""{str(emptyDict)}""")
FDOut.flush()
FDOut.close()

