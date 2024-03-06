class circularqueue():

    def __init__(self,n):
        self.front=-1
        self.rear=-1
        self.n=n
        self.array=[None]*self.n

    def isempty(self,):
        return self.rear==self.front
    
    def isfull(self,):
       return ((self.rear + 1) % self.n == self.front) or (self.front==0 and self.rear==self.n-1)
             
    def enqueue(self,item):

        if self.isfull():
            print("Queue is full")
            return 
        
        if self.front==self.rear==-1:
            self.front=0
        self.rear=(self.rear+1)% (self.n)
        self.array[self.rear]=item

    def dequeue(self,):

        if self.front ==-1:
            print("Queue is Empty")

        if self.front==self.rear:
            item=self.array[self.front]
            self.array[self.front]=None
            self.front= -1
            self.rear= -1
            return item
        else:
            item=self.array[self.front]
            self.array[self.front]=None
            self.front=(self.front+1) %self.n
            return item
    
c=circularqueue(3)
c.enqueue(2)
print("c.array:",c.array)
print("c.front:",c.front)
print("c.rear:",c.rear)
c.enqueue(3)
print("c.array:",c.array)
print("c.front:",c.front)
print("c.rear:",c.rear)
c.enqueue(5)
print("c.array:",c.array)
print("c.front:",c.front)
print("c.rear:",c.rear)
c.enqueue(6)
print("c.enqueue(6):")
print("c.array:",c.array)
print("c.front:",c.front)
print("c.rear:",c.rear)
c.dequeue()
print("c.dequeue():")
print("c.array:",c.array)
print("c.front:",c.front)
print("c.rear:",c.rear)
c.enqueue(6)
print("c.array:",c.array)
print("c.front:",c.front)
print("c.rear:",c.rear)
c.dequeue()
print("c.dequeue():")
print("c.array:",c.array)
print("c.front:",c.front)
print("c.rear:",c.rear)

c.dequeue()
print("c.dequeue():")
print("c.array:",c.array)
print("c.front:",c.front)
print("c.rear:",c.rear)
c.dequeue()
print("c.array:",c.array)
print("c.front:",c.front)
print("c.rear:",c.rear)