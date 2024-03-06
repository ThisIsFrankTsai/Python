
sparseMatrix = [[0,0,3,0,4],
                [0,0,5,7,0],
                [0,0,0,0,0],
                [0,2,6,0,0]]

size = 0 #non-zero element
 
for i in range(4):
    for j in range(5):
        if (sparseMatrix[i][j] != 0):
            size += 1

rows, cols = (3, size)
compactMatrix = [[0 for i in range(cols)] for j in range(rows)]

k = 0

for i in range(len(sparseMatrix)):
    for j in range(len(sparseMatrix[0])):
        if sparseMatrix[i][j] !=0 :
            compactMatrix[0][k]=i                   #row
            compactMatrix[1][k]=j                   #col
            compactMatrix[2][k]=sparseMatrix[i][j]  #value
            k+=1

for i in compactMatrix:
    print(i)