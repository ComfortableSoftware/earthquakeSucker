-- MariaDB dump 10.17  Distrib 10.4.13-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: seismicData
-- ------------------------------------------------------
-- Server version	10.4.12-MariaDB

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
  `TIMEZ` datetime DEFAULT NULL,
  `TIMEL` datetime DEFAULT NULL,
  `LATITUDE` float DEFAULT NULL,
  `LONGITUDE` float DEFAULT NULL,
  `EVENTDEPTH` decimal(10,3) DEFAULT NULL,
  `MAGNITUDE` decimal(4,2) DEFAULT NULL,
  `MAGNITUDETYPE` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `NST` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `GAP` decimal(10,3) DEFAULT NULL,
  `DMIN` decimal(10,3) DEFAULT NULL,
  `RMS` decimal(10,2) DEFAULT NULL,
  `NETWORK` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `EQID` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `UPDATEDZ` datetime DEFAULT NULL,
  `UPDATEDL` datetime DEFAULT NULL,
  `PLACE` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `EVENTTYPE` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `HORIZONTALERROR` decimal(10,2) DEFAULT NULL,
  `DEPTHERROR` decimal(10,2) DEFAULT NULL,
  `MAGNITUDEERROR` decimal(4,2) DEFAULT NULL,
  `MAGNST` int(11) DEFAULT NULL,
  `EVENTSTATUS` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `LOCATIONSOURCE` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `MAGNITUDESOURCE` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`RID`),
  KEY `eqid` (`EQID`),
  KEY `place` (`PLACE`)
) ENGINE=InnoDB AUTO_INCREMENT=219492 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
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
  `geoLon` decimal(40,20) DEFAULT NULL,
  `geoLat` decimal(40,20) DEFAULT NULL,
  `geoDepth` decimal(40,20) DEFAULT NULL,
  `featureType` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propMag` decimal(40,20) DEFAULT NULL,
  `propTimeZ` datetime DEFAULT NULL,
  `propUpdatedZ` datetime DEFAULT NULL,
  `propTZLM` int(11) DEFAULT NULL,
  `propUrl` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propDetailUrl` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propFelt` int(11) DEFAULT NULL,
  `propCompDYFIIndex` int(11) DEFAULT NULL,
  `propMaxMeasuredIntensity` decimal(40,20) DEFAULT NULL,
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
  `propDegMinToStation` decimal(40,20) DEFAULT NULL,
  `propRMS` decimal(40,20) DEFAULT NULL,
  `propMaxAzmGap` decimal(40,20) DEFAULT NULL,
  `propMagType` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propEventType` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propTitle` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
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
  `fileMetaGeneratedTime` datetime DEFAULT NULL,
  `fileUrl` varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `fileTitle` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `fileStatus` int(11) DEFAULT NULL,
  `fileApiVersion` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `fileRecordCount` int(11) DEFAULT NULL,
  `fileBBoxMinLon` decimal(40,20) DEFAULT NULL,
  `fileBBoxMinLat` decimal(40,20) DEFAULT NULL,
  `fileBBoxMinDepth` decimal(40,20) DEFAULT NULL,
  `fileBBoxMaxLon` decimal(40,20) DEFAULT NULL,
  `fileBBoxMaxLat` decimal(40,20) DEFAULT NULL,
  `fileBBoxMaxDepth` decimal(40,20) DEFAULT NULL,
  PRIMARY KEY (`RID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
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
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
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

-- Dump completed on 2020-05-17 21:36:42
