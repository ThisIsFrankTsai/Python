sparse = [
             [5, 6, 4], 
             [1, 1, 3], 
             [2, 3, 6],
             [3, 2, 9], 
             [4, 4, 12]
          ]

k=1
sparset=[]
sparset.append(sparse[0])
while k<=sparse[0][2]:
    sparset.append([sparse[k][1],sparse[k][0],sparse[k][2]])
    k+=1
print(sparset)