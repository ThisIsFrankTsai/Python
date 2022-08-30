import pymongo
from pprint import *

client = pymongo.MongoClient('localhost:20000') #任意機器
db = client.test

cursor = db.members.watch() 
print('變化流初始的resume token:: \n{}\n'.format(cursor.resume_token)) 
while True: #保持連線
    document = next(cursor) #卡住
    print('每筆資料的 resume token:: \n{}\n'.format(cursor.resume_token)) #直到變化 
    print('傳回的內容::')
    pprint(document)


