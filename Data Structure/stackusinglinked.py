class Node:
    def __init__(self,item):
        self.data=item
        self.next=None

class Stack:

    def __init__(self,):
        self.head=Node("head")
        self.size=0
        
    def getSize(self,):
        return self.size

    def isEmpty(self,):
        return self.size==0


    def peek(self,):
        return self.head.next.data

    def push(self,item):
        new_node=Node(item)
        if self.isEmpty() == None:
            self.head=new_node
            return 
        
        new_node.next=self.head.next
        self.head.next=new_node
        self.size+=1

    def pop(self,):
        if self.isEmpty() :
            print("Stack is Empty")
            return
        item=self.head.next.data
        self.head=self.head.next
        self.size-=1
        return item
    
    def print(self,):
        current=self.head.next
        while current :
            print(current.data)
            current=current.next

stack = Stack()
for i in range(1, 11):
    stack.push(i)

print(f"Stack: {stack.peek()}")
stack.print()

for _ in range(1, 6):
    remove = stack.pop()
    print(f"Pop: {remove}")

print(f"Stack: {stack.peek()}")
print(stack.getSize())
for _ in range(1, 8):
    remove = stack.pop()
    print(f"Pop: {remove}")

for i in range(1, 11):
    stack.push(i)
    print(f"Stack: {stack.peek()}")
    print(stack.getSize())