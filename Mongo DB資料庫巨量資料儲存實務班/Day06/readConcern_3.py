import pymongo
from pymongo.write_concern import WriteConcern
from pymongo.read_concern import ReadConcern
import time

hosts = ['localhost:20000', 'localhost:20001', 'localhost:20002']
client = pymongo.MongoClient(hosts, readPreference='secondary') #readPreference讀從 secondary，但不指定
db = client.test

db.test.drop()
for  n in range(100):
    # Primary 寫資料

    result=db.test.with_options(
        write_concern=WriteConcern(w='majority', j=True) #w預設majority超過一半節點(Primaryru加上Secondary),w=1，只要Prumary寫入 client就會收到訊息，但secondary有沒有寫入未知
    ).insert_one({'name': 'aaa','n':n})                        #True:資料要寫到硬碟才會回應 Falase:寫到記憶體就會回應

    id=None
    if result.acknowledged:
        id=result.inserted_id #回傳id
    else:
        print('error') #寫入失敗

    # Secondary 讀資料
    doc = db.test.with_options(
        read_concern=ReadConcern(level='local') #level:預設local,local:本地有資料就回傳，實際有沒有寫到大部分機器不管
    ).find({'_id':id}) #回傳list

    print(list(doc)) #回傳Secondary的結果，None 自己寫的資料自己讀不到
    time.sleep(1) #讓資料延緩寫入讀取
    

