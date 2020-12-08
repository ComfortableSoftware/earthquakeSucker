use seismicData;
create table prefix (
	RID int auto_increment not null primary key,
	myKey varchar(100) key,
	prefix varchar(1000),
	keyType varchar(1000),
	description text,
	sampleData text
);

