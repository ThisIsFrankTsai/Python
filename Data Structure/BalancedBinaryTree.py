
class Node:

    def __init__(self,item):
        self.item=item
        self.leftchild=self.rightchild=None
        
    def calculate(self,root):
    #if root is None return 0
        if root==None:
            return 0
        #find height of left subtree
        l=self.calculate(root.leftchild)
        #find the height of right subtree
        r=self.calculate(root.rightchild)  
        #find max of land r, add 1 to it and return the value
   
        if l>r:
            return l+1
        else:
            return r+1

    def isBalancedBinaryTree(self,root):

        if root is None:
            return True #如果中間都沒有問題,最後檢查到root 會回傳True 

        value=self.calculate(root)
        #計算tree的高度

        lheight=self.calculate(root.leftchild)
        rheight=self.calculate(root.rightchild)

        lcheck=self.isBalancedBinaryTree(root.leftchild)
        rcheck=self.isBalancedBinaryTree(root.rightchild)

        if abs(lheight-rheight)>1:
            return False
        
        if lcheck==True and rcheck==True:
            return True


        


if __name__ == '__main__':
    
    n=Node(0)

    root=Node(11)
    root.rightchild=Node(77)
    root.leftchild=Node(44)
    root.leftchild.leftchild=Node(33)
    root.leftchild.rightchild=Node(66)
    root.rightchild.rightchild=Node(55)
    #root.rightchild.rightchild.rightchild=Node(22)
    root.leftchild.rightchild.leftchild=Node(99)

    print(n.isBalancedBinaryTree(root,))