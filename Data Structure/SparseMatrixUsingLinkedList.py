class Node :
    def __init__(self,row,column,data):
        self.row = row 
        self.column = column
        self.data = data
        self.next = None

class Sparse:
    def __init__(self,):
        self.head = None
        self.temp = None
        self.sizes = 0
    
    def size(self,):
        return self.sizes
    
    def isempty(self,):
        return self.sizes == 0
    
    def create(self,row,column,data):
        new_node=Node(row,column,data)

        if self.isempty():
            self.head=new_node
        else:
            self.temp.next=new_node
        self.temp=new_node
        self.sizes+=1


    def printtuple(self,):
        temp = self.head
        while temp :
            print("("+str(temp.row)+","+str(temp.column)+","+str(temp.data)+")",end=" ")
            temp=temp.next

    def printarray(self,):
        temp = r = s =self.head
        print("row_position:", end=" ")
        while temp != None :
            print(temp.row,end=" ")
            temp=temp.next
        print()
        print("column_postion:", end=" ")
        while r != None :
            print(r.column,end=" ")
            r=r.next
        print()
        print("Value:", end=" ")
        while s != None :
            print(s.data,end=" ")
            s=s.next
        print()

s = Sparse()
sparseMatric = [[0, 0, 3, 0, 4],
                [0, 0, 5, 7, 0],
                [0, 0, 0, 0, 0],
                [0, 2, 6, 0, 0]]

for i in range(len(sparseMatric)):
    for j in range(len(sparseMatric[0])):
        if sparseMatric[i][j] != 0:
            s.create(i,j,sparseMatric[i][j])

s.printtuple()