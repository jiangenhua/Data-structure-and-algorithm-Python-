class Empty(Exception):
    pass
class ArrayStack():
  """LIFO Stack implementation using a Python list as underlying storage."""

  def __init__(self):
    """Create an empty stack."""
    self._data = []                       # nonpublic list instance

  def __len__(self):
    """Return the number of elements in the stack."""
    return len(self._data)

  def is_empty(self):
    """Return True if the stack is empty."""
    return len(self._data) == 0

  def push(self, e):
    """Add element e to the top of the stack."""
    self._data.append(e)                  # new item stored at end of list

  def top(self):
    """Return (but do not remove) the element at the top of the stack.

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise Empty('Stack is empty')
    return self._data[-1]                 # the last item in the list

  def pop(self):
    """Remove and return the element from the top of the stack (i.e., LIFO).

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise Empty('Stack is empty')
    return self._data.pop()               # remove last item from list

#6.20
def text20(S):
   temp=ArrayStack()                   #临时栈
   res=ArrayStack()                    #存储结果的栈
   res.push(list(S.pop()))             
   while len(S)!=0:                    #将S栈中的元素全部提取
      sign=S.pop()                     #保存元素到sign中
      while len(res)!=0:
         word=res.pop()                #添加元素到栈中
         for i in range(len(word)+1):
            t=list(word)
            t.insert(i,sign)
            temp.push(t)
      temp,res=res,temp
   return res
#6.21
def text21(S:ArrayStack())->list:
   temp=ArrayStack()                 #临时栈
   res=ArrayStack()                 #存贮答案的栈    
   while len(S)!=0:
      sign=S.pop()
      print('sign:',sign)
      while len(res)!=0:
         print('res.top()',res.top())
         word=res.pop()
         print('word',word)
         temp.push(word)
         print('temp.top()',temp.top())
         t=list(word) 
         print('t',t)           #创建新的列表对象，防止反复使用原列表
         t.insert(0,sign)
         print('t',t)
         temp.push(t)
         print('temp.top1()',temp.top())
      temp.push(list(sign))
      print('temp.top2()',temp.top())
      temp,res=res,temp
      print('res.top()',res.top())
   return res
'''
a=ArrayStack()
for i in range(1,4):
   a.push(str(i))
b=text21(a)
t=[0]*len(b)
for i in range(len(b)):
    t[i] = b.pop()
print(t)
'''
#6.22
def text22(s):
   sign=ArrayStack()                      #sign stack
   num=ArrayStack()                       #num stack
   for i in s:
      if i in '+-*/':                     # push sign and num into the match stack
         sign.push(i)
      elif i==')':                        #while discover a ) output two num from the num stack and one sign from sign stack
         temp=num.pop()
         word=num.pop()+temp+sign.pop()
         num.push(word)
      elif i !='(':
         num.push(i)
   temp=num.pop()
   return num.pop()+temp+sign.pop()
'''
print(text22('((5+2)*(4-3))/6'))
'''
#6.23
def text23(R:ArrayStack(),S:ArrayStack(),T:ArrayStack()):
   times=len(S)
   #将S中的元素拼接到T中
   for i in range(times):
      R.push(S.pop())
   for i in range(times):
      T.push(R.pop())
   times=len(T)
   #将T中拼接好的元素存入S中
   for i in range(times):
      R.push(T.pop())
   for i in range(times):
      S.push(R.pop())
def text232(R:ArrayStack(),S:ArrayStack(),T:ArrayStack()):
    len_T=len(T)
    while len(T)!=0:
        temp=T.pop()
        R.push(temp)
    while len(S)!=0:
        temp=S.pop()
        T.push(temp)
    for i in range(len_T):
        temp=R.pop()
        S.push(temp)
    while len(T)!=0:
        temp=T.pop()
        S.push(temp)
        
#6.27 伪代码
'''
解决方案是实际使用队列Q分两个阶段处理元素。 
在第一个阶段，我们迭代地从S中弹出每个元素并将其放入Q中，
然后迭代地从Q中使每个元素出列并将其推入S。这将反转S中的元素。
然后我们重复相同的过程，但是 时候我们还要寻找元素x。 
通过使元素通过Q并第二次返回S，我们反转了反转，从而将元素按其原始顺序放回S中。
'''    
#6.28 same as #6.16
from array_queue import ArrayQueue
class ArrayQueue1(ArrayQueue):
   def __init__(self,maxlen=None):
      super().__init__()
      self.maxlen=maxlen
      if maxlen!=None:
         self._data=[None]*maxlen
         
   def enqueue(self, e):
      """Add an element to the back of queue."""
      #源代码的基础上增加下两行
      if self.maxlen!=None and self.maxlen==self._size:
         raise Exception('it is the max')
      if self._size == len(self._data):
         self._resize(2 * len(self.data))     # double the array size
      avail = (self._front + self._size) % len(self._data)
      self._data[avail] = e
      self._size += 1
#6.29
def text29(self):
    if not self.is_empty():
        temp = self._data[self._front]
        self._data[self._front] = None
        self._front = self._front+1%len(self._data)
        self._data[(self._front+self._size)%len(self._data)]=temp
#6.30
        
        
        
        
        
        
        


