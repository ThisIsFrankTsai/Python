import math
import time

class Node:
    
    def __init__(self):
        self.next=None
        self.prev=None
        self.parent=None
        self.child=None
        self.degree=-1 #Consolidate() 需要合併相同degree的tree
        self.key=-1 #default value
        self.mark='' # Black or white mark of the node
        self.f='' #flag for Find function 如果有一個child 被刪除則標記 如果被標記又被刪除則升格為tree

    def Insertion(self,data):
        global nodes,min
        nodes+=1

        new_node=Node()
        new_node.prev=new_node
        new_node.next=new_node
        new_node.key=data
        new_node.f='N'
        new_node.mark='W'

        if min !=None:
            min.prev.next=new_node
            new_node.next=min
            new_node.prev=min.prev
            min.prev=new_node
            if new_node.key <min.key:
                min=new_node
        else:
            min=new_node

    def Fibonnaci_link(self,ptr3,ptr): #
        #ptr3所指的node 因為比較大所以會成為ptr的子樹因此 ptr3的前一個 node要重新連結到ptr
        ptr3.prev.next=ptr3.next 
        ptr3.next.prev=ptr3.prev
        if ptr.next==ptr: #如果root只剩下一個
            min=ptr
        #成為子樹後重新接上link
        ptr3.prev=ptr3 
        ptr3.next=ptr3
        ptr3.parent=ptr
        if ptr.child ==None: #如果此時ptr的node沒有child
            ptr.child=ptr3
        #跟ptr的child接上,位置放在ptr child的左邊
        ptr3.next=ptr.child
        ptr3.prev=ptr.child.prev
        ptr.child.prev.next=ptr3
        ptr.child.prev=ptr3
        if ptr3.key<ptr.child.key: #比較child跟新的child node大小,小的當child
            ptr.child=ptr3
        ptr.degree+=1

    def Consolidate(self): #合併
        global min,nodes
        #建立一個空array 大小不超過degree

        temp=math.log2(nodes) #temp用來指定array的大小
        temp=int(temp)
        array=[None]*(temp+1)
        for i in range(temp+1):
            array[i]=None
        ptr=min
        ptr2=ptr #ptr2當作指標,min開始跑,一直往下
        while True:
            ptr2=ptr2.next #逐步檢查 所有tree 的degree
            temp1=ptr.degree #將ptr所指的node的degree儲存起來
            while array[temp1] !=None: #發現有重複degree 就會進入 合併
                ptr3=array[temp1] #用來指 array內的node
                if (ptr.key)>ptr3.key: #比較root的大小
                    ptr4=ptr
                    ptr =ptr3
                    ptr3=ptr4
                if ptr3==min:
                    min=ptr

                self.Fibonnaci_link(ptr3,ptr) #ptr3>ptr,將兩個degree相同的node進行合併
                if ptr.next == ptr: #只剩下一個root
                    min=ptr
                array[temp1]=None #合併之後 degree增加 舊的array清空
                temp1+=1 #往下一個 degree檢查
                       
            array[temp1]=ptr #將 ptr所指的node儲存在array裡
            ptr=ptr.next#持續往右邊一一check 是否可以合併 

            if (ptr==min) :  #繞一圈 root
                break    
        min=None
        #跳出while迴圈表示array內的點都不能在合併 沒有相同的degree,接下來就是把
        #array內的node全部連接起來
        for i in range(temp+1) :
            if (array[i] !=None):
                array[i].prev=array[i]
                array[i].next=array[i]
                if (min!=None): #如果存在 min,則將node 加到 min的左邊
                    min.prev.next=array[i]
                    array[i].next=min
                    array[i].prev=min.prev
                    min.prev=array[i]
                    if array[i].key<min.key:
                        min=array[i]
                    
                else:
                    min=array[i]
                if min==None:
                    min=array[i]
                elif array[i].key<min.key:
                    min=array[i]

    def Find_min(self):
        global min
        print(end="\n")
        
        return print(min.key)

    def ExtractMin(self): #刪掉最小值
        global min,nodes 
        #print("in extract_min",min.key)
        if min==None:
            print("Empty")
        else:
            temp=min 
            pntr=temp
            x=None
            if temp.child!=None:
                x=temp.child #min的其中一個child 
                while True: #如果min 有小孩則將小孩一個一個升格到root
                    pntr=x.next
                    min.prev.next=x #將min 提升到 原來min 的左邊
                    x.next=min
                    x.prev=min.prev
                    min.prev=x
                    if x.key <min.key: #比較decrease的key跟原來的min key
                        min=x
                    x.parent=None
                    x=pntr
                    if(pntr==temp.child): #如果min又找到一開始指向的child 則表示所有的child都已經成為root
                        break

            temp.prev.next=temp.next #刪掉最小值,左右link重新連結
            temp.next.prev=temp.prev
            min=temp.next

            if temp==temp.next and temp.child==None: #剛好只有一個的時候
                min=None
            else:
                min=temp.next

                self.Consolidate()

            nodes-=1

    def Cut(self,found,temp): # found=子,temp=父
        global min
        if found ==found.next : #子 及 子的右邊
            temp.child=None  

        found.prev.next=found.next #將兒子(found)節點 拉至與原來的父親(temp)節點平行 並且左右鍊結
        found.next.prev=found.prev
        
        if (found==temp.child):
            temp.child=found.next #原本temp.child 指向temp其中一個child,現在child 被刪除,因此指向其他child 

        temp.degree=temp.degree-1 #父親 少一個子節點
        found.next=found #少了父親節點，且被提昇為父親節點,重新連結左右的link
        found.prev=found
        min.prev.next=found #將found 加入min的左邊
        found.next=min #接上link
        found.prev=min.prev
        min.prev=found
        found.parent=None #提昇為父親節點 與min水平
        found.mark='B'#標示
 
    def Cascase_cut(self,temp):
        
        ptr=temp.parent
        if (ptr !=None) : #存在父親節點
            if temp.mark =='W' : #父親節點為w, 如果父親節點不曾刪除過小孩則 改為B
                temp.mark ='B'
            else:               #如果父親節點曾經刪除過小孩,則將父親節點也排到root區
                self.Cut(temp,ptr)
                self.Cascase_cut(ptr)

    def Decrease_key(self,item,found): 
        global min
        if min==None:
            print("empty")
        
        if found==None:
            print("Not Found")

        found.key=item #找到後設為item
        temp=found.parent #為了之後跟parent做比較 #found=child temp=child

        if temp != None and found.key<temp.key : #父親非空 且父親值大於小孩值
            self.Cut(found,temp ) #父親跟兒子做分割
            self.Cascase_cut(temp)

        if found.key<min.key : #新的值如果比較小就交換小的當min
            min=found
    
    def Find(self,item,min,val): #找到值,並且將值設定為我們想要的值
        
        found=None
        temp=min
        temp.f='Y' #預設'Y' 表示沒有找過
        found_ptr=None
        if (temp.key==item) : #如果min 就是我們要找的值
            found_ptr=temp
            temp.f='N' #找到後設為N
            found=found_ptr
            self.Decrease_key(val,found)
        
        if (found_ptr==None): # 如果min 找不到則
            if (temp.child != None): #找min 的小孩
                self.Find(item,temp.child,val) #遞迴一直找小孩
            if (temp.next.f != 'Y'):#找min 的右邊
                self.Find(item,temp.next,val) #遞迴一直找右邊
        
        temp.f='N' #找到後設為N
        found=found_ptr #遞迴的中止條件

    def Deletion(self,item): #不直接刪掉 Decrease key 降為0 後,在ExtractMin
        global min
 
        if min==None:
            print("empty")
        else:
            #在執行ExtractMin將其刪除
            self.Find(item,min,0)
            self.ExtractMin()
            print("\ndeleted")

    #display   
    def display(self,min):
        first=min
        if min==None:
            print("empty")
        else:
            while True :
                print(min.key,end="->")
                min=min.next
                # if min != first:
                #     print("->",end='')
                    
                if min.key==first.key :
                    break

if __name__ == '__main__':
    
    array=[]
    n=Node()
    nodes=0
    min=None #min 為一指標,一直指向最小的Node

    n.Insertion(33)
    n.Insertion(77)
    n.Insertion(11)
    n.Insertion(44)
    n.Insertion(2)
    n.display(min)

    # #n.Deletion(77)
    n.ExtractMin()
    
    print("\n==============")
    n.display(min)
    print("\n==============")
    n.Find(77,min,0)
    n.display(min)
    print("\n==============")
    n.Deletion(44)
    n.display(min)
    print("\n==============")
    