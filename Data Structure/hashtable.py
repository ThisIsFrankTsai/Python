# Python program to demonstrate working of HashTable 

hashTable = [[],] * 10 #10個slot

def checkPrime(n):
    #print(n)
    if n == 1 or n == 0:
        return 0 #False

    for i in range(2, n//2): #n//2 floor function ,11 無法被整除,所以會一直回傳false
        if n % i == 0:
            return 0

    return 1 #回傳


def getPrime(n):
    if n % 2 == 0:
        n = n + 1 #奇數

    while not checkPrime(n):  #checkPrime 回傳false時 執行n=n+2 然後在進入迴圈
        n += 2

    return n


def hashFunction(key): #設計function 將資料放入相對應的位置
    capacity = getPrime(10) #因為n=10 所以固定回傳 capacity=11
    #print(capacity)
    return key % capacity


def insertData(key, data):
    index = hashFunction(key)
    #print(index)
    hashTable[index] = [key, data] #覆蓋原有的data

def removeData(key):
    index = hashFunction(key)
    hashTable[index] = 0

insertData(123, "apple")
insertData(432, "mango")
insertData(213, "banana")
insertData(654, "guava")

print(hashTable)
insertData(123, "Frank") # 覆蓋原有的data

print(hashTable)

removeData(123)

print(hashTable)