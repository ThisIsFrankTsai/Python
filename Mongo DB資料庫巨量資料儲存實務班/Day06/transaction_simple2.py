import pymongo
client = pymongo.MongoClient(['localhost:20000', 'localhost:20001', 'localhost:20002'])
db = client.test

def transaction(session): # 失敗的時候出現錯誤事件
    db.test.insert_one({ 'name': 'David' }, session=session)
    ret = input("enter '1' to commit, others rollback: ")#如果crtl+C 中斷，直接下abort
    if ret != "1":
        raise ValueError  

try: 
    with client.start_session() as session:#進入session，如果程式當掉。即不正常離開 rollback，資料保護較好
        with session.start_transaction(): #start_transaction
            transaction(session) #按1，正常離開 commit
except:
    print('transaction fail') #非1， 不正常 abort


