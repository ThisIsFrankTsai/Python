class Node:
    def __init__(self, item):
        self.next = None
        self.child = None
        self.data = item

def addchild(root,item):
    
    if root == None :
        return None
    if root.child == None :
        new_node = Node(item) 
        root.child = new_node
        return root.child
    else:
        return addsibling(root.child,item)

def addsibling(node,item):
    new_node=Node(item)
    if node == None :
        return None
    while node.next  :
        node=node.next
    node.next=new_node
    return node.next

#DFS
def traverse(root):
    if root == None:
        return None
    while root :
        print(root.data,end=" ")
        if root.child :
            traverse(root.child)
        root=root.next


root = Node(10) 
n1 = addchild(root, 2) 
n2 = addchild(root, 3) 
n3 = addchild(root, 4) 
n4 = addchild(n3, 6) 
n5 = addchild(root, 5) 
n6 = addchild(n5, 7) 
n7 = addchild(n5, 8) 
n8 = addchild(n5, 9) 

traverse(root)