class node:

    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:

    def __init__(self,):
        self.head=node("head")

    def insertatbegin(self,data):
        new_node=node(data)
        if self.head.next is None:
            self.head=new_node
            return 
        else:
            new_node.next=self.head
            self.head=new_node

    def insertatend(self,data):
        new_node=node(data)
        current=self.head
        while current.next != None:
            current=current.next
        current.next=new_node

    def insertatindex(self,index,data):
        new_node=node(data)
        current=self.head
        i=0
        if i==index:
            self.insertatbegin(data)
        while current !=None and i!=index-1:
            current=current.next
            i+=1
        if current!=None:
            new_node.next=current.next
            current.next=new_node

    def updata_node(self,index,data):
        i=0
        current=self.head
        if index==i:
            self.head.data==data
        else:
            while current!=None and i!=index:
                current=current.next
                i+=1
            if current!=None:
                current.data=data 
            
    def remove_index_node(self,index):
        i=0
        current=self.head
        if i==index:
            self.remove_begin_node()
        else:
            while current != None and i != index-1:
                current=current.next
                i+=1
            if current!=None:
                current.next=current.next.next

    def remove_begin_node(self,):
        self.head=self.head.next
     
    def remove_last_node(self,):
        current=self.head
        while current.next.next!=None:
            current=current.next
        current.next=None
    
    def traversal(self,):
        current=self.head
        while current !=None:
            print(current.data)
            current=current.next

    def count(self,):
        count=0
        current=self.head
        while current:
            count+=1
            current=current.next
        return count
        
L=linkedlist()

L.insertatbegin(55)
L.insertatend(66)
L.insertatindex(1,33)
L.insertatend(77)
# L.traversal()
L.insertatbegin(44)
L.traversal()
print("L.updata_node(1,99)")
L.updata_node(1,99)
L.traversal()
print("L.remove_begin_node()")
L.remove_begin_node()
L.traversal()
print("L.remove_last_node()")
L.remove_last_node()
print("L.remove_last_node()")
L.insertatindex(3,56)
print("L.insertatindex(3,56)")
L.remove_index_node(1)
print("L.remove_last_node()")
L.remove_last_node()
L.traversal()
c=L.count()
print(c)