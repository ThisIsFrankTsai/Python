
from platform import node


class Node:
    def __init__(self,item):
        self.item=item
        self.next=None
        self.head=None
        
if __name__ == '__main__' :
    head=Node(1)
    second=Node(22)
    third=Node(333)
    
    head.next=second
    second.next=third


while head!=None:
    print(head.item,end="->")
    head=head.next





