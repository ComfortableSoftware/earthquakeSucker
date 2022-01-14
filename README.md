
  1. [] getGeojson.py
    - `https://earthquake.usgs.gov/fdsnws/event/1/count?<query>`
     1. [] GEOJSONALLSMRY month/week/day/hour summary
        1. [] Needs to get count and paginate current limit 20,000
     2. [] GEOJSONQUERY my own query, this is a class.
        1. [] Needs to get count and paginate current limit 20,000
        2. [] ALL parameters need to work
     3. [] GEOJSONDETAIL
        1. [] Needs to get count and paginate current limit 20,000
     4. [] GEOJSONDETAILQUERY
        1. [] Needs to get count and paginate current limit 20,000
        2. [] ALL parameters need to work
  2. [] web01.py 
     1. [] This is now a standalone class that only displays results given an SQL string to select what to display.
     2. [] separate web01 out, this class only gets geoJson data and puts it into MariaDB
  3. [] getCsv.py.
    - **DOES NOT HAVE A COUNT METHOD**
