class Node:

    def __init__(self,item):
        self.data = item
        self.right = None
        self.left = None

class Traversal:

    def recursion_inorder(self,root):
        if root :
            self.recursion_inorder(root.left)
            print(root.data, end=' ')
            self.recursion_inorder(root.right)

    def recursion_preorder(self,root):
        if root :
            print(root.data, end=' ')
            self.recursion_preorder(root.left)
            self.recursion_preorder(root.right)

    def recursion_postorder(self,root):
        if root :
            self.recursion_postorder(root.left)
            self.recursion_postorder(root.right)
            print(root.data, end=' ')
    
    def stack_inorder(self,root):

        stack=[]
        current=root
        while True :
            if current :

                stack.append(current)
                current=current.left

            elif stack :
                    current=stack.pop(-1)
                    print(current.data,end=" ")
                    current=current.right
            else:
                break

    def stack_preorder(self,root):
        stack=[]
        current=root
        stack.append(current)
        while stack:
         
            print(current.data,end=" ")
            if current.right :
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        
            current=stack.pop(-1)

    def top(self,stack):
        if len(stack)>0:
            return stack[-1]
        return None

    def stack_postorder(self,root):

        if root is None:
            return
        stack=[]
        current=root
        while True:
            while current:

                if current.right :
                    stack.append(current.right)
                stack.append(current)
                current=current.left
            
            current=stack.pop(-1)
            if current.right != None and self.top(stack) == current.right :
                stack.pop()
                stack.append(current)
                current=current.right
            else:
                print(current.data,end=" ")
                current = None
            if len(stack) <= 0:
                break
    
    def Levelorder(self,root) :#Breadth-First
        queue=[]
        current=root
        queue.append(current)
        while len(queue) != 0 :
            current=queue.pop(0) 
            print(current.data,end=" ")
             
            if current.left != None :
                queue.append(current.left)
            if current.right != None :
                queue.append(current.right)
              
    def Depth_first_traversal(self,root):
        if root is None:
           return
        else:
             print(root.data,end=" ")
             self.Depth_first_traversal(root.left)
             self.Depth_first_traversal(root.right)  



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


#Case 1. Delete a Leaf Node in BST
#Case 2. Delete a Node with Single Child in BST，Copy the child to the node and delete the node. 
#Case 3. Delete a Node with Both Children in BST，
#Copy contents of the inorder successor to the node, and delete the inorder successor.
def delete(root,key):
    if root is None :
        return None

    if root.data > key: #find the node to be delete by Recursive
        root.left = delete(root.left,key)
        return root
    elif root.data < key :
        root.right = delete(root.right,key)
        return root
    #one child or leaf node,here root is the key to be delete
    if root.left is None :
        temp = root.right
        del root
        return temp
    elif root.right is None :
        temp = root.left
        del root 
        return temp
    else: #two child
        parent = root
        successor = root.right #find the successor ,successor is the next node in inorder,位於右子樹的最左邊
        while successor.left is not None :
            parent = successor
            successor = successor.left
        
        if parent != root :
            parent.left = successor.right
        else :
            parent.right = successor.left
        
        root.data = successor.data
        del successor
        return root


root=Node(20)

r=insert(root,17)
r=insert(root,27)
r=insert(root,10)
r=insert(root,18)
# r=insert(root,21)
r=insert(root,23)
r=insert(root,22)
r=insert(root,25)

T=Traversal()
print("Inorder")
T.recursion_inorder(r)
print()
T.stack_inorder(r)
print()
print("Postorder")
T.recursion_postorder(r)
print()
T.stack_postorder(r)
print()
print("Preorder")
T.recursion_preorder(r)
print()
T.stack_preorder(r)
print()
print("BFS(Levelorder)")
T.Levelorder(r)
print()
print("DFS")
T.Depth_first_traversal(r)
print()
r=delete(r,10)
print("delete Inorder")
T.recursion_inorder(r)