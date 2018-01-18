ES_HOST = {"host" : "localhost", "port" : 9200}
INDEX_NAME = 'policy'
TYPE_NAME = 'policy'
ID_FIELD = 'policyID'

import csv
csv_file_object = csv.reader('dummy.csv')
 
header = csv_file_object.next()
header = [item.lower() for item in header]

bulk_data = [] 
for row in csv_file_object:
    data_dict = {}
    for i in range(len(row)):
        data_dict[header[i]] = row[i]
    op_dict = {
        "index": {
            "_index": INDEX_NAME, 
            "_type": TYPE_NAME, 
            "_id": data_dict[ID_FIELD]
        }
    }
    bulk_data.append(op_dict)
    bulk_data.append(data_dict)