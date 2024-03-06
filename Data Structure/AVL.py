#https://www.geeksforgeeks.org/insertion-in-an-avl-tree/
class Node:

    def __init__(self,item):
        self.data = item
        self.right = None
        self.left = None
        self.height = 1

class Traversal:
    
    def recursion_inorder(self,root):
        if root :
            self.recursion_inorder(root.left)
            print(root.data, end=' ')
            self.recursion_inorder(root.right)

def getHeight(root,):

    if not root: 
            return 0
    return root.height 

def getBalance(root,):

    if not root: 
        return 0
    return getHeight(root.left) - getHeight(root.right) 

def leftRotate(root,):
    y = root.right 
    x = y.left 

    # Perform rotation 
    y.left = root 
    root.right = x 

    # Update heights 
    root.height = 1 + max(getHeight(root.left), 
                        getHeight(root.right)) 
    y.height = 1 + max(getHeight(y.left), 
                        getHeight(y.right)) 

    # Return the new root 
    return y 
  

def rightRotate(root,):
    y = root.left 
    x = y.right 

    # Perform rotation 
    y.right = root 
    root.left = x 

    # Update heights 
    root.height = 1 + max(getHeight(root.left), 
                    getHeight(root.right)) 
    y.height = 1 + max(getHeight(y.left), 
                    getHeight(y.right)) 

    # Return the new root 
    return y 

def getMinValueNode(root):
    if root is None or root.left is None:
        return root
 
    return getMinValueNode(root.left)
 

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

    root.height = 1 + max(getHeight(root.left), 
                           getHeight(root.right)) 
    
    balance = getBalance(root) 

    # Case 1 - Left Left 
    if balance > 1 and item < root.left.data: 
        return rightRotate(root) 
  
    # Case 2 - Right Right 
    if balance < -1 and item > root.right.data: 
        return leftRotate(root) 
  
    # Case 3 - Left Right 
    if balance > 1 and item > root.left.data: 
        root.left = leftRotate(root.left) 
        return rightRotate(root) 
  
    # Case 4 - Right Left 
    if balance < -1 and item < root.right.data: 
        root.right = rightRotate(root.right) 
        return leftRotate(root) 

    return root

def delete(root,item):
    if not root:
        return root
    elif item < root.data:
        root.left = delete(root.left, item)
    elif item > root.data:
        root.right = delete(root.right, item)
    else: #Now,find the item in the tree
        if root.left is None: #only right child
            temp = root.right
            root = None
            return temp

        elif root.right is None: #only left child
            temp = root.left
            root = None
            return temp
        #the item node has two child
        temp = getMinValueNode(root.right) #find the inorder sequence next node
        root.data = temp.data #this root will be delete
        root.right = delete(root.right,temp.data) #exchange the root node and inorder next node,then delete

    if root is None:
        return root
    #renew root's height
    root.height = 1 + max(getHeight(root.left),getHeight(root.right))
 
    # Step 3 - Get the balance factor
    balance = getBalance(root)

    # Step 4 - If the node is unbalanced, 
    # then try out the 4 cases
    # Case 1 - Left Left
    if balance > 1 and getBalance(root.left) >= 0:
        return rightRotate(root)

    # Case 2 - Right Right
    if balance < -1 and getBalance(root.right) <= 0:
        return leftRotate(root)

    # Case 3 - Left Right
    if balance > 1 and getBalance(root.left) < 0:
        root.left = leftRotate(root.left)
        return rightRotate(root)

    # Case 4 - Right Left
    if balance < -1 and getBalance(root.right) > 0:
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root
 
root=Node(20)

r=insert(root,17)
r=insert(root,27)
r=insert(root,10)
r=insert(root,9)
r=insert(root,23)
r=insert(root,21)
r=insert(root,25)
r=insert(root,8)
T=Traversal()

T.recursion_inorder(r)
r=delete(root,20)
print()
T.recursion_inorder(r)

print("\nFinal root's data:", root.data)