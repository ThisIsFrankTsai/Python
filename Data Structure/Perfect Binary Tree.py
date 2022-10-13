from itertools import count
import time


class Node :
    def __init__(self,item):
        self.item=item
        self.leftchild=self.rightchild=None

    def calculate(self,node):
        d=0
        while(node!=None): #只有root 就會加1
            d+=1
            node=node.leftchild
            
        return d

    def isPerfectBinaryTree(self,root,d,level=0):

        if root is None : #連root都沒有的時候
            print("if root is None :")
            return True
        if root.leftchild is None and root.rightchild is None:

            return (d==level+1) #比較如果d跟level+1相等則回傳True,也就是走訪的深度一樣
        
        if root.leftchild is None or root.rightchild is  None:  #只有一邊有葉子 
            return False
        
        return  (self.isPerfectBinaryTree(root.leftchild,d,level+1) 
                 and self.isPerfectBinaryTree(root.rightchild,d,level+1) )


if __name__ == '__main__':
    
    n=Node(0)

    root=Node(11)
    root.rightchild=Node(77)
    root.leftchild=Node(44)
    root.leftchild.leftchild=Node(33)
    root.leftchild.rightchild=Node(66)
    root.rightchild.rightchild=Node(55)
    root.rightchild.leftchild=Node(22)

    print(n.isPerfectBinaryTree(root,n.calculate(root)))
    
    



