#!/usr/bin/env /usr/bin/python


from earthquakeSucker import getGeoJson_C

with getGeoJson_C.USGS_C() as GGJ:
  GGJ.getAFile()
  GGJ.parseAFile()
