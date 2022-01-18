

DROP DATABASE IF EXISTS `GJ_data`;
CREATE DATABASE `GJ_data` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;
USE `GJ_data`;


DROP TABLE IF EXISTS `GJ_enumerated`;
CREATE TABLE `GJ_enumerated` (
  `RID` int(11) NOT NULL AUTO_INCREMENT,
  `itemType` VARCHAR(50) COLLATE utf8mb4_unicode_ci DEFAULT "",
  `entryName` VARCHAR(50) COLLATE utf8mb4_unicode_ci DEFAULT "",
  `description` VARCHAR(200) COLLATE utf8mb4_unicode_ci DEFAULT "",
  PRIMARY KEY (`RID`),
  KEY `itemType` (`itemType`),
  KEY `typeEntry` (`itemType`, `entryName`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


DROP TABLE IF EXISTS `GJ_events`;
CREATE TABLE `GJ_events` (
  `RID` int(11) NOT NULL AUTO_INCREMENT,
  `detailRID` int(11) DEFAULT 0,
  `eventID` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT "",
  `featureType` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT "",
  `fileEntryRID` int(11) DEFAULT 0,
  `geoDepth` decimal(40,20) DEFAULT 0.0,
  `geoHomeLat` decimal(40,20) default 41.0,
  `geoHomeLon` decimal(40,20) default -112.0,
  `geoKMFROMHM` decimal(40,20) GENERATED ALWAYS AS ((atan2(sqrt(pow(cos(radians(`geoHomeLat`)) * sin(radians(`geoHomeLon`) - radians(geoLon)), 2) + pow(cos(radians(`geoLat`)) * sin(radians(`geoHomeLat`)) - sin(radians(`geoLat`)) * cos(radians(`geoHomeLat`)) * cos(radians(`geoHomeLon`) - radians(geoLon)), 2)), sin(radians(`geoLat`)) * sin(radians(`geoHomeLat`)) + cos(radians(`geoLat`)) * cos(radians(`geoHomeLat`)) * cos(radians(`geoHomeLon`) - radians(geoLon)))) * 6371) STORED,
  `geoLat` decimal(40,20) DEFAULT 0.0,
  `geoLon` decimal(40,20) DEFAULT 0.0,
  `geoType` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT "",
  `propAlert` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT "",
  `propCode` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT "",
  `propCompDYFIIndex` int(11) DEFAULT 0,
  `propDegMinToStation` decimal(40,20) DEFAULT 0.0,
  `propDepthErr` decimal(40,20) DEFAULT 0.0,
  `propDetailUrl` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT "",
  `propEventType` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT "",
  `propFelt` int(11) DEFAULT 0,
  `propIDsUsed` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT "",
  `propMagType` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT "",
  `propMag` decimal(40,20) DEFAULT 0.0,
  `propMaxAzmGap` decimal(40,20) DEFAULT 0.0,
  `propMaxMeasuredIntensity` decimal(40,20) DEFAULT 0.0,
  `propNetwork` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT "",
  `propNumStations` int(11) DEFAULT 0,
  `propPlace` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT "",
  `propProductTypesUsed` varchar(300) COLLATE utf8mb4_unicode_ci DEFAULT "",
  `propRMS` decimal(40,20) DEFAULT 0.0,
  `propSignificanceIndex` int(11) DEFAULT 0,
  `propSourcesUsed` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT "",
  `propStatus` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT "",
  `propTimeZ` datetime DEFAULT NULL,
  `propTitle` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT "",
  `propTsunami` int(11) DEFAULT 0,
  `propTZLM` int(11) DEFAULT 0,
  `propUpdatedZ` datetime DEFAULT NULL,
  `propUrl` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT "",
  PRIMARY KEY (`RID`),
  KEY `eventID` (`eventID`),
  KEY `propPlace` (`propPlace`),
  KEY `propIDsUsed` (`propIDsUsed`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


DROP TABLE IF EXISTS `GJ_files`;
CREATE TABLE `GJ_files` (
  `RID` int(11) NOT NULL AUTO_INCREMENT,
  `BBoxMaxDepth` decimal(40,20) DEFAULT 0.0,
  `BBoxMaxLat` decimal(40,20) DEFAULT 0.0,
  `BBoxMaxLon` decimal(40,20) DEFAULT 0.0,
  `BBoxMinDepth` decimal(40,20) DEFAULT 0.0,
  `BBoxMinLat` decimal(40,20) DEFAULT 0.0,
  `BBoxMinLon` decimal(40,20) DEFAULT 0.0,
  `fileType` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT "",
  `metaAPI` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT "",
  `metaFileStatus` int(11) DEFAULT 0,
  `metaFileTitle` text COLLATE utf8mb4_unicode_ci DEFAULT "",
  `metaGeneratedTime` datetime DEFAULT NULL,
  `metaLimit` int(11) DEFAULT 0,
  `metaOffset` int(11) DEFAULT 0,
  `metaRecordCount` int(11) DEFAULT 0,
  `metaURL` text COLLATE utf8mb4_unicode_ci DEFAULT "",
  PRIMARY KEY (`RID`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


DROP TABLE IF EXISTS `GJ_queries`;
CREATE TABLE `GJ_queries` (
  `RID` int(11) NOT NULL AUTO_INCREMENT,
  `QUERIESINTITLE` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT "",
  `QUERIESINRETURNTO` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT "",
  `SQLSELECT` text COLLATE utf8mb4_unicode_ci DEFAULT "",
  `SQLWHERE` text COLLATE utf8mb4_unicode_ci DEFAULT "",
  `SQLGROUPBY` text COLLATE utf8mb4_unicode_ci DEFAULT "",
  `SQLHAVING` text COLLATE utf8mb4_unicode_ci DEFAULT "",
  `SQLORDERBY` text COLLATE utf8mb4_unicode_ci DEFAULT "",
  `SQLLIMIT` text COLLATE utf8mb4_unicode_ci DEFAULT "",
  `REGION0NAME` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT "",
  `REGION0DESCRIPTION` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT "",
  `REGION0KMFROM` decimal(8,2) DEFAULT 0.0,
  `REGION0NORTH` float DEFAULT 0.0,
  `REGION0WEST` float DEFAULT 0.0,
  `REGION0SOUTH` float DEFAULT 0.0,
  `REGION0EAST` float DEFAULT 0.0,
  `REGION1NAME` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT "",
  `REGION1DESCRIPTION` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT "",
  `REGION1KMFROM` decimal(8,2) DEFAULT 0.0,
  `REGION1NORTH` float DEFAULT 0.0,
  `REGION1WEST` float DEFAULT 0.0,
  `REGION1SOUTH` float DEFAULT 0.0,
  `REGION1EAST` float DEFAULT 0.0,
  `REGION2NAME` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT "",
  `REGION2DESCRIPTION` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT "",
  `REGION2KMFROM` decimal(8,2) DEFAULT 0.0,
  `REGION2NORTH` float DEFAULT 0.0,
  `REGION2WEST` float DEFAULT 0.0,
  `REGION2SOUTH` float DEFAULT 0.0,
  `REGION2EAST` float DEFAULT 0.0,
  `REGION3NAME` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT "",
  `REGION3DESCRIPTION` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT "",
  `REGION3KMFROM` decimal(8,2) DEFAULT 0.0,
  `REGION3NORTH` float DEFAULT 0.0,
  `REGION3WEST` float DEFAULT 0.0,
  `REGION3SOUTH` float DEFAULT 0.0,
  `REGION3EAST` float DEFAULT 0.0,
  PRIMARY KEY (`RID`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
