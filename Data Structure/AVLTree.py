class AVLtree():

    def __init__(self,key):
        self.key=key
        self.right=None
        self.left=None
        self.h=1

    def insert(self,root,key):

        if root==None:
            root=AVLtree(key)
            return root

        if key<root.key:
            root.left=self.insert(root.left,key)
        else:
            root.right=self.insert(root.right,key)

        root.h=1+max(self.Height(root.left),self.Height(root.right))

        balancefactor=self.balance(root)

        if balancefactor >1: #由下往上從第一個不平衡的地方開始整理
            if key>root.left.key:   #子樹為 ：左左右
                return self.rightrotate(root) #看root的走向決定right or left
            else:
                root.left=self.leftrotate(root.left)#子樹為：左左左
                return self.rightrotate(root)
        if balancefactor<-1:
            if key>root.right.key:          #子樹為：右右右
                return self.leftrotate(root)
            else:
                root.right=self.rightrotate(root.right) #子樹為：右右左
                return self.leftrotate(root)

        return root

    def delete(self,root,key):
        
        if not root:
            return root
        elif key<root.key: #用遞迴的方式一直往下找key
            root.left=self.delete(root.left,key)
        elif key>root.key:
            root.right=self.delete(root.right,key)
        else:
            if root.left is None: #只有一個leaf,直接交換即可
                temp=root.right
                root=None
                return temp
            elif root.right is None : #只有一個leaf,直接交換即可
                temp=root.left
                root=None
                return temp
            #如果root的部份有比較多的子node
            temp=self.getmin(root.right) #用遞迴的方式,找到右邊子樹的最小值 
            root.key=temp.key #跟root交換
            root.right=self.delete(root.right,temp.key) #原本的右邊最小值 刪除

        if root is None :
            return root

        root.h=1+max(self.Height(root.left),self.Height(root.right)) #重新計算高度

        balancefactor=self.balance(root)

        if balancefactor>1: #左邊比較深
            if key<root.left.key:  
                return self.rightrotate(root)
            else:
                root.left=self.leftrotate(root.left)
                return self.rightrotate(root)
            
        if balancefactor<-1: #右邊比較深
            if key>root.left.key:
                return self.leftrotate(root)
            else:
                root.right=self.rightrotate(root.right)
                return self.leftrotate(root)
        
        return root

    def rightrotate(self,root):
        x=root.left
        y=x.right
        x.right=root
        root.left=y

        root.height=1+max(self.Height(root.left),self.Height(root.right))
        x.height=1+max(self.Height(x.left),self.Height(x.right))

        return x

    def leftrotate(self,root):
        print("root.key",root.key)
        x=root.right
        print("x.key",x.key)
        y=x.left
        x.left=root
        root.right=y

        root.height=1+max(self.Height(root.left),self.Height(root.right))
        x.height=1+max(self.Height(x.left),self.Height(x.right))

        return x

    def balance(self,root):
        #計算factor要從下往上算
        if not root: 
            return 0
        return self.Height(root.left)-self.Height(root.right)

    def Height(self,root):
        if not root:
            return 0
        return root.h
    
    def getmin(self,root):
        if root is None or root.left is None:
            return root
        return self.getmin(root.left) #小的一定在左邊

    def display(self,root): #inorder
        if root :
            self.display(root.left)
            print(root.key,end="->")
            self.display(root.right)

if __name__ == '__main__':

    AVL=AVLtree(0)
    root=None
    root=AVL.insert(root,33)
    root=AVL.insert(root,44)
    root=AVL.insert(root,55)
    root=AVL.insert(root,11)
    root=AVL.insert(root,22)
    root=AVL.insert(root,9)
    root=AVL.insert(root,88)

    AVL.display(root)
    print("\n------------------------------")
    AVL.delete(root,22)

    AVL.display(root)


