class Node:

    def __init__(self,item):
        self.item = item
        self.color = 'Red'
        self.right = None
        self.left = None
        self.parent = None

class Traversal:
    
    def recursion_inorder(self,root):
        if root :
            self.recursion_inorder(root.left)
            print(f'{root.item} and {root.color}' , end='\n')
            self.recursion_inorder(root.right)

def leftRotate(root, x):
    y = x.right
    x.right = y.left

    if y.left is not None:
        y.left.parent = x

    y.parent = x.parent

    if x.parent is None:  # When checking up to the root
        root = y
    elif x == x.parent.left:  # If x was the left child
        x.parent.left = y
    else:  # If x was the right child
        x.parent.right = y

    y.left = x
    x.parent = y

    return root  # Return the modified root

def rightRotate(root, y):
    x = y.left
    y.left = x.right

    if x.right is not None:
        x.right.parent = y

    x.parent = y.parent

    if y.parent is None:
        root = x
    elif y == y.parent.left:
        y.parent.left = x
    else:
        y.parent.right = x

    x.right = y
    y.parent = x

    return root  # Return the modified root

def insertFix(root,new_node):

    while new_node.parent is not None and new_node.parent.color == 'Red':
        # print(f'new_node.parent{new_node.parent.item} and {new_node.parent.color}')
        if new_node.parent.parent is not None:
            if new_node.parent == new_node.parent.parent.left:
                y = new_node.parent.parent.right
                if y is not None and y.color == 'Red':
                    new_node.parent.color = 'Black'
                    y.color = 'Black'
                    new_node.parent.parent.color = 'Red'
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        root = leftRotate(root, new_node.parent)
                    new_node.parent.color = 'Black'
                    new_node.parent.parent.color = 'Red'
                    root = rightRotate(root, new_node.parent.parent)
            else:
                y = new_node.parent.parent.left
                if y is not None and y.color == 'Red':
                    new_node.parent.color = 'Black'
                    y.color = 'Black'
                    new_node.parent.parent.color = 'Red'
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        root = rightRotate(root, new_node.parent)
                    new_node.parent.color = 'Black'
                    new_node.parent.parent.color = 'Red'
                    root = leftRotate(root, new_node.parent.parent)

    root.color = 'Black'
    return root  # Return the modified root

def insert(root,item):

    new_node = Node(item)
    y = None 
    x = root #為了保持 root 不變，所以用替代的x當作root
    root.color='Black'
    while x is not None: #找到要插入的位置
        y = x
        if new_node.item < x.item:
            x = x.left
        else:
            x = x.right

    new_node.parent = y
        
    if y is None:
        root = new_node #最初沒有節點的時候，新的節點就是root
        
    elif new_node.item < y.item:
        y.left = new_node
    else:
        y.right = new_node
    print(f'insert:{item}')
    root=insertFix(root,new_node) #將整棵樹的root跟新增的new_node進行調整

    return root



root=Node(20)

root=insert(root,17)
root=insert(root,16)
root=insert(root,15)
root=insert(root,14)
root=insert(root,13)
root=insert(root,12)
root=insert(root,11)
root=insert(root,10)
T=Traversal()
T.recursion_inorder(root)
print()
print(root.item)
