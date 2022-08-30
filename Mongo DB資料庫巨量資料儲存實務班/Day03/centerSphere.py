import pymongo
from pprint import pprint

client = pymongo.MongoClient()
db = client.turist

cursor=db.spot.find({ 
    'Geometry': {
        '$geoWithin': {    #找交集 geoIntersects # 完整包含範圍geoWithin
                '$centerSphere':[   #半徑      
            [ 121.18057250976562,25.04081549894912 ],
            5/6378.1
                ]
            }
        } 
},{'Name':1,'Description':1,'Add':1,'_id':0})

pprint(list(cursor))