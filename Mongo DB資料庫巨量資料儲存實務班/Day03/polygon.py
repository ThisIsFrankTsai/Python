import pymongo
from pprint import pprint

client = pymongo.MongoClient()
db = client.turist

cursor=db.spot.find({ 
    'Geometry': {
        '$geoWithin': {    #找交集 geoIntersects # 完整包含範圍geoWithin
                '$polygon':[   #多邊型       
            [
              121.18057250976562,
              25.04081549894912
            ],
            [
              121.17507934570311,
              25.009706290997322
            ],
            [
              121.18606567382812,
              24.968630068937276
            ],
            [
              121.23962402343749,
              24.93252145867791
            ],
            [
              121.3275146484375,
              24.948709386318527
            ],
            [
              121.35772705078125,
              25.017173220003865
            ],
            [
              121.18057250976562,
              25.04081549894912
            ]          
                ]
            }
        } 
},{'Name':1,'Description':1,'Add':1,'_id':0})

pprint(list(cursor))