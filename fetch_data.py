import json
import psycopg2.extras

"""
Script to generate data of the osm db
"""

config_db = {
	'user': 'python',
	'dbname':'girona',
	'password':'pygrn',
	'host':'localhost'
}


conn = psycopg2.connect(**config_db)


sql_json = """
select "bridge","layer","bicycle","lock","surface","osm_id","operator","horse","service","area","way_area","width",ST_AsGeoJSON(way) as geom,"motorcar","covered","boundary","ref","highway","admin_level","noname","junction","barrier","toll","denomination","foot","population","z_order","name","tunnel","disused","route","place","public_transport","oneway","railway","landuse","tracktype" from planet_osm_roads where st_intersects((select way from planet_osm_polygon where osm_id=-343535),way);
"""

dict_cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
cur.execute(sql_json)
result = []
for data in cur:
    result.append(dict(data))
with open("carrers.json", "w") as f:
    f.write(json.dumps(result))
