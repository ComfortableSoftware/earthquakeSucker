

import gc
import geojson as GJ
from collections.abc import Iterable as IT


from dataStuff import constants as C


gc.enable()
levelOfIndent = 0


def doIterableRight(myIterable):
	global levelOfIndent
	if isinstance(myIterable, str):
		return
	if isinstance(myIterable, dict):
		for key, value in myIterable.items():
			if isinstance(myIterable[key], IT) and not isinstance(myIterable[key], str):
				FDOut.write(f"""{C.INDENTIN}{levelOfIndent:03d} {key}:{C.INDENTIN}iter 
			""")
				levelOfIndent += 1
				doIterableRight(myIterable[key])
			else:
				FDOut.write(f"""{key}: {value}
""")
		FDOut.write(f"""{C.INDENTOUT}{levelOfIndent:03d}{C.INDENTOUT}dict
""")
	elif isinstance(myIterable, list):
		levelOfIndent += 1
		for key, value in enumerate(myIterable):
			if isinstance(myIterable[key], IT) and not isinstance(myIterable[key], str):
				FDOut.write(f"""{C.INDENTIN}{levelOfIndent:03d} {key}:{C.INDENTIN}
""")
				doIterableRight(myIterable[key])
			else:
				FDOut.write(f"""{key}: {value}
""")
		FDOut.write(f"""{C.INDENTOUT}{levelOfIndent:03d}{C.INDENTOUT}list
""")
		levelOfIndent -= 1
	elif isinstance(myIterable, tuple):
		levelOfIndent += 1
		for key, value in enumerate(myIterable):
			if isinstance(myIterable[key], IT) and not isinstance(myIterable[key], str):
				FDOut.write(f"""{C.INDENTIN}{levelOfIndent:03d} {key}:{C.INDENTIN}iter
""")
				doIterableRight(GJLI[key])
			else:
				FDOut.write(f"""{key}: {value}
""")
		FDOut.write(f"""{C.INDENTOUT}{levelOfIndent:03d}{C.INDENTOUT}tuple
""")
		levelOfIndent -= 1



FDOut = open("reimagine.txt", "w")
with open("geojson/all_hour.geojson", "r") as FIn:
	GJLI = GJ.load(FIn)
	for keyRoot, valueRoot in GJLI.items():
		FDOut.write(f"""{keyRoot}:{C.INDENTIN}
""")
		if isinstance(GJLI[keyRoot], IT) and not isinstance(GJLI[keyRoot], str):
			FDOut.write(f"""{keyRoot}:{levelOfIndent}{C.INDENTIN}
""")
			doIterableRight(GJLI[keyRoot])
			FDOut.write(f"""{keyRoot}:{levelOfIndent}{C.INDENTOUT}
""")
		else:
			FDOut.write(f"""{keyRoot}: {valueRoot}
""")

FDOut.flush()
FDOut.close()

