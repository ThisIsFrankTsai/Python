class Node :
    def __init__(self,item):
        self.item=item
        self.leftchild=None
        self.rightchild=None

    def search(self,item):


        return node

    def insert(self,root,item):
        
        if root==None:
            return Node(item)

        if item<root.item:
            root.leftchild=self.insert(root.leftchild,item)
        else:
            root.rightchild=self.insert(root.rightchild,item)

        return root
    
    def min(self,root):
        temp=root
        
        while temp.leftchild != None:
            temp=temp.leftchild
        
        return temp

    def deletion(self,root,item):
        if root==None:
            return
        #Find Node
        if item<root.item:
            root.leftchild=self.deletion(root.leftchild,item)
        elif (item>root.item):
            root.rightchild=self.deletion(root.rightchild,item)
        else:
        #找到該node 且該root 只有一個child
            if root.leftchild is None:
                temp=root.leftchild
                root=None
                return temp
            elif root.rightchild is None:
                temp=root.rightchild
                root=None
                return temp
        #找到該node 且該root 有2個child

            temp=self.min(root.rightchild)
            
            root.item=temp.item
            
            root.rightchild=self.deletion(root.rightchild,temp.item) #重複同樣的動作在一次刪除

        return root

    def inorder(self,root):

        if root :
            self.inorder(root.leftchild)
            print(root.item,end="->")
            self.inorder(root.rightchild)

    def preorder(self,root):
        if root :
            print(root.item,end="->")
            self.inorder(root.leftchild)
            self.inorder(root.rightchild)


if __name__ == '__main__':

    n=Node(99)
    root=None

    # root=n.insert(root,18)
    # root=n.insert(root,55)
    # root=n.insert(root,75)
    # root=n.insert(root,33)
    # root=n.insert(root,99)
    root = n.insert(root, 8)
    root = n.insert(root, 3)
    root = n.insert(root, 1)
    root = n.insert(root, 6)
    root = n.insert(root, 7)
    root = n.insert(root, 10)
    root = n.insert(root, 14)
    root = n.insert(root, 4)
    n.inorder(root)
    print("\n===================================")
    n.deletion(root,3)
    n.inorder(root)