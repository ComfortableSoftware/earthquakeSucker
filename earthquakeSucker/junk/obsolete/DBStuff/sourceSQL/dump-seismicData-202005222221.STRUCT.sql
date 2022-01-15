-- MariaDB dump 10.17  Distrib 10.4.13-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: seismicData
-- ------------------------------------------------------
-- Server version	10.4.13-MariaDB

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
-- Table structure for table `USGSData`
--

DROP TABLE IF EXISTS `USGSData`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `USGSData` (
  `RID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `propTimeZ` datetime DEFAULT NULL,
  `propTimeL` datetime GENERATED ALWAYS AS (convert_tz(`propTimeZ`,'+00:00','right/US/Mountain')) STORED,
  `geoLon` decimal(40,5) DEFAULT NULL,
  `geoLat` decimal(40,5) DEFAULT NULL,
  `geoDepth` decimal(40,5) DEFAULT NULL,
  `geoKMFROMHM` decimal(40,5) GENERATED ALWAYS AS (6371 * atan(sqrt(pow(0.7582812718284733 * sin(-1.9535056674539806 - radians(`geoLon`)),2) + pow(cos(radians(`geoLat`)) * 0.6519275364595309 - sin(radians(`geoLat`)) * 0.7582812718284733 * cos(-1.9535056674539806 - radians(`geoLon`)),2)),sin(radians(`geoLat`)) * 0.6519275364595309 + cos(radians(`geoLat`)) * 0.7582812718284733 * cos(-1.9535056674539806 - radians(`geoLon`)))) STORED,
  `propMag` decimal(40,5) DEFAULT NULL,
  `propMagType` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propNumStations` int(11) DEFAULT NULL,
  `propMaxAzmGap` decimal(40,5) DEFAULT NULL,
  `propDegMinToStation` decimal(40,5) DEFAULT NULL,
  `propRMS` decimal(40,5) DEFAULT NULL,
  `propNetwork` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `eventID` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propUpdatedZ` datetime DEFAULT NULL,
  `propUpdatedL` datetime GENERATED ALWAYS AS (convert_tz(`propUpdatedZ`,'+00:00','right/US/Mountain')) STORED,
  `propPlace` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propEventType` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propHorizontalErr` decimal(40,5) DEFAULT NULL,
  `propDepthErr` decimal(40,5) DEFAULT NULL,
  `propMagErr` decimal(40,5) DEFAULT NULL,
  `propMagNST` int(11) DEFAULT NULL,
  `propStatus` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propLocationSrc` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propMagSrc` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`RID`),
  KEY `eqid` (`eventID`),
  KEY `place` (`propPlace`)
) ENGINE=InnoDB AUTO_INCREMENT=224541 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `USGSStats`
--

DROP TABLE IF EXISTS `USGSStats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `USGSStats` (
  `RID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `TIMEL` datetime DEFAULT NULL,
  `TOTALNEW` int(11) DEFAULT NULL,
  `UTAHNEW` int(11) DEFAULT NULL,
  `MINMAGNITUDE` float DEFAULT NULL,
  `MAXMAGNITUDE` float DEFAULT NULL,
  PRIMARY KEY (`RID`)
) ENGINE=InnoDB AUTO_INCREMENT=3453 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `geoJsonEvents`
--

DROP TABLE IF EXISTS `geoJsonEvents`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `geoJsonEvents` (
  `RID` int(11) NOT NULL AUTO_INCREMENT,
  `eventID` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propPlace` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `fileEntryRID` int(11) DEFAULT NULL,
  `detailRID` int(11) DEFAULT NULL,
  `geoType` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `geoLon` decimal(40,5) DEFAULT NULL,
  `geoLat` decimal(40,5) DEFAULT NULL,
  `geoDepth` decimal(40,5) DEFAULT NULL,
  `featureType` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propMag` decimal(40,5) DEFAULT NULL,
  `propTimeZ` datetime DEFAULT NULL,
  `propUpdatedZ` datetime DEFAULT NULL,
  `propTZLM` int(11) DEFAULT NULL,
  `propUrl` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propDetailUrl` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propFelt` int(11) DEFAULT NULL,
  `propCompDYFIIndex` int(11) DEFAULT NULL,
  `propMaxMeasuredIntensity` decimal(40,5) DEFAULT NULL,
  `propAlert` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propStatus` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propTsunami` int(11) DEFAULT NULL,
  `propSignificanceIndex` int(11) DEFAULT NULL,
  `propNetwork` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propCode` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propIDsUsed` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propSourcesUsed` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propProductTypesUsed` varchar(300) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propNumStations` int(11) DEFAULT NULL,
  `propDegMinToStation` decimal(40,5) DEFAULT NULL,
  `propRMS` decimal(40,5) DEFAULT NULL,
  `propMaxAzmGap` decimal(40,5) DEFAULT NULL,
  `propMagType` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propEventType` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propTitle` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propTimeL` datetime GENERATED ALWAYS AS (convert_tz(`propTimeZ`,'+00:00','right/US/Mountain')) STORED,
  `propUpdatedL` datetime GENERATED ALWAYS AS (convert_tz(`propUpdatedZ`,'+00:00','right/US/Mountain')) STORED,
  `propDepthErr` decimal(40,5) DEFAULT NULL,
  `geoKMFROMHM` decimal(40,5) GENERATED ALWAYS AS (6371 * atan(sqrt(pow(0.7582812718284733 * sin(-1.9535056674539806 - radians(`geoLon`)),2) + pow(cos(radians(`geoLat`)) * 0.6519275364595309 - sin(radians(`geoLat`)) * 0.7582812718284733 * cos(-1.9535056674539806 - radians(`geoLon`)),2)),sin(radians(`geoLat`)) * 0.6519275364595309 + cos(radians(`geoLat`)) * 0.7582812718284733 * cos(-1.9535056674539806 - radians(`geoLon`)))) STORED,
  PRIMARY KEY (`RID`),
  KEY `eventID` (`eventID`),
  KEY `propPlace` (`propPlace`),
  KEY `propIDsUsed` (`propIDsUsed`)
) ENGINE=InnoDB AUTO_INCREMENT=36661 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `geoJsonEventsTest`
--

DROP TABLE IF EXISTS `geoJsonEventsTest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `geoJsonEventsTest` (
  `RID` int(11) NOT NULL AUTO_INCREMENT,
  `eventID` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propPlace` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `fileEntryRID` int(11) DEFAULT NULL,
  `detailRID` int(11) DEFAULT NULL,
  `geoType` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `geoLon` decimal(40,5) DEFAULT NULL,
  `geoLat` decimal(40,5) DEFAULT NULL,
  `geoDepth` decimal(40,5) DEFAULT NULL,
  `geoKMFROMHM` decimal(40,5) GENERATED ALWAYS AS (6371 * atan(sqrt(pow(0.7582812718284733 * sin(-1.9535056674539806 - radians(`geoLon`)),2) + pow(cos(radians(`geoLat`)) * 0.6519275364595309 - sin(radians(`geoLat`)) * 0.7582812718284733 * cos(-1.9535056674539806 - radians(`geoLon`)),2)),sin(radians(`geoLat`)) * 0.6519275364595309 + cos(radians(`geoLat`)) * 0.7582812718284733 * cos(-1.9535056674539806 - radians(`geoLon`)))) STORED,
  `featureType` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propMag` decimal(40,5) DEFAULT NULL,
  `propTimeZ` datetime DEFAULT NULL,
  `propTimeL` datetime GENERATED ALWAYS AS (convert_tz(`propTimeZ`,'+00:00','right/US/Mountain')) STORED,
  `propUpdatedZ` datetime DEFAULT NULL,
  `propUpdatedL` datetime GENERATED ALWAYS AS (convert_tz(`propUpdatedZ`,'+00:00','right/US/Mountain')) STORED,
  `propTZLM` int(11) DEFAULT NULL,
  `propUrl` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propDetailUrl` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propFelt` int(11) DEFAULT NULL,
  `propCompDYFIIndex` int(11) DEFAULT NULL,
  `propMaxMeasuredIntensity` decimal(40,5) DEFAULT NULL,
  `propAlert` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propStatus` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propTsunami` int(11) DEFAULT NULL,
  `propSignificanceIndex` int(11) DEFAULT NULL,
  `propNetwork` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propCode` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propIDsUsed` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propSourcesUsed` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propProductTypesUsed` varchar(300) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propNumStations` int(11) DEFAULT NULL,
  `propDegMinToStation` decimal(40,5) DEFAULT NULL,
  `propRMS` decimal(40,5) DEFAULT NULL,
  `propMaxAzmGap` decimal(40,20) DEFAULT NULL,
  `propMagType` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propEventType` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propTitle` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propDepthErr` decimal(40,20) DEFAULT NULL,
  PRIMARY KEY (`RID`),
  KEY `eventID` (`eventID`),
  KEY `propPlace` (`propPlace`),
  KEY `propIDsUsed` (`propIDsUsed`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `geoJsonFileEntries`
--

DROP TABLE IF EXISTS `geoJsonFileEntries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `geoJsonFileEntries` (
  `RID` int(11) NOT NULL AUTO_INCREMENT,
  `fileType` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `metaGeneratedTime` datetime DEFAULT NULL,
  `metaURL` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `metaFileTitle` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `metaFileStatus` int(11) DEFAULT NULL,
  `fileApiVersion` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `metaRecordCount` int(11) DEFAULT NULL,
  `BBoxMinLon` decimal(40,5) DEFAULT NULL,
  `BBoxMinLat` decimal(40,5) DEFAULT NULL,
  `BBoxMinDepth` decimal(40,5) DEFAULT NULL,
  `BBoxMaxLon` decimal(40,5) DEFAULT NULL,
  `BBoxMaxLat` decimal(40,5) DEFAULT NULL,
  `BBoxMaxDepth` decimal(40,5) DEFAULT NULL,
  PRIMARY KEY (`RID`)
) ENGINE=InnoDB AUTO_INCREMENT=254 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `queriesIn`
--

DROP TABLE IF EXISTS `queriesIn`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `queriesIn` (
  `RID` int(11) NOT NULL AUTO_INCREMENT,
  `QUERIESINTITLE` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `QUERIESINRETURNTO` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `SQLSELECT` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `SQLWHERE` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `SQLGROUPBY` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `SQLHAVING` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `SQLORDERBY` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `SQLLIMIT` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `REGION0NAME` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `REGION0DESCRIPTION` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `REGION0KMFROM` decimal(8,2) DEFAULT NULL,
  `REGION0NORTH` float DEFAULT NULL,
  `REGION0WEST` float DEFAULT NULL,
  `REGION0SOUTH` float DEFAULT NULL,
  `REGION0EAST` float DEFAULT NULL,
  `REGION1NAME` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `REGION1DESCRIPTION` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `REGION1KMFROM` decimal(8,2) DEFAULT NULL,
  `REGION1NORTH` float DEFAULT NULL,
  `REGION1WEST` float DEFAULT NULL,
  `REGION1SOUTH` float DEFAULT NULL,
  `REGION1EAST` float DEFAULT NULL,
  `REGION2NAME` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `REGION2DESCRIPTION` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `REGION2KMFROM` decimal(8,2) DEFAULT NULL,
  `REGION2NORTH` float DEFAULT NULL,
  `REGION2WEST` float DEFAULT NULL,
  `REGION2SOUTH` float DEFAULT NULL,
  `REGION2EAST` float DEFAULT NULL,
  `REGION3NAME` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `REGION3DESCRIPTION` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `REGION3KMFROM` decimal(8,2) DEFAULT NULL,
  `REGION3NORTH` float DEFAULT NULL,
  `REGION3WEST` float DEFAULT NULL,
  `REGION3SOUTH` float DEFAULT NULL,
  `REGION3EAST` float DEFAULT NULL,
  PRIMARY KEY (`RID`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping routines for database 'seismicData'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-22 22:21:48
