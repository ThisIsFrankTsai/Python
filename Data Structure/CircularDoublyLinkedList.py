class Node:
    def __init__(self,item):
        self.data=item
        self.prev=None
        self.next=None

class Linkedlist :

    def __init__(self,):
        self.head=Node("head")
        self.size=0
        
    def insertatbegin(self,item):
        new_node=Node(item)
        if self.isempty():
            self.head=new_node
            new_node.next=new_node
            new_node.prev=new_node
            self.size+=1
            return
        
        current=self.head
        while current.next != self.head :
            current=current.next
        
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node
        new_node.prev=current
        current.next=new_node
        self.size+=1

    def insertatend(self,item):
        new_node=Node(item)
        if self.isempty():
            self.head=new_node
            new_node.next=new_node
            new_node.prev=new_node
            self.size+=1
            return
        
        current=self.head
        while current.next != self.head :
            current=current.next
        current.next=new_node
        new_node.prev=current
        new_node.next=self.head
        self.head.prev=new_node
        self.size+=1

    def insertatindex(self,index,item):
        new_node=Node(item)
        i=0
        if self.isempty():
            self.head=new_node
            self.size+=1
            return
        if index==0:
            self.insertatbegin(item)
            return
        current=self.head
        
        while i != index :
            current=current.next
            i+=1
        current.prev.next=new_node     
        new_node.prev=current.prev 
        new_node.next=current 
         
        current.prev=new_node
        
        self.size+=1

    def removeatbegin(self,):
        if self.isempty():
            print("Linked List is Empty")
            return
        current = self.head
        while current.next !=self.head :
            current=current.next
        self.head.next.prev=current
        current.next=self.head.next
        self.head=self.head.next
        self.size-=1

    def removeatend(self,):
        if self.isempty():
            print("Linked List is Empty")
            return
        current=self.head
        while current.next != self.head :
            current=current.next
        current.prev.next=self.head
        self.head.prev=current.prev

        self.size-=1

    def removeatindex(self,index):
        if self.isempty():
            print("Linked List is Empty")
            return
        i=0
        current=self.head
        while i!= index :
            current=current.next
            i+=1
        current.prev.prev.next=current
        current.prev=current.prev.prev
        self.size-=1

    def updata_node(self,index,item):
        current=self.head
        i=0
        while i!=index:
            current=current.next
            i+=1
        current.prev.data=item

    def isempty(self,):
        return  self.size==0

    def print(self,):
        current=self.head
        while current.next != self.head:
            print(current.data)
            current=current.next
        print(current.data)

L=Linkedlist()
L.insertatbegin(77)
L.insertatend(88)
L.insertatend(99)
L.insertatbegin(55)
L.insertatindex(1,66)
L.insertatindex(0,7)

L.print()     
print("="*50)
L.removeatbegin()
L.print()
print("="*50)
L.removeatindex(2)
L.removeatend()
L.print()
print("="*50) 
L.updata_node(2,2)
L.print()  