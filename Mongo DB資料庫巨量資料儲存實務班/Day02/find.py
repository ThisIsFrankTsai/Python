import pymongo
from pprint import pprint

client = pymongo.MongoClient()
db = client.test

cursor=db.ataiwan.find(
   { 
    'geometry': {
        '$geoIntersects': { 
            '$geometry': {
                'type': 'Point',
                'coordinates': [ 121.76971435546874,
                                 24.693191139677126 ] 
            }
        } 
    }
}


)

pprint(list(cursor))