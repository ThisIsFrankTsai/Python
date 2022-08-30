import pymongo
from pprint import pprint

client = pymongo.MongoClient()
db = client.opendata

cursor=db.geoAQI.find({ 
    'geometry': {
        '$geoWithin': {    #找交集 geoIntersects # 完整包含範圍geoWithin
                '$centerSphere':[   #圓弧常數        
            [
              121.47994995117188,
              24.821639356846607
            ],
            10/6378.1
                ]
            }
        } 
},{'County':1,'SiteName':1,'AQI':1,'_id':0})

pprint(list(cursor))