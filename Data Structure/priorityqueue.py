

def heapify(array,n,i):
    largest=i
    l=2*i+1
    r=2*i+2
    if array[l]>array[i] and l < n:
        largest=l
    if  r < n and array[r]> array[largest]  :
        largest=r
    if largest!=i:
        temp=array[i]
        array[i]=array[largest]
        array[largest]=temp

def insert(array,node):
    if len(array)==0:
        array.append(node)
    else:
        array.append(node)
        n=(len(array)/2)-1
        n=int(n)
        size=len(array)
        for i in range(n,-1,-1):
            heapify(array,size,i)

def delete(array,node):
    n=len(array)
    m=int((len(array)/2)-1)
    if array[n-1] == node :
        array.pop()
    else:
        for i in range(0,len(array)-1):
            if array[i] == node:
                break 
        temp=array[i]
        array[i]=array[n-1]
        array[n-1]=array[i]
        array.pop()
        for i in range(m-1,-1,-1):
            heapify(array,n,i)



array=[]
insert(array,2)
insert(array,5)
insert(array,29)
insert(array,32)
insert(array,12)
insert(array,9)
insert(array,41)
delete(array,41)

print(array)



