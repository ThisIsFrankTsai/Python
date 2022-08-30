import pymongo
from pprint import pprint
 
hosts=['localhost:20000','localhost:20001']
client = pymongo.MongoClient(hosts,readPreference='secondary')

db = client.test
docs=db.test.find()

pprint(list(docs))