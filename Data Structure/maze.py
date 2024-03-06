#老鼠走迷宮，使用linked list 實作stack

class Node:
    def __init__(self,):
        self.x=0
        self.y=0
        self.next=None

def push(x,y):
    global top
    new_node=Node()
    new_node.x=x
    new_node.y=y
    new_node.next=top
    top=new_node

def pop():
    global top
    top=top.next

def check(x,y,exitx,exity):
    if x==exitx and y==exity:
        return 1
    else:
        return 0
    
def next_step(maze):

    a=top.x
    b=top.y
    # print((a,b))
    if maze[a-1][b]==0: #如果maze[a-1][b]這個位置是0 ，0表示空地 ，上
        push(a-1,b)     #則將此位置放入堆疊，表示未來可以走訪的路
        maze[a-1][b]=2  #表示已經走訪過的路 
    elif maze[a][b-1]==0: #左
        push(a,b-1)
        maze[a][b-1]=2
    elif maze[a+1][b]==0: #下
        push(a+1,b)
        maze[a+1][b]=2
    elif maze[a][b+1]==0: #右
        push(a,b+1)
        maze[a][b+1]=2
    else:
        pop()

def find(maze,x,y,exitx,exity):
    global top
    head=Node()
    head.x=x
    head.y=y
    head.next=None
    top=head
    
    while check(top.x,top.y,exitx,exity)==0:
        next_step(maze)

    print("visited:")
    for i in range(10):
        for j in range(12):
            print(maze[i][j],end="")
        print()

maze=[[1,1,1,1,1,1,1,1,1,1,1,1],
      [1,0,0,2,1,1,1,1,1,1,1,1],
      [1,1,1,2,1,1,0,0,0,0,1,1],
      [1,1,1,1,1,1,0,1,1,0,1,1],
      [1,1,1,0,0,0,0,1,1,0,1,1],
      [1,1,1,0,1,1,0,1,1,0,1,1],
      [1,1,1,0,1,1,0,1,1,0,1,1],
      [1,1,1,1,1,1,0,1,1,0,1,1],
      [1,1,0,0,0,0,0,0,1,0,0,1],
      [1,1,1,1,1,1,1,1,1,1,1,1]]
x=1
y=1
exitx=8
exity=10

print('='*20)
print('迷宮爲:')
for i in range(10):
    for j in range(12):
        print(maze[i][j],end='')
    print()
print('='*20)
find(maze,x,y,exitx,exity)


