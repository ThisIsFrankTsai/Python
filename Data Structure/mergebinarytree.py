
class Node:
    def __init__(self,item):
        self.data = item
        self.right = None
        self.left = None

def insert(root,item):
    new_node=Node(item)

    if root is None :
        return new_node
    else:
        if root.data == item:
            return root 
        elif root.data < item:
            root.right=insert(root.right,item)
        else:
            root.left=insert(root.left,item)
    return root

def bsttoarr(root,array):
    if not root:
        return 
    array.append(root.data)
    bsttoarr(root.right,array)
    bsttoarr(root.left,array)

    return array
#method 先轉成 array 後再插入另外一棵樹
def merge1(root1,array2):
    i=0
    while  i<len(array2) :
        insert(root1,array2[i])
        i+=1
    return root1
#不轉成array 直接插入另外一棵樹
def merge2(root1,root2):
    insert(root1,root2.data)
    insert(root1,root2.left.data)
    insert(root1,root2.right.data)

    return root1

def inorder(root):
    if root is None :
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

root1 =Node(20)
root2 =Node(15)
array1 =[]
array2 =[]


r1=insert(root1,17)
r1=insert(root1,27)
r1=insert(root1,10)
r1=insert(root1,18)
r1=insert(root1,21)
r1=insert(root1,25)

r2=insert(root2,7)
r2=insert(root2,23)
r2=insert(root2,5)
r2=insert(root2,14)

array1=bsttoarr(r1,array1)
array2=bsttoarr(r2,array2)

print(array1)
print(array2)

root1=merge1(root1,array2)
inorder(root1)
print()
root1=merge2(root1,root2)
inorder(root1)

