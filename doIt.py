#!/usr/bin/env /usr/bin/python



from CF.SUBM_D import _00_DEBUG as DBG
from earthquakeSucker import USGS_C


def main():
  with USGS_C.USGS_C() as GGJ:
    GGJ.getAFile()
    GGJ.parseAFile()

main()
