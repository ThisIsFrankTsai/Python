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

def add(root1,root2):
    if not root1 :
        return root2
    if not root2 :
        return root1
    root1.data+=root2.data
    root1.left = add(root1.left,root2.left)
    root2.right = add(root1.right,root2.right)

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
inorder(r1)
print()
inorder(r2)
r3=add(r1,r2)
print()
inorder(r3)
