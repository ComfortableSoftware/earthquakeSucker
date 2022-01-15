

DROP DATABASE IF EXISTS `GJ_data`;
CREATE DATABASE `GJ_data` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;
USE `GJ_data`;


DROP TABLE IF EXISTS `GJ_enumerated`;
CREATE TABLE `GJ_enumerated` (
  `RID` int(11) NOT NULL AUTO_INCREMENT,
  `itemType` VARCHAR(50) COLLATE utf8mb4_unicode_ci DEFAULT "",
  `entryName` VARCHAR(50) COLLATE utf8mb4_unicode_ci DEFAULT "",
  PRIMARY KEY (`RID`),
  KEY `itemType` (`itemType`),
  KEY `typeEntry` (`itemType`, `entryName`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


DROP TABLE IF EXISTS `GJ_events`;
CREATE TABLE `GJ_events` (
  `RID` int(11) NOT NULL AUTO_INCREMENT,
  `detailRID` int(11) DEFAULT NULL,
  `eventID` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `featureType` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `fileEntryRID` int(11) DEFAULT NULL,
  `geoDepth` decimal(40,5) DEFAULT NULL,
  `geoKMFROMHM` decimal(40,5) GENERATED ALWAYS AS (6371 * atan(sqrt(pow(0.7582812718284733 * sin(-1.9535056674539806 - radians(`geoLon`)),2) + pow(cos(radians(`geoLat`)) * 0.6519275364595309 - sin(radians(`geoLat`)) * 0.7582812718284733 * cos(-1.9535056674539806 - radians(`geoLon`)),2)),sin(radians(`geoLat`)) * 0.6519275364595309 + cos(radians(`geoLat`)) * 0.7582812718284733 * cos(-1.9535056674539806 - radians(`geoLon`)))) STORED,
  `geoLat` decimal(40,5) DEFAULT NULL,
  `geoLon` decimal(40,5) DEFAULT NULL,
  `geoType` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propAlert` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propCode` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propCompDYFIIndex` int(11) DEFAULT NULL,
  `propDegMinToStation` decimal(40,5) DEFAULT NULL,
  `propDepthErr` decimal(40,5) DEFAULT NULL,
  `propDetailUrl` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propEventType` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propFelt` int(11) DEFAULT NULL,
  `propIDsUsed` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propMagType` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propMag` decimal(40,5) DEFAULT NULL,
  `propMaxAzmGap` decimal(40,5) DEFAULT NULL,
  `propMaxMeasuredIntensity` decimal(40,5) DEFAULT NULL,
  `propNetwork` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propNumStations` int(11) DEFAULT NULL,
  `propPlace` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propProductTypesUsed` varchar(300) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propRMS` decimal(40,5) DEFAULT NULL,
  `propSignificanceIndex` int(11) DEFAULT NULL,
  `propSourcesUsed` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propStatus` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propTimeZ` datetime DEFAULT NULL,
  `propTitle` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propTsunami` int(11) DEFAULT NULL,
  `propTZLM` int(11) DEFAULT NULL,
  `propUpdatedL` datetime GENERATED ALWAYS AS (convert_tz(`propUpdatedZ`,'+00:00','right/US/Mountain')) STORED,
  `propUpdatedZ` datetime DEFAULT NULL,
  `propUrl` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`RID`),
  KEY `eventID` (`eventID`),
  KEY `propPlace` (`propPlace`),
  KEY `propIDsUsed` (`propIDsUsed`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


DROP TABLE IF EXISTS `GJ_files`;
CREATE TABLE `GJ_files` (
  `RID` int(11) NOT NULL AUTO_INCREMENT,
  `BBoxMaxDepth` decimal(40,5) DEFAULT NULL,
  `BBoxMaxLat` decimal(40,5) DEFAULT NULL,
  `BBoxMaxLon` decimal(40,5) DEFAULT NULL,
  `BBoxMinDepth` decimal(40,5) DEFAULT NULL,
  `BBoxMinLat` decimal(40,5) DEFAULT NULL,
  `BBoxMinLon` decimal(40,5) DEFAULT NULL,
  `fileType` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `metaAPI` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `metaFileStatus` int(11) DEFAULT NULL,
  `metaFileTitle` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `metaGeneratedTime` datetime DEFAULT NULL,
  `metaLimit` int(11) DEFAULT NULL,
  `metaOffset` int(11) DEFAULT NULL,
  `metaRecordCount` int(11) DEFAULT NULL,
  `metaURL` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
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
  `REGION0KMFROM` decimal(8,2) DEFAULT NULL,
  `REGION0NORTH` float DEFAULT NULL,
  `REGION0WEST` float DEFAULT NULL,
  `REGION0SOUTH` float DEFAULT NULL,
  `REGION0EAST` float DEFAULT NULL,
  `REGION1NAME` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT "",
  `REGION1DESCRIPTION` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT "",
  `REGION1KMFROM` decimal(8,2) DEFAULT NULL,
  `REGION1NORTH` float DEFAULT NULL,
  `REGION1WEST` float DEFAULT NULL,
  `REGION1SOUTH` float DEFAULT NULL,
  `REGION1EAST` float DEFAULT NULL,
  `REGION2NAME` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT "",
  `REGION2DESCRIPTION` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT "",
  `REGION2KMFROM` decimal(8,2) DEFAULT NULL,
  `REGION2NORTH` float DEFAULT NULL,
  `REGION2WEST` float DEFAULT NULL,
  `REGION2SOUTH` float DEFAULT NULL,
  `REGION2EAST` float DEFAULT NULL,
  `REGION3NAME` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT "",
  `REGION3DESCRIPTION` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT "",
  `REGION3KMFROM` decimal(8,2) DEFAULT NULL,
  `REGION3NORTH` float DEFAULT NULL,
  `REGION3WEST` float DEFAULT NULL,
  `REGION3SOUTH` float DEFAULT NULL,
  `REGION3EAST` float DEFAULT NULL,
  PRIMARY KEY (`RID`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
