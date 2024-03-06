class Node:
    def __init__(self,item):
        self.data = item
        self.left = None
        self.right = None

def insert(root,item):
    new_node = Node(item)
    if root == None :
        return new_node
    
    if root.data == item :
        return root
    elif root.data < item :
        root.right = insert(root.right,item)
    else :
        root.left = insert(root.left,item)

    return root 

def equal(root1,root2):

    if root1 == None and root2 == None :
        return True
    elif root1 != None and root2 == None :
        return False
    elif root1 == None and root2 != None :
        return False
    
    if (root1.data == root2.data and equal(root1.left,root2.left) and equal(root1.right,root2.right)):
        return True
    else :
        return False

    


root1=Node(20)

r=insert(root1,17)
r=insert(root1,27)
r=insert(root1,10)
r=insert(root1,18)
r=insert(root1,21)
r=insert(root1,25)

root2=Node(20)

r=insert(root2,17)
r=insert(root2,27)
r=insert(root2,10)
r=insert(root2,18)
r=insert(root2,21)
r=insert(root2,25)

ans = equal(root1,root2)
print(ans)