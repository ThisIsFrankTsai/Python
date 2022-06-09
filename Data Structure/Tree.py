"""
For BFS, use queue; For DFS, use stack or recursion
"""
class node:
    def __init__(self,item):
        self.right=None
        self.left=None
        self.var=item

def inorder(root):
    if root :
        inorder(root.left)
        print(str(root.var)+"->",end='')
        inorder(root.right)

def preorder(root):
    if root:
        print(str(root.var)+"->",end='')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.var)+"->",end='')

if __name__ == '__main__' :

    root=node(2)
    root.left=node(5)
    root.right=node(9)
    root.left.right=node(10)
    root.left.right.left=node(3)
    root.right.left=node(8)
    
    inorder(root)
    print("\n")
    preorder(root)
    print("\n")
    postorder(root)