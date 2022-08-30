import pymongo
from pprint import *

client = pymongo.MongoClient('localhost:20000') #任意機器
db = client.test

token={'_data':
'8262FB336C000000012B022C0100296E5A10047C2364C2DC014F1BA82DC97EDBB92E2946645F6964006462FB336CC8ED813CA9A539440004'
}#為了監聽變化流斷線後，無法監聽資料 
 #從oplog找出異動資料並補上
 #但是如果oplog滿了或覆蓋 也是會漏掉
 #解決方法:斷線不能太久、oplog放大
cursor = db.members.watch(resume_after=token) #監測 resume_after 斷線前最後一筆資料
print('變化流初始的resume token:: \n{}\n'.format(cursor.resume_token)) #cursor.resume_token 目前最新那一筆資料最新的token
while True: #保持連線
    document = next(cursor) #卡住
    print('每筆資料的 resume token:: \n{}\n'.format(cursor.resume_token)) #直到變化 
    print('傳回的內容::')
    pprint(document)


