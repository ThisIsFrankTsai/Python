def restore(sparse): #三元序對轉為稀疏矩陣
    row = sparse[0][0]
    column = sparse[0][1]
    array = [[0] *column  for i in range(row)] #先建立空陣列，每一列有 column個0*共有row列
    k = 1 #從第一列開始 而非第0列開始

    while k<=sparse[0][2]:
        array[sparse[k][0]][sparse[k][1]]=sparse[k][2]
        k+=1

    return array

def store(array): #將稀疏矩陣儲存三元序對

    row=len(array) #計算三元陣列的total row
    column=len(array[0]) #計算三元陣列的total column
    s=[] #建立空的陣列
    count=0 #計算所有非0值

    for i in range(row):        #計算所有非0值
        for j in range(column):
            if array[i][j]!=0:
                count+=1
    
    s.append([row,column,count]) #儲存總數

    for i in range(row):            #將非0值儲存成三元序對
        for j in range(column):
            if array[i][j] !=0:
                s.append([i,j,array[i][j]])

    return s

def sparset(sparse):  #稀疏矩陣一般轉置
    k=0
    sparset=[]
    sparset.append([sparse[0][1],sparse[0][0],sparse[0][2]])
    
    while k<=sparset[0][1]:
        for i in sparse[1:]:
            if i[1]==k:
                sparset.append([i[1],i[0],i[2]])
        k+=1
    return sparset

def fastt(sparse): #稀疏矩陣快速轉置

    rowsize=[0 for _ in range(int(sparse[0][1]))] #用來統計原本矩陣 column有幾個0幾個1、
    rowstart=[0 for _ in range(int(sparse[0][1]))]
    sparset=[]   #建立轉置後的空陣列
    
    for _ in range(sparse[0][2]):   
        sparset.append([0,0,0])

    for i in sparse[1:]:                        #1.計算rowsize 統計矩陣column的出現次數
        rowsize[i[1]]+=1
    
    rowstart[0]=0 #固定填入0
    for i in range(1,int(sparse[0][1])):        #2.計算rowstart
        rowstart[i]+=rowsize[i-1]+rowstart[i-1]

    for i in sparse[1:]:                        #3.回到原三元序對，逐行檢查，轉置後對照rowstart放入相對應的位置，並且rowstart加1
        sparset[rowstart[i[1]]][0]=i[1]
        sparset[rowstart[i[1]]][1]=i[0]
        sparset[rowstart[i[1]]][2]=i[2]
        rowstart[i[1]]+=1

    sparset.insert(0,[sparse[0][1],sparse[0][0],sparse[0][2]]) #4.依照三元序對，第一列為total，將第一列放入

    return sparset


def add(sparse1,sparse2): #兩稀疏矩陣相加
    sparse3=[]
    i,j=1,1
    sparse3=[[sparse1[0][0],sparse1[0][1],0]]

    if sparse1[0][0] != sparse2[0][0] or sparse1[0][1] !=sparse2[0][1]:
        print("兩矩陣大小不同，無法相加")
        
    else:
        while i<=sparse1[0][2] and j<=sparse2[0][2]:
            if sparse1[i][0]==sparse2[j][0]:
                if sparse1[i][1]==sparse2[j][1]:
                    sparse3.append([sparse1[i][0],sparse2[j][1],sparse1[i][2]+sparse2[j][2]])
                    i+=1
                    j+=1
                    sparse3[0][2]+=1
                else:
                    if  sparse1[i][1] < sparse2[j][1]:
                        sparse3.append([sparse1[i][0],sparse1[i][1],sparse1[i][2]])
                        i+=1
                        sparse3[0][2]+=1
                    else:
                        sparse3.append([sparse2[j][0],sparse2[j][1],sparse2[j][2]])
                        j+=1
                        sparse3[0][2]+=1
            else:
                if  sparse1[i][0] < sparse1[j][0]:
                    sparse3.append([sparse1[i][0],sparse1[i][1],sparse1[i][2]])
                    i+=1
                    sparse3[0][2]+=1
                else:
                    sparse3.append([sparse2[j][0],sparse2[j][1],sparse2[j][2]])
                    j+=1
                    sparse3[0][2]+=1


        return sparse3

def multi(sparse1,sparse3) : #兩稀疏矩陣相乘
    s1row=sparse1[0][0]
    s1col=sparse1[0][1]
    s3row=sparse3[0][0]
    s3col=sparse3[0][1]
    sparse4=[] 
    c=0   #計算總共非零項
    if s1col!=s3row:
        print("大小不同，無法相乘")
    else:
        sparse4.append([s1row,s3col,0]) #將總共的行列數append入新的matrix

        for i in sparse1[1:]: #遍歷sparse1的非0元素
            total=0
            for j in sparse3[1:]: #遍歷sparse3的非0元素
                if i[1]==j[0]: #大小相同就相乘
                    k=j[1]
                    total+=i[2]*j[2]
            if total !=0:
                sparse4.append([i[0],k,total])    
                c+=1   

        sparse4[0][2]=c

        return sparse4     

sparse1 = [
             [5, 6, 4], 
             [1, 2, 3], 
             [2, 1, 6],
             [3, 1, 9], 
             [4, 5, 12]
          ]

sparse2=[
        [5,6,5],
        [1,2,7],
        [2,5,2],
        [3,4,4],
        [4,2,2],
        [4,5,5]
        ]

sparse3=[
            [6, 6, 4], 
            [1, 2, 3], 
            [2, 1, 6],
            [5, 4, 9], 
            [5, 5, 12]
        ]

array = restore(sparse1)
print("給定三元序對，還原矩陣:",array)
store(array)
three=store(array)
print("給定稀疏矩陣，轉成三元序對:",three)#依照row major 排序

martixt1=sparset(sparse1)
print("給定三元序對，使用一般轉置法轉成三元序對:",martixt1) #依照row major排序
matrixt=fastt(sparse1)
print("給定稀疏矩陣的三元序對，使用快速矩陣轉置法轉置:",matrixt)

addmatrix=add(sparse1,sparse2)
print("給定兩個三元序對，相加:",addmatrix)
multimatrix=multi(sparse1,sparse3)
print("給定兩個三元序對，相乘:",multimatrix)