#查詢by View

import pymongo
from pprint import pprint

DATABASE='opendata'

client = pymongo.MongoClient()
db = client[DATABASE]  #寫成變數
cursor=db.avgaqi.find()

pprint(list(cursor))