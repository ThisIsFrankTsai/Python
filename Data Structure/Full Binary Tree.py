class Node :
    def __init__(self,item):
        self.item=item
        self.leftchild=None
        self.rightchild=None

    def isFullBinaryTree(self,root):
        if root is None:
            return True
        if root.leftchild is None and root.rightchild is None:
            return True
        
        if root.leftchild is not None and root.rightchild is not None:
            return self.isFullBinaryTree(root.leftchild) and self.isFullBinaryTree(root.rightchild) 
        
        return False


if __name__ == '__main__':

    n=Node(0)

    root=Node(11)
    root.rightchild=Node(77)
    root.leftchild=Node(44)
    root.leftchild.leftchild=Node(33)
    root.leftchild.rightchild=Node(66)
    root.rightchild.rightchild=Node(55)
    root.rightchild.leftchild=Node(22)

    print(n.isFullBinaryTree(root))
    
    



