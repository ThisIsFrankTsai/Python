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

    if root is None :
        return 
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

def store(root,total):

    if root is None :
        return 
    store(root.left,total)
    total.append(root.data)
    store(root.right,total)
    return total

def arraytobst(array): #create a blance binary tree，always create a node using middle of array
    if not array :
        return None
    mid=len(array)//2
    root=Node(array[mid])
    root.left = arraytobst(array[:mid])
    root.right = arraytobst(array[mid+1:])
    return root

def split(root,key):
    total=[]
    total=store(root,total)
    bst1=[]
    bst2=[]
    for i in total:
        if i<key:
            bst1.append(i)
        else:
            bst2.append(i)
    root1=arraytobst(bst1)
    root2=arraytobst(bst2)
    return root1,root2

root=Node(20)

root=insert(root,17)
root=insert(root,27)
root=insert(root,10)
root=insert(root,18)
root=insert(root,21)
root=insert(root,23)
root=insert(root,22)
root=insert(root,25)
root=insert(root,7)
root=insert(root,9)
inorder(root)
print()
r1,r2=split(root,20)
inorder(r1)
print()
inorder(r2)

