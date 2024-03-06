#Convert a Generic Tree(N-array Tree) to Binary Tree 
class Node:
    def __init__(self, item):
        self.data = item
        self.left = None #之後轉成二元樹要使用
        self.right = None
        self.children = [] #起初為n-array樹

def convert(root):
    if root is None :
        return None
    if len(root.children) == 0 :
        return root
    if len(root.children) == 1 : 
        root.left = convert(root.children[0])
        return root
    root.left = convert(root.children[0])
    root.right = convert(root.children[1])

    for i in range(2,len(root.children)): #決定左右節點之後，多餘的節點，依照順序掛在右節點的最左邊節點
        rightsubtreeroot = root.right
        while rightsubtreeroot.left != None :
            rightsubtreeroot = rightsubtreeroot.left
        rightsubtreeroot.left = convert(root.children[i])

    return root

def leftchildandrightsibling(root) :
    if root is None:
        return None
 
    # create a binary tree node with the data of the current node
    binary_node = Node(root.data)
 
    # convert the first child to a binary tree and set as left child of binary_node
    if root.children:
        binary_node.left = leftchildandrightsibling(root.children[0])
 
    # convert the next sibling to a binary tree and set as right child of binary_node
    current = binary_node.left
    for child in root.children[1:]:
        current.right = leftchildandrightsibling(child)
        current = current.right
    return binary_node


def inorder(root):
    if root is None :
        return None
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

root = Node('A')
root.children.append(Node('B')) #root 的 子樹
root.children.append(Node('C'))
root.children.append(Node('D'))
root.children.append(Node('L'))

root.children[0].children.append(Node('E')) #B的子樹
 
root.children[1].children.append(Node('F')) #C的子樹
root.children[1].children.append(Node('G'))
root.children[1].children.append(Node('H'))

root.children[2].children.append(Node('I')) #D的子樹
root.children[2].children.append(Node('J'))

root.children[2].children[1].children.append(Node('K')) #J的子樹

binaryTreeRoot = convert(root)
inorder(binaryTreeRoot)
print()
# print(binaryTreeRoot.data)
# print(binaryTreeRoot.left.data)
# print(binaryTreeRoot.right.data)
# print(binaryTreeRoot.right.left.data)
# print(binaryTreeRoot.right.right.data)
# print(binaryTreeRoot.right.left.left.data)
# print(binaryTreeRoot.right.right.left.data)
# print(binaryTreeRoot.right.left.left.left.data)
# print(binaryTreeRoot.right.left.left.right.data)
print()
method2=leftchildandrightsibling(root)
inorder(method2)
print()
# print(method2.data)
# print(method2.left.data)
# print(method2.left.left.data)
# print(method2.left.right.data)
# print(method2.left.right.left.data)
# print(method2.left.right.right.data)
# print(method2.right.left.left.data)
# print(method2.right.right.left.data)
# print(method2.right.left.left.left.data)
# print(method2.right.left.left.right.data)