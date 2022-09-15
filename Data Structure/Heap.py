def heapify(array, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2 
    
    if l < n and array[i] < array[l]:
        largest = l
    
    if r < n and array[largest] < array[r]:
        largest = r
    
    if largest != i:
        array[i],array[largest] = array[largest],array[i]
        heapify(array, n, largest)

def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum);
        for i in range((size//2)-1, -1, -1):
            heapify(array, size, i)

def delete(array, num):
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break
        
    array[i], array[size-1] = array[size-1], array[i]

    array.remove(num)
    
    for i in range((len(array)//2)-1, -1, -1):
        heapify(array, len(array), i)
    

array=[]
insert(array,25)
insert(array,35)
insert(array,15)
insert(array,5)
insert(array,55)
insert(array,75)
insert(array,65)
insert(array,100)
print ("Max-Heap array: " + str(array))
delete(array,100)
print("After deleting an element: " + str(array))





         
 