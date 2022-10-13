#Node按照順序由上至下 由左至右排列

class Node:

    def __init__(self,item):
        self.item=item
        self.leftchild=self.rightchild=None
        
    def calculate(self,root):
        if root is None:
            return 0
        return 1+self.calculate(root.leftchild)+self.calculate(root.rightchild)

    def isCompleteBinaryTree(self,root,index,count):

        if root is None:
            return True #如果中間都沒有問題,最後檢查到root 會回傳True 
        if index>=count:
            return False
            #index大於count表示,有node沒有按照順序排列

        return (self.isCompleteBinaryTree(root.leftchild,2*index+1,count) and
               self.isCompleteBinaryTree(root.rightchild,2*index+2,count))
        #遞迴的方式會按照順序計算每個葉子節點的index,最後再與count比較




if __name__ == '__main__':
    
    n=Node(0)
    index=0

    root=Node(11)
    root.rightchild=Node(77)
    root.leftchild=Node(44)
    root.leftchild.leftchild=Node(33)
    root.leftchild.rightchild=Node(66)
    root.rightchild.rightchild=Node(55)
    root.rightchild.leftchild=Node(22)
    # root.leftchild.rightchild.leftchild=Node(99)

    print(n.isCompleteBinaryTree(root,index,n.calculate(root)))