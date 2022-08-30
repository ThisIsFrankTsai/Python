import pymongo

client = pymongo.MongoClient(['localhost:27017', 'localhost:27018'])
db = client.test

num = 480000
data = [18]
for n in data:
    db.d.insert_one(
        {
            'lv': None,
            'n': n,
            'junk': '_' * num
        }
    )