class Node:

    def __init__(self,item):
        self.data = item
        self.right = None
        self.left = None
        self.lthread = True #no child
        self.rthread = True #no child

class Traversal:

    def inordersuccessor(self,ptr): #sucessor is node's next node in inorder  always in the right subtree

        if ptr.rthread == True :  # no right child
            return ptr.right

        ptr = ptr.right
        while ptr.lthread == False :
            ptr=ptr.left
        return ptr
    

    def inorder(self,root):

        if root == None :
            return "Tree is empty"

        ptr = root

        while ptr.lthread == False : # having left child，inorder starting from leftmost
            ptr=ptr.left
        
        while ptr != None :
            print(ptr.data,end=" ")
            ptr=self.inordersuccessor(ptr)

def insert(root,item):
    new_node=Node(item)
    ptr=root
    parent=None
    while ptr != None: #until find empty place
        if item == ptr.data :
            print("data already exists")
            return root
        parent=ptr
        if item < ptr.data : 
            if ptr.lthread == False : #if ptr.lthread ,it is mean ptr's node  have left child
                ptr=ptr.left
            else:   #if ptr.lthread == True ,it is mean find the empty place 
                break
        else :
            if ptr.rthread == False :
                ptr=ptr.right
            else:
                break

    #and then connect thread     
    if parent == None : # No node in the tree
        root=new_node
        new_node.left=None
        new_node.right=None
    elif item < parent.data :
        new_node.left=parent.left
        new_node.right=parent
        parent.lthread=False #beacuse exists left child
        parent.left=new_node
    else  :
        new_node.right = parent.right
        new_node.left = parent
        parent.rthread = False #when parent have right child
        parent.right = new_node

    return root 


def delete(root,item):
    parent = None #指向要被刪除的node 的parent
    ptr = root #指向要被刪除的node
    found = 0 
    while ptr != None :
        if item == ptr.data :
            found = 1
            break
        parent=ptr
        if item < ptr.data :
            if ptr.lthread ==False:
                ptr=ptr.left
            else : 
                break
        else :
            if ptr.rthread == False :
                ptr=ptr.right
            else :
                break

    if found == 0:
        print("not found") 
    elif ptr.lthread == False and ptr.rthread == False : #have two child
        root=deleteC(root,parent,ptr)
    elif ptr.rthread ==False :                           #only have right child
        root=deleteB(root,parent,ptr)
    else :                                               #only have left child
        root=deleteA(root,parent,ptr)
    
    return root

def sucessor(ptr): # Returns inorder successor 
    if ptr.rthread == True :#if ptr no right child 
        return ptr.right
    ptr=ptr.right
    while ptr.lthread == False : #find the leftmost node in the ptr's right subtree
        ptr = ptr.left 

    return ptr

def predecessor(ptr):
    if ptr.lthread == True : #No left child
        return ptr.left
    ptr=ptr.left
    while ptr.rthread == False :
        ptr = ptr.right

    return ptr

def deleteA(root,parent,ptr): 
    if parent == None :
        root = None
    elif ptr == parent.left :
        parent.lthread = True
        parent.left = ptr.left
    else :
        parent.rthread =True
        parent.right = ptr.right
    
    return root

def deleteB(root,parent,ptr):
    child = None
    if ptr.lthread==False : # Node to be deleted has  child.
        child = ptr.left
    else:
        child = ptr.right 
    
    if parent == None : # Node to be deleted is root Node.
        root=child
    elif ptr == parent.left:
        parent.left=child
    else:
        parent.right=child

    # Find ptr's successor and predecessor
    s=sucessor(ptr)
    p=predecessor(ptr)
    
    if ptr.lthread == False : # have left child
        p.right=s
    elif ptr.rthread == False : # have right child
        s.left=p

    return root

def deleteC(root,parent,ptr):
    parentsucessor=ptr
    sucessor=ptr.right
    while sucessor.lthread == False :
        parentsucessor=sucessor
        sucessor=sucessor.left
    ptr.data = sucessor.data
    if sucessor.lthread ==True and sucessor.rthread == True :
        root = deleteA(root,parentsucessor,sucessor)
    else:
        root=deleteB(root,parentsucessor,sucessor)
    
    return root



root=Node(20)
T=Traversal()
r=insert(root,17)
r=insert(root,27)
r=insert(root,10)
r=insert(root,18)
r=insert(root,21)
r=insert(root,25)
T.inorder(r)
print()
delete(r,17)
T.inorder(r)


