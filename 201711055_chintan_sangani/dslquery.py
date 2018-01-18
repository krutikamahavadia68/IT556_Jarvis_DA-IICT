from elasticsearch import Elasticsearch
client = Elasticsearch()

response = client.search(
    index="titanic",
    body={
      "query": {
        "filtered": {
          "query": {
            "bool": {
              "must": [{"match": {"Sex": "male"}}]
            }
          },
          "filter": {"term": {"category": "search"}}
        }
      },
      "aggs" : {
        "per_tag": {
          "terms": {"field": "tags"},
          "aggs": {
            "max_lines": {"max": {"field": "lines"}}
          }
        }
      }
    }
)
print (response)
for hit in response['hits']['hits']:
    print(hit['_score'], hit['_source']['title'])

for tag in response['aggregations']['per_tag']['buckets']:
    print(tag['key'], tag['max_lines']['value'])
