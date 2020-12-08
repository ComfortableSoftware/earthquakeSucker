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
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
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
  `metaAPI` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `metaLimit` int,
  `metaOffset` int,
  `metaRecordCount` int(11) DEFAULT NULL,
  `BBoxMinLon` decimal(40,5) DEFAULT NULL,
  `BBoxMinLat` decimal(40,5) DEFAULT NULL,
  `BBoxMinDepth` decimal(40,5) DEFAULT NULL,
  `BBoxMaxLon` decimal(40,5) DEFAULT NULL,
  `BBoxMaxLat` decimal(40,5) DEFAULT NULL,
  `BBoxMaxDepth` decimal(40,5) DEFAULT NULL,
  PRIMARY KEY (`RID`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

	("metaAPI", DFLTSTR, DFLTSTR, "varchar", "API",),
	("metaFileRID", 0, 0, "int", "MFRID"),
	("metaFileStatus", 0, 0, "int", "FSTAT",),
	("metaFileTitle", DFLTSTR, DFLTSTR, "varchar", "metaTitle",),
	("metaGeneratedTime", DFLTSTR, DFLTSTR, "datetime", "timestamp",),
	("metaLimit", 0, 0, "int", "LIMIT"),
	("metaOffset", 0, 0, "int", "OFFSET"),
	("metaRecordCount", 0, 0, "int", "MRC",),
	("metaURL", DFLTSTR, DFLTSTR, "varchar", "URL",),