import pymongo
client = pymongo.MongoClient(['localhost:20000', 'localhost:20001', 'localhost:20002']) #任寫一個，MongoDB只要連進去後，會自動尋找誰是Primary
db = client.test

# 建立交易需要的 session
session = client.start_session()
# 交易開始
session.start_transaction()
db.test.insert_one({ 'name': 'David' }, session=session)

#docs=db.test.find({}) #回傳空陣列，尚未進入交易，自己無法查到自己得資料，因為資料不在交易內
docs=db.test.find({}, session=session) #在交易中查詢
print(list(docs))

ret = input("enter '1' to commit, others rollback: ") #如果下ctrl+C 會鎖住 等待
if ret == "1":
    session.commit_transaction()
else:
    session.abort_transaction()