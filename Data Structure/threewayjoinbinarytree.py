#in the twowayjoin，root1 all nodes < root2  all nodes < root3 all nodes

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

def twowayjoin(root1,root2): 
    if root2 is None:
        return root1
    if root1 is None:
        return root2
    
    if root1.data < root2.data :
        root2.left= twowayjoin(root1,root2.left)
    elif root1.data > root2.data :
        root2.right = twowayjoin(root1,root2.right)
    
    return root2

def threewayjoin(root1,root2,root3): # since root3 all nodes > root2 all nodes >root1 all nodes,insert root1 and root3 into root2 and return root2
    root2=twowayjoin(root1,root2)
    root2=twowayjoin(root3,root2)
    return root2

def inorder(root):

    if root is None :
        return 
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)


root1=Node(10)
root2=Node(24)
root3=Node(35)

root1=insert(root1,17)
root1=insert(root1,9)
root1=insert(root1,8)
root1=insert(root1,12)
root1=insert(root1,1)
root1=insert(root1,18)
inorder(root1)
print()
root2=insert(root2,21)
root2=insert(root2,23)
root2=insert(root2,22)
root2=insert(root2,25)
inorder(root2)
print()
root3=insert(root3,31)
root3=insert(root3,33)
root3=insert(root3,32)
root3=insert(root3,36)
root3=insert(root3,34)
root3=insert(root3,39)
root3=insert(root3,40)
inorder(root3)
print()

print()
root2=threewayjoin(root1,root2,root3)
inorder(root2)