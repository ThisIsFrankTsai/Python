import pymongo

client = pymongo.MongoClient(['localhost:27017', 'localhost:27018'])
db = client.test

num = 480000

for n in range(100):
    db.school.insert_one(
        {
            'staff_id':n,
            'c': 'staff', #無指定，平均分散
            'junk': '_' * num
        }
    )