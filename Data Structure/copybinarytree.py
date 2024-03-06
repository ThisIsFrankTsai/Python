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

    if root == None :
        return

    inorder(root.left)
    print(str(root.data)+"-",end="")
    inorder(root.right)

def copy(root):

    if root == None :
        return

    copy_node = Node(root.data)
    copy_node.left = copy(root.left)
    copy_node.right = copy(root.right)

    return copy_node


root=Node(20)

r=insert(root,17)
r=insert(root,27)
r=insert(root,10)
r=insert(root,18)
r=insert(root,21)
r=insert(root,25)

inorder(root)
print()
copy_root = copy(root)

inorder(copy_root)