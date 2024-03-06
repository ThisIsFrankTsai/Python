A = [10, 5, 20, 40]
L=0 
R=1 
Value=10
for i in range(L,R+1):
  A[i] = A[i] + Value
print(A) # [20, 15, 20, 40]

L=1 
R=3 
Value=20
for i in range(1,4):
  A[i] = A[i] + Value
print(A) #  [20, 35, 40, 60]]

A = [10, 5, 20, 40]
print("origin array =",  A) # origin array = [10, 5, 20, 40]
lenghtA = len(A)
DiffArray = [0]*(lenghtA+1)
DiffArray[0] = A[0]
for i in range(1, lenghtA):
    DiffArray[i] = A[i] - A[i-1]
print("DA =", DiffArray) # DA = [10, -5, 15, 20, 0]