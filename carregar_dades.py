from elasticsearch import Elasticsearch
import json

"""
Script to index the data
"""


def index_data():
    with open("carrers.json") as f:
        data = f.read()
    example_data = json.loads(data)
    es = Elasticsearch()
    for element in example_data:
        if element["name"]:
            geom = json.loads(element["geom"])
            element["geom"] = geom
            print geom
            resp = es.index(
                index="presentacio",
                doc_type="doc",
                body=element,
                id=element["osm_id"]
            )
            print resp

index_data()
