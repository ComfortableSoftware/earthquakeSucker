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
-- Table structure for table `USGSGeoJson`
--


DROP TABLE IF EXISTS `geoJsonSummaryFeatures`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `geoJsonSummaryFeatures` (
  `RID` int(11) NOT NULL AUTO_INCREMENT,
  `nextRID` int(11) DEFAULT NULL,
  `prevRID` int(11) DEFAULT NULL,
  `eventID` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `entryType` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propMagnitude` decimal(40,20) DEFAULT NULL,
  `propPlace` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propTimeZ` datetime DEFAULT NULL,
  `propUpdatedZ` datetime DEFAULT NULL,
  `propTZ` int(11) DEFAULT NULL,
  `propUrl` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propDetail` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propFelt` int(11) DEFAULT NULL,
  `propDYFIIndex` int(11) DEFAULT NULL,
  `propAlert` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propStatus` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propTsunami` int(11) DEFAULT NULL,
  `propSignificance` int(11) DEFAULT NULL,
  `propNet` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propCode` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propIdsUsed` varchar(300) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propSourcesUsed` varchar(300) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propTypesUsed` varchar(1000) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propNumStationsUsed` int(11) DEFAULT NULL,
  `propHorizDegFrmStation` decimal(40,20) DEFAULT NULL,
  `propRMSOfWave` decimal(40,20) DEFAULT NULL,
  `propMaxGapAziDeg` decimal(40,20) DEFAULT NULL,
  `propMagnitudeType` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propEventType` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `propEventTitle` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `geometryType` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `geometryLat` decimal(40,20) DEFAULT NULL,
  `geometryLon` decimal(40,20) DEFAULT NULL,
  `geometryDepth` decimal(40,20) DEFAULT NULL,
  PRIMARY KEY (`RID`),
  KEY `eventID` (`eventID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `geoJsonSummary`
--

DROP TABLE IF EXISTS `geoJsonSummarySummary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `geoJsonSummarySummary` (
  `RID` int(11) NOT NULL AUTO_INCREMENT,
  `featuresId` int(11) DEFAULT NULL,
  `detailsID` int(11) DEFAULT NULL,
  `eventID` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL key,
  `metadataEngenerated` datetime DEFAULT NULL,
  `metadataUrl` varchar(300) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `metadataTitle` varchar(300) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `metadataStatus` int(11) DEFAULT NULL,
  `metadataApi` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`RID`),
  KEY `eventID` (`eventID`)
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

-- Dump completed on 2020-05-17  5:20:02
