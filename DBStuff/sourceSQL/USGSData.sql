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
  KEY `eqid` (`EQID`)
) ENGINE=InnoDB AUTO_INCREMENT=218945 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
