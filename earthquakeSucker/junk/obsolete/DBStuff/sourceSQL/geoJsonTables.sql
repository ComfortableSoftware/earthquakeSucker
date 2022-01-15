DROP TABLE IF EXISTS `geoJsonFileEntries`;
create table geoJsonFileEntries(
	RID int not null auto_increment primary key,
	fileType varchar(100),
	fileMetaGeneratedTime datetime,
	fileUrl varchar(500),
	fileTitle varchar(200),
	fileStatus int,
	fileApiVersion varchar(100),
	fileRecordCount int,
	fileBBoxMinLon decimal(40,20),
	fileBBoxMinLat decimal(40,20),
	fileBBoxMinDepth decimal(40,20),
	fileBBoxMaxLon decimal(40,20),
	fileBBoxMaxLat decimal(40,20),
	fileBBoxMaxDepth decimal(40,20)
);


DROP TABLE IF EXISTS `geoJsonDetails`;
create table geoJsonDetails(
	RID int not null auto_increment primary key,
	eventID varchar(100) not null index XeventID,
	eventsRID int,
	geoJsonEventsRID int,
	detailsProductsRIDs varchar(200),
	geoType varchar(100),
	geoCoordsLat decimal(40,20),
	geoCoordsLat decimal(40,20),
	geoCoordsDepth decimal(40,20)
);


DROP TABLE IF EXISTS `geoJsonEvents`;
create table geoJsonEvents(
	RID int not null auto_increment primary key,
	eventID varchar(100) not null index XeventID,
	propPlace varchar(200) not null index XpropPlace,
	fileEntryRID int,
	detailRID int,
	geoType varchar(100),
	geoLon decimal(40,20),
	geoLat decimal(40,20),
	geoDepth decimal(40,20),
	feaureType varchar(100),
	propMag decimal(40,20),
	propTimeZ datetime,
	propUpdatedZ datetime,
	propTZLM int,
	propUrl varchar(200),
	propDetailUrl varchar(200),
	propFelt int,
	propCompDYFIIndex int,
	propMaxMeasuredIntensity decimal(40,20),
	propAlert varchar(100),
	propStatus varchar(100),
	propTsunami int,
	propSignificanceIndex int,
	propNetwork varchar(100),
	propCode varchar(100),
	propIDsUsed varchar(200),
	propSourcesUsed varchar(200),
	propProductTypesUsed varchar(300),
	propNumStations int,
	propDegMinToStation decimal(40,20),
	propRMS decimal(40,20),
	propMaxAzmGap decimal(40,20),
	propMagType varchar(100),
	propEventType varchar(100),
	propTitle varchar(200)
);


DROP TABLE IF EXISTS `geoJsonProducts`;
create table geoJsonProducts(
	RID int not null auto_increment primary key,
	eventID varchar(100) not null index XeventID,


