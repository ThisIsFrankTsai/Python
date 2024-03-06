class Node:
    def __init__(self,item):
        self.data=item
        self.next=None

class Linkedlist:

    def __init__(self,):
        self.head=Node("head")

    def insertatbegin(self,data):
        new_node=Node(data)
        if self.head.next is None:
            self.head=new_node
            new_node.next=self.head

            return 

        current=self.head
        while current.next != self.head :
            current=current.next

        current.next=new_node
        new_node.next=self.head
        self.head=new_node       

    def insertatend(self,data):
        new_node=Node(data)
        current=self.head

        if self.head.next == self.head :
            self.head.next=new_node
            new_node.next=self.head
            return
        
        while current.next != self.head:
            current=current.next
        current.next=new_node
        new_node.next=self.head

    def insertatindex(self,index,data):
        new_node=Node(data)
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
        current=self.head
        while current.next != self.head:
                current=current.next
        current.next=self.head.next
        self.head=self.head.next

    def remove_end_node(self,):
        current=self.head
        while current.next.next!=self.head:
            current=current.next
        current.next=self.head
    
    def traversal(self,):
        current=self.head
        while current.next != self.head:
            print(current.data)
            current=current.next
        print(current.data)
L=Linkedlist()
L.insertatbegin(55)
L.insertatend(33)
L.insertatbegin(36)
L.insertatindex(1,44)
L.insertatindex(1,77)
L.insertatindex(1,88)
L.traversal()
L.remove_end_node()
L.traversal()
L.remove_index_node(1)
L.traversal()