#!/usr/bin/env /usr/bin/python


from earthquakeSucker import getGeoJson_C

help(getGeoJson_C)
with getGeoJson_C.flipIt() as GGJ:
  help(GGJ)
