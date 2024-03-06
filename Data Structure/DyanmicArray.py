import ctypes

class DynamicArray:

    def __init__(self,):
        self.n=0
        self.capacity=1
        self.a=self.make_array(self.capacity)

    def __len__(self,):
        return self.n
    
    def __getitem__(self,k):

        if 0>k or k>= self.n :
            return "K is out of index"
        
        return self.a[k]
    
    def append(self,element):
        if self.n==self.capacity:
            self.resize(2*self.capacity)
        
        self.a[self.n]=element
        self.n+=1
    
    def insert(self,element,index):

        if 0>index or index>self.n:
            return "out of index"

        if self.n == self.capacity:
            self.resize(2*self.capacity)
        
        for i in range(index,self.n):
            self.a[i+1]=self.a[i]

        self.a[index]=element
        self.n+=1

    def delete(self,):
        if self.n==0:
            return "No element in the array"
        self.a[self.n-1]=0
        self.n-=1

    def remove(self,index):

        if self.n==0:
            return "array is empty"

        if 0>index or index>self.n:
            return "out of index"
        
        for i in range(index,self.n-1):
            self.a[i]=self.a[i+1]
        
        self.a[self.n-1]=0
        self.n-=1

    def resize(self,capacity):
        b=self.make_array(capacity)

        for i in range(self.n):
            b[i]=self.a[i]
        
        self.a=b
        self.capacity=capacity
    
    def make_array(self,capacity):
        return (capacity*ctypes.py_object)()
    

a=DynamicArray()

a.append(1)
a.append(2)
a.append(3)

print(len(a))

for i in range(len(a)):
    print(f"a[{i}]={a[i]}")

a.insert(5,2)

for i in range(len(a)):
    print(f"a[{i}]={a[i]}")

print(a[3])

a.remove(2)
for i in range(len(a)):
    print(f"a[{i}]={a[i]}")
