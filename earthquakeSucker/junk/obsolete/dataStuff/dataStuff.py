import inspect
import math
from re import sub as SUB
import os


PATH = os.path
ABSPATH = os.path.abspath


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def getDebugInfo(varListed):
  previous_frame = inspect.currentframe().f_back
  (filename, line_number, function_name, lines, index) = inspect.getframeinfo(previous_frame)
  return f"file {filename}, line {line_number}, function {function_name}\n{varListed}\n"


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def dictToLine(dictIn):

  if not dictIn:
    return None

  returnStr = ""

  for key, value in dictIn.items():
    returnStr += f"{key}: '{value}', "

  returnStr = returnStr[:-2] + "\n"
  return returnStr


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *Vincenti's.'s great circle distance calculator with defaults to home for lat/lon to
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def vGreatCircleDistance(lat1, lon1, lat2=40.687088, lon2=-111.927630, earthRadius=6371):  # 3959 for miles 6371 for km
  # convert from degrees to radians
  latFrom = math.radians(lat1)
  lonFrom = math.radians(lon1)
  latTo = math.radians(lat2)
  lonTo = math.radians(lon2)

  lonDelta = lonTo - lonFrom
  a = pow(math.cos(latTo) * math.sin(lonDelta), 2) + pow(math.cos(latFrom) * math.sin(latTo) - math.sin(latFrom) * math.cos(latTo) * math.cos(lonDelta), 2)
  b = math.sin(latFrom) * math.sin(latTo) + math.cos(latFrom) * math.cos(latTo) * math.cos(lonDelta)

  angle = math.atan2(math.sqrt(a), b)
  return angle * earthRadius


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * haversine formula for GCD
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def GCdistance(lat1, lon1, lat2, lon2, unit):
  theta = lon1 - lon2
  sinRadLat2 = math.sin(math.radians(lat2))
  cosRadLat2 = math.cos(math.radians(lat2))
  cosRadLat1 = math.cos(math.radians(lat1))
  sinRadLat1 = math.sin(math.radians(lat1))
  cosRadTheta = math.cos(math.radians(theta))
  dist = sinRadLat1 * sinRadLat2 + cosRadLat1 * cosRadLat2 * cosRadTheta
  dist = math.cos(dist)
  dist = math.degrees(dist)
  miles = dist * 60 * 1.1515
  unit = unit.upper()

  if unit == "K":
    return miles * 1.609344
  elif unit == "N":
    return miles * 0.8684
  else:
    return miles


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def justTheNumbers(relDateStr):
  blackList = "[^0-9]+"
  thisWhiteReturn = SUB(blackList, "", relDateStr)
  return thisWhiteReturn
