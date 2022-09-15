class Heap: 
    def __init__(self,):
        pass   
    def Heapify(self,array):
        n=len(array)
        m=(n//2)-1
        for i in range(m,-1,-1):
            largest=i
            l=2*i+1
            r=2*i+2
            if  array[l]>array[i]:
                largest=l
            if 2*i+2<n :    #當 i=0 l=1 r=2 但是size=2
                if array[r]>array[largest]:
                    largest=r
            if largest!=i:
                array[i],array[largest]=array[largest],array[i]
                self.Heapify(array)

    def insert(self,array,item):
        n=len(array)
        if n==0:
            array.append(item)
        else :
            array.append(item)
            self.Heapify(array)

    def delete(self,array,item):
        n=len(array)
        if array[-1]==item :
            array.remove(item)
        else:
            for i in range(0,n):
                if item==array[i]  :
                    break
            
        array[i],array[-1]=array[-1],array[i]
        array.remove(item)
        self.Heapify(array)

    def Peek(self,array):
        min=array[0]
        return min
    def display(self,array):
        return print(array)


array=[]
H=Heap()
H.insert(array,25)
H.insert(array,35)
H.insert(array,15)
H.insert(array,5)
H.insert(array,55)
H.insert(array,75)
H.insert(array,65)
H.insert(array,100)
H.display(array)

H.delete(array,100)
H.display(array)
print(H.Peek(array))



         
 