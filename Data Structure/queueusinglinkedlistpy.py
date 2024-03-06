class Node:
    
    def __init__(self,item):
        self.data = item
        self.next = None

class Queue:

    def __init__(self,):
        self.head = Node("head")
        self.rear = None
        self.front = None

    def enqueue(self,item):
        new_node=Node(item)
        if self.isempty() :
            self.head.next = new_node
            self.rear = new_node
            self.front = new_node
            return

        self.rear.next = new_node
        self.rear = new_node


    def dequeue(self,):
        if self.isempty():
            print("Queue is empty")
            return
        item = self.front.data
        self.front = self.front.next
        self.head = self.head.next

        return item
        
    def isempty(self,):
        return self.front == None
    
    def print(self,):
        current=self.head.next
        while current :
            print(current.data)
            current=current.next
        

queue = Queue()
for i in range(1, 5):
    queue.enqueue(i)

queue.print()
print(queue.front.data)
print(queue.rear.data)
queue.dequeue()
queue.dequeue()
queue.print()
print("="*20)
print(queue.front.data)
print(queue.rear.data)
queue.dequeue()
queue.print()
