import pymongo
from pprint import pprint

client = pymongo.MongoClient()
db = client.opendata

cursor=db.geoAQI.find({ 
    'geometry': {
        '$geoWithin': {    #找交集 geoIntersects # 完整包含範圍geoWithin
                '$box':[   #左下角 畫到 右上角
              [
            121.43051147460938,
            24.966140159912975
          ],
          [
            121.63650512695312,
            25.156472435986753
          ]
                ]
            }
        } 
},{'County':1,'SiteName':1,'AQI':1,'_id':0})

pprint(list(cursor))