-- MariaDB dump 10.19  Distrib 10.6.5-MariaDB, for Linux (x86_64)
--
-- Host: 192.168.0.16    Database: GJ_data
-- ------------------------------------------------------
-- Server version	10.6.5-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `GJ_enumerated`
--

DROP TABLE IF EXISTS `GJ_enumerated`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `GJ_enumerated` (
  `RID` int(11) NOT NULL AUTO_INCREMENT,
  `itemType` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT '',
  `entryName` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT '',
  `description` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT '',
  PRIMARY KEY (`RID`),
  KEY `itemType` (`itemType`),
  KEY `typeEntry` (`itemType`,`entryName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `GJ_events`
--

DROP TABLE IF EXISTS `GJ_events`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `GJ_events` (
  `RID` int(11) NOT NULL AUTO_INCREMENT,
  `detailRID` int(11) DEFAULT 0,
  `eventID` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT '',
  `featureType` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT '',
  `fileEntryRID` int(11) DEFAULT 0,
  `geoDepth` decimal(40,20) DEFAULT 0.00000000000000000000,
  `geoHomeLat` decimal(40,20) DEFAULT 41.00000000000000000000,
  `geoHomeLon` decimal(40,20) DEFAULT -112.00000000000000000000,
  `geoKMFROMHM` decimal(40,20) GENERATED ALWAYS AS (atan(sqrt(pow(cos(radians(`geoHomeLat`)) * sin(radians(`geoHomeLon`) - radians(`geoLon`)),2) + pow(cos(radians(`geoLat`)) * sin(radians(`geoHomeLat`)) - sin(radians(`geoLat`)) * cos(radians(`geoHomeLat`)) * cos(radians(`geoHomeLon`) - radians(`geoLon`)),2)),sin(radians(`geoLat`)) * sin(radians(`geoHomeLat`)) + cos(radians(`geoLat`)) * cos(radians(`geoHomeLat`)) * cos(radians(`geoHomeLon`) - radians(`geoLon`))) * 6371) STORED,
  `geoLat` decimal(40,20) DEFAULT 0.00000000000000000000,
  `geoLon` decimal(40,20) DEFAULT 0.00000000000000000000,
  `geoType` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT '',
  `propAlert` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT '',
  `propCode` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT '',
  `propCompDYFIIndex` int(11) DEFAULT 0,
  `propDegMinToStation` decimal(40,20) DEFAULT 0.00000000000000000000,
  `propDepthErr` decimal(40,20) DEFAULT 0.00000000000000000000,
  `propDetailUrl` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT '',
  `propEventType` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT '',
  `propFelt` int(11) DEFAULT 0,
  `propIDsUsed` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT '',
  `propMagType` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT '',
  `propMag` decimal(40,20) DEFAULT 0.00000000000000000000,
  `propMaxAzmGap` decimal(40,20) DEFAULT 0.00000000000000000000,
  `propMaxMeasuredIntensity` decimal(40,20) DEFAULT 0.00000000000000000000,
  `propNetwork` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT '',
  `propNumStations` int(11) DEFAULT 0,
  `propPlace` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT '',
  `propProductTypesUsed` varchar(300) COLLATE utf8mb4_unicode_ci DEFAULT '',
  `propRMS` decimal(40,20) DEFAULT 0.00000000000000000000,
  `propSignificanceIndex` int(11) DEFAULT 0,
  `propSourcesUsed` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT '',
  `propStatus` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT '',
  `propTimeZ` datetime DEFAULT NULL,
  `propTitle` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT '',
  `propTsunami` int(11) DEFAULT 0,
  `propTZLM` int(11) DEFAULT 0,
  `propUpdatedL` datetime GENERATED ALWAYS AS (convert_tz(`propUpdatedZ`,'+00:00','right/US/Mountain')) STORED,
  `propUpdatedZ` datetime DEFAULT NULL,
  `propUrl` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT '',
  PRIMARY KEY (`RID`),
  KEY `eventID` (`eventID`),
  KEY `propPlace` (`propPlace`),
  KEY `propIDsUsed` (`propIDsUsed`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `GJ_files`
--

DROP TABLE IF EXISTS `GJ_files`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `GJ_files` (
  `RID` int(11) NOT NULL AUTO_INCREMENT,
  `BBoxMaxDepth` decimal(40,20) DEFAULT 0.00000000000000000000,
  `BBoxMaxLat` decimal(40,20) DEFAULT 0.00000000000000000000,
  `BBoxMaxLon` decimal(40,20) DEFAULT 0.00000000000000000000,
  `BBoxMinDepth` decimal(40,20) DEFAULT 0.00000000000000000000,
  `BBoxMinLat` decimal(40,20) DEFAULT 0.00000000000000000000,
  `BBoxMinLon` decimal(40,20) DEFAULT 0.00000000000000000000,
  `fileType` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT '',
  `metaAPI` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT '',
  `metaFileStatus` int(11) DEFAULT 0,
  `metaFileTitle` text COLLATE utf8mb4_unicode_ci DEFAULT '',
  `metaGeneratedTime` datetime DEFAULT NULL,
  `metaLimit` int(11) DEFAULT 0,
  `metaOffset` int(11) DEFAULT 0,
  `metaRecordCount` int(11) DEFAULT 0,
  `metaURL` text COLLATE utf8mb4_unicode_ci DEFAULT '',
  PRIMARY KEY (`RID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `GJ_queries`
--

DROP TABLE IF EXISTS `GJ_queries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `GJ_queries` (
  `RID` int(11) NOT NULL AUTO_INCREMENT,
  `QUERIESINTITLE` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT '',
  `QUERIESINRETURNTO` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT '',
  `SQLSELECT` text COLLATE utf8mb4_unicode_ci DEFAULT '',
  `SQLWHERE` text COLLATE utf8mb4_unicode_ci DEFAULT '',
  `SQLGROUPBY` text COLLATE utf8mb4_unicode_ci DEFAULT '',
  `SQLHAVING` text COLLATE utf8mb4_unicode_ci DEFAULT '',
  `SQLORDERBY` text COLLATE utf8mb4_unicode_ci DEFAULT '',
  `SQLLIMIT` text COLLATE utf8mb4_unicode_ci DEFAULT '',
  `REGION0NAME` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT '',
  `REGION0DESCRIPTION` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT '',
  `REGION0KMFROM` decimal(8,2) DEFAULT 0.00,
  `REGION0NORTH` float DEFAULT 0,
  `REGION0WEST` float DEFAULT 0,
  `REGION0SOUTH` float DEFAULT 0,
  `REGION0EAST` float DEFAULT 0,
  `REGION1NAME` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT '',
  `REGION1DESCRIPTION` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT '',
  `REGION1KMFROM` decimal(8,2) DEFAULT 0.00,
  `REGION1NORTH` float DEFAULT 0,
  `REGION1WEST` float DEFAULT 0,
  `REGION1SOUTH` float DEFAULT 0,
  `REGION1EAST` float DEFAULT 0,
  `REGION2NAME` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT '',
  `REGION2DESCRIPTION` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT '',
  `REGION2KMFROM` decimal(8,2) DEFAULT 0.00,
  `REGION2NORTH` float DEFAULT 0,
  `REGION2WEST` float DEFAULT 0,
  `REGION2SOUTH` float DEFAULT 0,
  `REGION2EAST` float DEFAULT 0,
  `REGION3NAME` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT '',
  `REGION3DESCRIPTION` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT '',
  `REGION3KMFROM` decimal(8,2) DEFAULT 0.00,
  `REGION3NORTH` float DEFAULT 0,
  `REGION3WEST` float DEFAULT 0,
  `REGION3SOUTH` float DEFAULT 0,
  `REGION3EAST` float DEFAULT 0,
  PRIMARY KEY (`RID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-17 19:55:10
