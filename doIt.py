#!/usr/bin/env /usr/bin/python


from earthquakeSucker import USGS_C

with USGS_C.USGS_C() as GGJ:
  GGJ.getAFile()
  GGJ.parseAFile()
