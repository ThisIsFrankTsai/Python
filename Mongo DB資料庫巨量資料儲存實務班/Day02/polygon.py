import pymongo
from pprint import pprint

client = pymongo.MongoClient()
db = client.opendata

cursor=db.geoAQI.find({ 
    'geometry': {
        '$geoWithin': {    #找交集 geoIntersects # 完整包含範圍geoWithin
                '$polygon':[   #多邊型       
            [
            [
              121.39755249023439,
              25.015928763367857
            ],
            [
              121.15036010742188,
              24.957425081612215
            ],
            [
              121.1407470703125,
              24.750572772068463
            ],
            [
              121.2451171875,
              24.55087064225044
            ],
            [
              121.56784057617186,
              24.483399199271453
            ],
            [
              121.69418334960939,
              24.686952411999155
            ],
            [
              121.73263549804688,
              24.830364024647107
            ],
            [
              121.73126220703125,
              24.923804001418254
            ],
            [
              121.65847778320311,
              25.063209244186485
            ],
            [
              121.53350830078124,
              25.147770882723563
            ],
            [
              121.41952514648438,
              25.104253813095614
            ],
            [
              121.39755249023439,
              25.015928763367857
            ]
          ]
                ]
            }
        } 
},{'County':1,'SiteName':1,'AQI':1,'_id':0})

pprint(list(cursor))