class row_node:
    def __init__(self,row_number):
        self.row_number = row_number
        self.link_down = None 
        self.link_right = None 

class value_node:

    def __init__(self,col,value):
        self.column = col
        self.value = value 
        self.next = None

def create_value_link(start_row_node,j,value):
    new_node=value_node(j,value)

    if start_row_node.link_right == None :
        start_row_node.link_right = new_node
    else:
        s = start_row_node.link_right #將s 設為value node 的第一個
        while s.next : 
            s = s.next
        s.next=new_node

def create_row_link(start,Sparse_Matrix):
    for i in range(len(Sparse_Matrix)):
        new_row_node = row_node(i)
        
        if i == 0 :
            start = new_row_node
        else:
            d = start
            while d.link_down :
                d=d.link_down
            d.link_down=new_row_node

        for j in range(len(Sparse_Matrix[0])): #建立row 之後向右邊建立value node
            if Sparse_Matrix[i][j] != 0:
                create_value_link(new_row_node,j,Sparse_Matrix[i][j])
    
    return start

def printlink(start):

    s = start
    while s :
        if s.link_right != None : #判斷右邊有沒有node，如果該列都沒有value node，則此行的row start不會列印
            print("row:",s.row_number)
            r=s.link_right
            while r :
                print("column:",r.column,"value:",r.value)
                r=r.next
        s=s.link_down

"""
1.先建立 row link (直的)
2.在建立 value link(向右)
"""

Sparse_Matrix = [[ 0, 0, 3, 0, 4 ], 
                 [ 0, 0, 5, 7, 0 ], 
                 [ 0, 0, 0, 0, 0 ], 
                 [ 0, 2, 6, 0, 0 ]]

start=None

start= create_row_link(start,Sparse_Matrix)

printlink(start)