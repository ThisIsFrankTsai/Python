"""
Push: Add an element to the top of a stack
Pop: Remove an element from the top of a stack
IsEmpty: Check if the stack is empty
IsFull: Check if the stack is full
Peek: Get the value of the top element without removing it
"""
"""
1.A pointer called TOP is used to keep track of the top element in the stack.
2.When initializing the stack, we set its value to -1 so that we can check if the stack is empty by comparing TOP == -1.
3.On pushing an element, we increase the value of TOP and place the new element in the position pointed to by TOP.
4.On popping an element, we return the element pointed to by TOP and reduce its value.
5.Before pushing, we check if the stack is already full
6.Before popping, we check if the stack is already empty
"""

def creat():
    s=[]
    return s

def check(s):
    return  len(s)==0
        

def push(s,item):
    s.append(item)

def pop(s):
    if (check(s)) :
        return "stack is empty"
    return s.pop()


s=creat()
push(s,30)
push(s,23)
push(s,19)
push(s,9)
push(s,41)
push(s,55)
push(s,57)

for i in range(len(s)):
    print(pop(s))
