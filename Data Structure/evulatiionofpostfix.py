
global top

def create_stack(exp):
    global top
    stack=[None]*len(exp)     
    top =-1
    return stack

def push(s,item):
    global top
    if is_full(s):
        return "stack is full"
    top+=1
    s[top]=item
    

def pop(s):
    global top
    if is_empty() :
        return "stack is empty"
    item=s[top]
    top-=1
    return item

def is_empty():
    global top
    return top == -1

def is_full(s):
    return top == len(s) 

exp="231*+9-"

n=len(exp)
i=0
stack=create_stack(exp)
while i!=n :
    if exp[i] == '+' :
        op1=pop(stack)
        op2=pop(stack)
        result=int(op2)+int(op1)
        push(stack,result)
    elif exp[i] == '-':
        op1=pop(stack)
        op2=pop(stack)
        result=int(op2)-int(op1)
        push(stack,result)
    
    elif exp[i] == '*':
        op1=pop(stack)
        op2=pop(stack)
        result=int(op1)*int(op2)
        push(stack,result)
    elif exp[i] == '/':
        op1=pop(stack)
        op2=pop(stack)
        result=int(op2)/int(op1)
        push(stack,result)
    else:
        push(stack,exp[i])

    i+=1

print(pop(stack))