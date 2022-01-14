


myOffset = 1
myUrl = f"""https://earthquake.usgs.gov/fdsnws/event/1/query.geojson?starttime=1900-04-21%2000:00:00"""
myUrl += f"""&endtime=2020-05-21%2023:59:59&minmagnitude=-1&orderby=time&limit=10000&offset={myOffset}"""
