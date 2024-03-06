class Node:
    def __init__(self,item):
        self.data= item
        self.next = None

class add: 
    def add(self,p1,p2):
        cur1 = p1
        cur2 = p2
        if p1 ==None :
            return p2
        elif p2==None:
            return p1
        else :
            while cur1.next!=None:
                cur1=cur1.next
            cur1.next=p2
            return p1

        
#建立多項式
start1=None
cur1=None
start2=None
cur2=None

list1 = [ 5, 4, 2 ]; 
n = len(list1); 
i=0
while n>0:
    a=list1[i]
    ptr=Node(a,)
    if start1 == None :
        start1 = ptr
        cur1 = ptr
    else :
        cur1.next=ptr
        cur1=ptr

    i+=1
    n-=1

cur1=start1
while cur1 !=None:
    print(cur1.data, sep = "", end = "")
    if cur1.next != None:  # 如果回到了起始節點，結束列印
        print(" + ", end="")
    cur1=cur1.next      
print()
list2 = [ -5, -5 ,7 ]; 
n = len(list2); 
i=0
while n>0:
    a=list2[i]

    ptr=Node(a)
    if start2 == None :
        start2 = ptr
        cur2 = ptr
    else :
        cur2.next=ptr
        cur2=ptr
        
    i+=1
    n-=1

cur2=start2

while cur2 !=None:
    print(cur2.data, sep = "", end = "")
    if cur2.next != None:  # 如果回到了起始節點，結束列印
        print(" + ", end="")
    cur2=cur2.next      
print()
a=add()

start3=a.add(start1,start2)
cur=start3
while cur !=None:
    print(cur.data, sep = "", end = "")
    if cur.next != None:  # 如果回到了起始節點，結束列印
        print(" -> ", end="")
    cur=cur.next      
print()
