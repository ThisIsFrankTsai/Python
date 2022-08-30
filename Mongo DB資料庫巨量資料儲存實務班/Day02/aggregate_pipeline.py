import pymongo
from pprint import pprint

DATABASE='opendata'
COLLECTION='AQI'
client = pymongo.MongoClient()
db = client[DATABASE]  #寫成變數


pipeline=[
    {
        '$addFields': {
            'iAQI': {
                '$toInt': '$AQI'
            }
        }
    }, {
        '$bucket': {
            'groupBy': '$iAQI', 
            'boundaries': [
                0, 11, 21, 31, 1000
            ], 
            'default': 'error', 
            'output': {
                'count': {
                    '$sum': 1
                }, 
                'location': {
                    '$push': {
                        'County': '$County', 
                        'SiteName': '$SiteName', 
                        'AQI': '$AQI'
                    }
                }
            }
        }
    }, {
        '$match': {
            '_id': 21
        }
    }, {
        '$unwind': '$location'
    }, {
        '$replaceWith': '$location'
    }
]
"""
pipeline = [
    {
        '$project': {
            'County': 1, 
            '_id': 0, 
            'SiteName': 1, 
            'AQI': 1
        }
    }, {
        '$addFields': {
            'iAQI': {
                '$toInt': '$AQI'
            }
        }
    }, {
        '$group': {
            '_id': '$County', 
            'AverageAQI': {
                '$avg': '$iAQI'
            }
        }
    }, {
        '$addFields': {
            'AverageAQI': {
                '$round': [
                    '$AverageAQI', 0
                ]
            }
        }
    }, {
        '$sort': {
            'AverageAQI': -1
        }
    }, {
        '$limit': 3
    }
]
docs = db[COLLECTION].aggregate(pipeline)
"""
docs = db[COLLECTION].aggregate(pipeline)
pprint(list(docs))
