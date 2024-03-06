
def getmin(heap):
    item=heap[0]

    return item

def heapify(heap,size,i):
    minmum=i
    l=2*i+1
    r=2*i+2
    if l < size and heap[i] > heap[l]:
        minmum = l
    if r < size and heap[minmum] > heap[r]:
        minmum = r
    if minmum != i :
        heap[i],heap[minmum] =heap[minmum],heap[i]
        heapify(heap,size,minmum) 

def insert(heap,item):
    size=len(heap)
    if size == 0:
        heap.append(item)
    else :
        heap.append(item)
        size=len(heap)
        for i in range((size//2),-1,-1):
            heapify(heap,size,i)

def delete(heap,item):
    size=len(heap)
    i=0
    for i in range(0,size):
        if item == heap[i] :
            break   
    heap[i],heap[size-1]=heap[size-1],heap[i]
    heap.remove(item)
    size=len(heap)
    for i in range((size//2)-1,-1,-1):
        heapify(heap,size,i)

def 

heap=[]

insert(heap, 4)
insert(heap, 9)
insert(heap, 3)
insert(heap, 5)
insert(heap, 2)
insert(heap, 1)

print(heap)
print(getmin(heap))
print()
delete(heap,1)
print(heap)

