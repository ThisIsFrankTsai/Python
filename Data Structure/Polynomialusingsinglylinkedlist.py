class Node:
    def __init__(self,coefficient,pow):
        self.coefficient = coefficient
        self.pow = pow
        self.next = None

class Polynomial: 
    def add(self,p1,p2):
        new_node=Node(0,0)
        cur = new_node
        cur1 = p1
        cur2 = p2

        while  cur1 != None and cur2 != None:

            if cur1 == None:
                cur.next=p2
                break
            elif cur2 == None:
                cur.next = cur1
                break
            elif cur1.pow == cur2.pow :
                cur.next = Node(cur1.coefficient + cur2.coefficient,cur1.pow)
                cur1 = cur1.next
                cur2 = cur2.next
            elif cur1.pow > cur2.pow :
                cur.next = Node(cur1.coefficient,cur1.pow)
                cur1 = cur1.next
            elif cur2.pow > cur1.pow :
                cur.next = Node(cur2.coefficient,cur2.pow)
                cur2 = cur2.next
            
            cur = cur.next 
        
        return new_node.next

        
#建立多項式
start1=None
cur1=None
start2=None
cur2=None

list1_coeff = [ 5, 4, 2 ]; 
list1_pow = [ 2, 1, 0 ]; 
n = len(list1_coeff); 
i=0
while n>0:
    a=list1_coeff[i]
    b=list1_pow[i]
    ptr=Node(a,b)
    if start1 == None :
        start1 = ptr
        cur1 = ptr
    else :
        cur1.next=ptr
        cur1=ptr

    i+=1
    n-=1

cur1=start1
while cur1 != None:
    print(cur1.coefficient,"x^",cur1.pow, sep = "", end = "")
    cur1=cur1.next  
    if cur1 == None:
        break
    print(" + ", end="")
print()

list2_coeff = [ -5, -5 ,7 ]; 
list2_pow = [ 3,1, 0 ]; 
n = len(list2_coeff); 
i=0
while n>0:
    a=list2_coeff[i]
    b=list2_pow[i]
    ptr=Node(a,b)
    if start2 == None :
        start2 = ptr
        cur2 = ptr
    else :
        cur2.next=ptr
        cur2=ptr
        
    i+=1
    n-=1

cur2=start2

while cur2 != None:
    print(cur2.coefficient,"x^",cur2.pow, sep = "", end = "")
    cur2=cur2.next  
    if cur2 == None:
        break
    print(" + ", end="")
print()

p=Polynomial()

start3=p.add(start1,start2)
cur=start3
while cur != None:
    print(cur.coefficient,"x^",cur.pow, sep = "", end = "")
    cur=cur.next  
    if cur == None:
        break
    print(" + ", end="")

print()
