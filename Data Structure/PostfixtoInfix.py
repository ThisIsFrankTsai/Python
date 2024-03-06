
def isOperand(x):
    if (x=='+' or
       x=='-' or
       x=='*' or
       x=='/' or
       x=='^' or
       x==')' or
       x=='(' ) :
       return False #不是數字
    return True  #是數字


def prec(c):
    if c == '^':
        return 3
    elif c == '/' or c == '*':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1
 
def associativity(c):
    if c == '^':
        return 'R'
    return 'L'  # Default to left-associative

def PostfixtoInfix(exp):
    stack=[]

    for i in exp:
        if isOperand(i): #是數字 就丟入堆疊
            stack.insert(0,i) 
        else:             #不是數字，就從堆疊裡面取出兩個元素做運算
            op1=stack[0]
            stack.pop(0)
            op2=stack[0]
            stack.pop(0)
            stack.insert(0,"("+op2+i+op1+")") #運算完後放回堆疊

    return stack[0]

def InfixtoPostfix(exp):
    result = []
    stack = []
    for i in exp:
        
        if isOperand(i) :
            result.append(i)
        elif i=='(':
            stack.append(i)
        elif i==')':
            while stack and stack[-1]!='(':
                result.append(stack.pop())
            stack.pop()
        else:
            while stack and (prec(i) < prec(stack[-1]) or(prec(i)==prec(stack[-1]) and associativity(i)=='L')): #比較堆疊內最後一個元素與目前讀到的元素的優先權
                result.append(stack.pop())
            stack.append(i)

    while stack:
        result.append(stack.pop())

    return ''.join(result)


if __name__ == '__main__': 
 
    exp = "ab/c+ef*/gh^i-+k+"
    print(PostfixtoInfix(exp.strip()))
    exp = "a+b*(c^d-e)^(f+g*h)-i"
    print(InfixtoPostfix(exp))