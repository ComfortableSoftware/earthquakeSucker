

aDetailDict = \
	{
	  TYPE: "FEATURE",
	  PROPERTIES:
		  {
	      MAG: DECIMAL,
	      PLACE: STRING,
	      TIME: INTEGER,
	      UPDATED: INTEGER,
	      TZ: INTEGER,
	      URL: STRING,
	      FELT:INTEGER,
	      CDI: DECIMAL,
	      MMI: DECIMAL,
	      ALERT: STRING,
	      STATUS: STRING,
	      TSUNAMI: INTEGER,
	      SIG:INTEGER,
	      NET: STRING,
	      CODE: STRING,
	      IDS: STRING,
	      SOURCES: STRING,
	      TYPES: STRING,
	      NST: INTEGER,
	      DMIN: DECIMAL,
	      RMS: DECIMAL,
	      GAP: DECIMAL,
	      MAGTYPE: STRING,
	      TYPE: STRING,
				PRODUCTS:
	        {
	          earthquake:
							[
	              {
	          ID: STRING,
	          TYPE: STRING,
	          CODE: STRING,
	          SOURCE: STRING,
	          UPDATETIME: INTEGER,
	          STATUS: STRING,
	          PROPERTIES: {
	            <KEY>: STRING,
	            …
	          },
	          PREFERREDWEIGHT: INTEGER,
	          CONTENTS: {
	            <PATH>: {
	              CONTENTTYPE: STRING,
	              LASTMODIFIED: LONG INTEGER,
	              LENGTH: INTEGER,
	              URL: STRING
	            },
	            …
	          }
	        },
	        …
	      ],
	      …
	    }
	  },
	  GEOMETRY: {
	    TYPE: "POINT",
	    COORDINATES: [
	      LONGITUDE,
	      LATITUDE,
	      DEPTH
	    ]
	  },
	  ID: STRING
	}

