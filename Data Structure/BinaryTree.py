"""
For BFS, use queue; For DFS, use stack or recursion
"""
class node:
    def __init__(self,item):
        self.right=None
        self.left=None
        self.var=item
 
    def inorder(self):
        if self.left:
            self.left.inorder()        
        print(str(self.var)+"->",end='')
        if self.right :
            self.right.inorder()

    def preorder(self):
        print(str(self.var)+"->",end='')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(str(self.var)+"->",end='')
        
if __name__ == '__main__' :

    root=node(2)
    root.left=node(5)
    root.left
    root.right=node(9)
    root.left.right=node(10)
    root.left.right.left=node(3)
    root.right.left=node(8)

    print("\ninoder:",end="")
    root.inorder()
    print("\npreorder:",end="")
    root.preorder()
    print("\npostorder:",end="")
    root.postorder()
    print("\nBFS:",end="")


   