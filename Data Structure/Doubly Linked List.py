class Node:
    def __init__(self,item):
        self.item=item
        self.next=None
        self.prev=None
        self.head=None

    def traverse(self,head):
        while head!=None:
            print(head.item,end="->")
            head=head.next

    def InsertionattheBeginning(self,item,head):
        new_node=Node(item)
        # #當不知道 指向哪個位置的時候 可以print出來 避免亂猜
        # print("self.head",self.head) #attribute 的 head
        # print("head",head) #丟近來的head
        # print("new_node.head",new_node.head) #new_node 的head def __init__ 預設為None
        # print("self.prev",self.prev) #attribute 的 prev
        # print("head.prev",head.prev) # 丟近來的head的prev
        # print("new_node.prev",new_node.prev) #new_node 的prev def __init__ 預設為None
        # print("self.next",self.next) #attribute 的 next
        # print("head.next",head.next) # 丟近來的head的next
        # print("new_node.next",new_node.next) #new_node 的next def __init__ 預設為None
        # print("new_node",new_node) #new_node address
        new_node.next=head
        #new_node.next=self.head 錯誤寫法,因為self.head 為attribute 故為none
        head.prev=new_node
        head=new_node
        # print("==========after change=========")
        # #self.head=new_node #self. 為調用def__init__內的attribute
        # print("self.head",self.head) #attribute的 head
        # print("head",head) #丟近來的head ,更改為 head=new_node new_node 的address
        # print("new_node.head",new_node.head) #
        # print("self.prev",self.prev) #attribute的prev
        # print("head.prev",head.prev) # 丟近來的head的prev
        # print("new_node.prev",new_node.prev) #因為是開頭所以指向None
        # print("self.next",self.next) #attribute的 next
        # print("head.next",head.next) # 因head=new_node 為 new_node的next 也就是 原本的head
        # print("new_node.next",new_node.next)#指向 原來head
        return head

    def Insertioninbetweentwonodes(self,item,head,node):
        new_node=Node(item)
        while head.item!=node: #插入 node 之後
            head=head.next   
        # print(head.item)
        # print(head.next.item)
        new_node.next=head.next
        head.next=new_node 
        new_node.prev=head
        new_node.next.prev=new_node #set new_node 的下一個的prev為new_node
        # print("Insertioninbetweentwonodes")
        # print(head.item)
        # print(head.next.item)
        # print(head.prev.item)
        # print(new_node.item)
        # print(new_node.next.item)
        # print(new_node.prev.item)

    def InsertionattheEnd(self,head,item):
        new_node=Node(item)
        while head.next!=None:
            head=head.next
        head.next=new_node
        new_node.prev=head
        # print(head.item)
        # print(new_node.item)
    
    def DeletetheFirstNodeofDoublyLinkedList(self,head):
        head=head.next
        head.prev=None
        
        return head

    def DeletionoftheInnerNode(self,head,item): 
        while head.item!=item :
            head=head.next
        # print(head.item)
        # print(head.next.item)
        # print(head.prev.item)
        # print(head.next.prev.item)
        # print(head.prev.next.item)

        head.next.prev=head.prev
        head.prev.next=head.next

        # print("DeletionoftheInnerNode")
        # print(head.item)
        # print(head.next.item)
        # print(head.prev.item)
        # print(head.next.prev.item)
        # print(head.prev.next.item)

    def DeletetheLastNodeofDoublyLinkedList(self,head):
        while head.next!=None:
            head=head.next
        head.prev.next=None


if __name__ == '__main__' :
    n=Node(99)
    head=Node(44)
    second=Node(69)
    third=Node(77)
    
    head.next=second
    head.prev=None
    second.next=third
    second.prev=head
    third.next=None
    third.prev=second

    head=n.InsertionattheBeginning(36,head)
    n.Insertioninbetweentwonodes(61,head,44)
    n.InsertionattheEnd(head,55)
    head=n.DeletetheFirstNodeofDoublyLinkedList(head)
    n.DeletionoftheInnerNode(head,69)
    n.DeletetheLastNodeofDoublyLinkedList(head)

    n.traverse(head)