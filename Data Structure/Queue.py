

def creat():
    q=[]
    return q

def enqueue(q,item):
    q.append(item)
    return q

def checkempty(q):
    return len(q)

def checkfull(q):
    if len(q)==Max:
        return "queue is full" 

def dequeue(q):
    if (checkempty(q))==0:
        return "queue is empty"
    else:
        q.pop(0)
        return q

i=0
Max=10
q=creat()
enqueue(q,10)
enqueue(q,20)
enqueue(q,30)
enqueue(q,40)
enqueue(q,50)
enqueue(q,60)

print(q)

print(dequeue(q))