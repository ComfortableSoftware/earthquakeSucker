DROP TABLE IF EXISTS `USGSGeoJson`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `USGSGeoJson` (
  `RID` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `EQID` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL KEY,
  `EQIDS` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `TIMEZ` datetime DEFAULT NULL,
  `UPDATEDZ` datetime DEFAULT NULL,
  `TZ` int(11) DEFAULT NULL,
  `MAGNITUDE` decimal(40,20) DEFAULT NULL,
  `MAGERROR` decimal(40,20)DEFAULT NULL,
  `MAGTYPE` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `MAGSOURCE` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `URL` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `DETAIL` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ALERT` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `STATUS` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `TSUNAMI` int(11) DEFAULT NULL,
  `NET` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `CODE` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `SOURCES` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `EVENTTYPE` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `EVENTTYPES` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `NUMSTATIONS` int(11) DEFAULT NULL,
  `MAGNUMSTATIONS` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `DEGMINSTATION` decimal(40,20)DEFAULT NULL,
  `RMS` decimal(40,20)DEFAULT NULL,
  `MAXGAPAZIDEG` decimal(40,20)DEFAULT NULL,
  `NUMPHASE` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `GEOLAT` decimal(40,20)DEFAULT NULL,
  `GEOLON` decimal(40,20)DEFAULT NULL,
  `GEODEPTH` decimal(40,20)DEFAULT NULL,
  `LOCATIONSOURCE` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `HORIZONTALERROR` decimal(40,20)DEFAULT NULL,
  `DEPTHERROR` decimal(40,20)DEFAULT NULL,
  `SIGNIFICANCE` int(11) DEFAULT NULL,
  `FELT` int(11) DEFAULT NULL,
  `DYFIMAX` decimal(40,20)DEFAULT NULL,
  `MAXINSTINTENSITY` decimal(40,20)DEFAULT NULL,
  `TITLE` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL key,
  `PLACE` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL key,
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;


DROP TABLE IF EXISTS `geoJsonDetails`;
create table geoJsonDetails(
RID int not null auto_increment primary key,
eventID varchar(100) not null index XeventID,
geoType varchar(100),
geoCoordLon decimal(40,20),
geoCoordLat decimal(40,20),
geoCoordDepth decimal(40,20),
featureRIDs varchar(200),
productRIDs varchar(200),
propMag decimal(40,20),
);


create table geoJsonProducts(
RID int not null auto_increment primary key,
productName varchar(100) default null key,
productLocation varchar(200) default null key,
prodType varchar(200),
prodEventCode varchar(200),
prevProductRID int,
nextProductRID int,
productIndexID varchar(100),
productIndexTimeZ datetime,
productID varchar(200),
productStatus varchar(100),
productPropEventSource varchar(100),
propUpdateTimeZ datetime,
prodPropEventSrc varchar(100),
prodPropEventSrcCode varchar(100),
prodPropLocn varchar(200) not null index xProdPropLocn,
prodPropPdlClientVer varchar(100),
prodPropTsunami int,
prodPropUTCTZM varchar(100), -- possibly better made an int
prodPreferredWght int,
prodContentName varchar(200),
prodContentType varchar(200),
prodContentLastMod datetime,
prodContentLen int,
prodContentUrl varchar(500),
);
