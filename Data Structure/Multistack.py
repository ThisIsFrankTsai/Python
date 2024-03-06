class Multistack:

    def __init__(self,k=1):
        self.number_of_stacks=k
        self.values=[None]*(self.number_of_stacks*2) #default set size is 2
        self.sizes=[2+i*2 for i in range(self.number_of_stacks)] #動態調整stack大小
        self.top_index=[size-2 for size in self.sizes] #與一般stack 不同，top的index 從0開始，一般是從-1 開始
    
    def push(self, stack_num, val):
 
        # Pushes a value onto the given stack_num.
        # If the stack is full, expands the stack.
        if self.is_full(stack_num):
            self.expand(stack_num)

        self.values[self.top_index[stack_num]] = val
        self.top_index[stack_num] += 1 #當放入stack的時候，top+1 但是 該位置沒有任何東西
    
    def pop(self,stack_num):
        if self.is_empty(stack_num):
            print(f'{stack_num} is empty')
        
        item=self.values[self.top_index[stack_num]]
        self.values[self.top_index[stack_num]]=None
        self.top_index[stack_num]=self.top_index[stack_num]-1 
        self.shrink(stack_num)

        return item

    def top(self,stack_num):
        if self.is_empty(stack_num):
            print(f'{stack_num} is empty')
        
        return self.values[self.top_index[stack_num]-1] #由於， top index 位置是從0開始，所以要先-1 才會找到item
    
    def size(self,stack_num): #計算目前stack_num 內的item 數量
        if not stack_num :    #如果 是 stack_num 0的話
            return self.top_index[0]
        
        return self.top_index[stack_num]-self.sizes[stack_num-1]
    
    def is_empty(self,stack_num):
        if not stack_num:
            offset=0
        else:
            offset=self.sizes[stack_num-1]
         
        index=self.top_index[stack_num]

        return index == offset #目前的數量跟index相比
    
    def is_full(self,stack_num):
        offset=self.sizes[stack_num] #預定的大小
        index=self.top_index[stack_num] #index 的位置

        return index>=offset
    
    def expand(self,stack_num):
        reserved_size=self.size(stack_num) #原來的size

        for i in range(stack_num+1,self.number_of_stacks): #目前的stack 往後面的stack 全部都要位移reserved_size
            self.sizes[i]+=reserved_size
            self.top_index[i]+=reserved_size

        self.sizes[stack_num]+=reserved_size #stack_num 加大 原來的size

        self.values=(self.values[:self.top_index[stack_num]]+ #stack_num 以前的values不變
                     [None]*reserved_size+                    #新增的reserved sizes 先填入None
                     self.values[self.top_index[stack_num]:]) #stack_num 後面的values 不變直接放入



MStack = Multistack(3)#stack 編號0,1,2
print("stack內容:",MStack.values)
print("stack size:",MStack.sizes)
print("stack top index:",MStack.top_index)

MStack.push(0, 21)
MStack.size(1)
print("MStack.push(0, 21)")
print("stack內容:",MStack.values)
print("stack size:",MStack.sizes)
print("stack top index:",MStack.top_index)
print("MStack.size(0):",MStack.size(0))
print("MStack.size(1):",MStack.size(1))
print("MStack.size(2):",MStack.size(2))
MStack.push(2, 13)
print("MStack.push(2, 13)")
print("stack內容:",MStack.values)
print("stack size:",MStack.sizes)
print("stack top index:",MStack.top_index)
print("MStack.size(0):",MStack.size(0))
print("MStack.size(1):",MStack.size(1))
print("MStack.size(2):",MStack.size(2))
MStack.expand(0)
print("MStack.expand(0):")
print("stack內容:",MStack.values)
print("stack size:",MStack.sizes)
print("stack top index:",MStack.top_index)
print("MStack.size(0):",MStack.size(0))
print("MStack.size(1):",MStack.size(1))
print("MStack.size(2):",MStack.size(2))


MStack.push(1, 14)
print("MStack.push(1, 14)")
print("stack內容:",MStack.values)
print("stack size:",MStack.sizes)
print("stack top index:",MStack.top_index)
MStack.push(1, 24)
print("MStack.push(1, 24)")
print("stack內容:",MStack.values)
print("stack size:",MStack.sizes)
print("stack top index:",MStack.top_index)
MStack.push(2, 5)
print("MStack.push(2, 5)")
print("stack內容:",MStack.values)
print("stack size:",MStack.sizes)
print("stack top index:",MStack.top_index)
MStack.push(0, 9)
print("MStack.push(2, 9)")
print("stack內容:",MStack.values)
print("stack size:",MStack.sizes)
print("stack top index:",MStack.top_index)
MStack.push(0, 17)
print("MStack.push(0, 17)")
print("stack內容:",MStack.values)
print("stack size:",MStack.sizes)
print("stack top index:",MStack.top_index)
MStack.top(0)
print("MStack.top(0):",MStack.top(0))
MStack.top(1)
print("MStack.top(1):",MStack.top(0))

print("stack內容:",MStack.values)
print("stack size:",MStack.sizes)
print("stack top index:",MStack.top_index)