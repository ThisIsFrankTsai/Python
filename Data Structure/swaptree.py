#swap each node every level

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

def inorder(root):
    if root :
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)

def swap(level,root):
    if root == None or (root.left is None and root.right is None ):
        return
    
    root.left,root.right = root.right,root.left
    
    swap(level+1,root.left)
    swap(level+1,root.right)


root=Node(20)

r=insert(root,17)
r=insert(root,27)
r=insert(root,10)
r=insert(root,18)
r=insert(root,21)
r=insert(root,25)
inorder(r)
print()
swap(1,r)
inorder(r)
