class Multiqueue:

    def __init__(self,k,array_length):
        self.number_of_queue=k
        self.array_length=array_length
        self.array=[None]*array_length
        self.front=[-1]*k
        self.rear=[-1]*k 
        self.free=0
        self.next_array=[i for i in range(1,array_length)] #存放下一個空的index
        self.next_array.append(-1)

    def enqueue(self,queue_num,item):
        if self.isfull(queue_num):
            print("Queue is Full")
            return 
        next_free=self.next_array[self.free] #找出下一個free的位置
        if self.isempty(queue_num):        #該queue第一次放入，如果都沒有放入任何元素，則初始化front=rear=0
            self.front[queue_num]=self.rear[queue_num]=self.free
        else:
            self.next_array[self.rear[queue_num]]=self.free 
            self.rear[queue_num]=self.free                  #如果已經放入過元素，rear往前推進
        self.next_array[self.free] = -1 #表示該位置不能再放入
        self.array[self.free] = item    #將item 放入queue
        self.free = next_free           #free往前推進


    def dequeue(self,queue_num):
        if self.isempty(queue_num):
            print("Queue is empty")
            return
        front_index=self.front[queue_num]
        self.front[queue_num]=self.next_array[front_index]
        self.next_array[front_index]=self.free
        self.free=front_index
        return self.array[front_index]


    def isempty(self,queue_num):
        return True if self.front[queue_num] == -1 else False

    def isfull(self,queue_num):
        return True if self.free == -1 else False 

ks =  Multiqueue(3, 6) 
        
# Let us put some items in queue number 2  
ks.enqueue(0,15 ) 
print(ks.array)
print(ks.array_length)
print("ks.free:",ks.free)
print("ks.front:",ks.front)
print("ks.rear:",ks.rear)
print("ks.next_array:",ks.next_array)
ks.enqueue(0,25 ) 
print(ks.array)
print(ks.array_length)
print("ks.free:",ks.free)
print("ks.front:",ks.front)
print("ks.rear:",ks.rear)
print("ks.next_array:",ks.next_array)
# ks.enqueue(0,45 ) 
# ks.enqueue(0,35 ) 
# print(ks.array)
# print(ks.array_length)
# print("ks.free:",ks.free)
# print("ks.front:",ks.front)
# print("ks.rear:",ks.rear)
# print("ks.next_array:",ks.next_array)

# ks.enqueue(45, 2)

# # Let us put some items in queue number 1  
# ks.enqueue(17, 1);  
# ks.enqueue(49, 1);  
# ks.enqueue(39, 1);  
        
# # Let us put some items in queue number 0  
# ks.enqueue(11, 0);  
# ks.enqueue(9, 0);  
# ks.enqueue(7, 0);  
           