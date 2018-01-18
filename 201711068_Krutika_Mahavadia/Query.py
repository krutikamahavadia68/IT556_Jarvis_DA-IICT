from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

#get particular ID
res = es.get(index="music", doc_type='music-map', id=10)
print(res['_source'])

#get all records
res = es.search(index="music", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print("%(title)s %(artist)s" % hit["_source"])

#get documents with "Wiley" in their "location" field
res = es.search(index="music", body={"query": {"match": {"location": "Wiley"}}})
print("%d documents found" % res['hits']['total'])
for doc in res['hits']['hits']:
    print("%s %s" % (doc['_source']['title'], doc['_source']['artist']))

