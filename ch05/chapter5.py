#5.1 5.2
import sys
data=[]
for k in range(20):
    a=len(data)
    b=sys.getsizeof(data)
    #print('length:{0:3d};size in bytes:{1:4d}'.format(a,b))
    if not b-8*a-64:
      print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
    data.append(None)
#5.3
data=[None]*20
for k in range(20):
    a=len(data)
    b=sys.getsizeof(data)
    print('length:{0:3d};size in bytes:{1:4d}'.format(a,b))
    data.pop()
#5.4
def __getitem__(self, k):
        if k < 0:
            k = self._n + k
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]
#5.6
def insert(self, k, value):
    #temp为新数组，新旧数组除k处一一映射
    if self._n == self._capacity: #改变数组大小时
        temp = self._make_array(2 * self._capacity)
        self._capacity *= 2
        for i in range(k):
            temp[i] = self._A[i]
        temp[k] = value
        for i in range(k, self._n):
            temp[i + 1] = self._A[i]
        self._A = temp
    else:
        for i in range(self._n, k, -1):#不改变数组大小时，k后面的数组循环移动
            self._A[i] = self._A[i - 1]
        self._A[k] = value
    self._n += 1
#5.7
def findint(A,n):
    return sum(A)-sum(range(n+1))+n
#5.8
from time import time
N=10000
list = [j for j in range(N)]
start = time()
while list:
    list.pop(0)
end = time()
print((end - start) / N)

list = [j for j in range(N)]
start = time()
while list:
    list.pop(len(list)//2)
end = time()
print((end - start) / N)

list = [j for j in range(N)]
start = time()
while list:
    list.pop() #pop()=pop(-1)=pop(n-1)
end = time()
print((end - start) / N)
#5.11
def add_index(n):
    list1=[[0]*n for k in range(n)]
    k=1
    for i in range(n):
        for j in range(n):
            list1[i][j]=k 
            k+=1
    count=0
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            count=count+list1[i][j]
    return count
#5.13
data=[None,None,None,None]
for k in range(20):
    a=len(data)
    b=sys.getsizeof(data)
    #print('length:{0:3d};size in bytes:{1:4d}'.format(a,b))
    if not b-8*a-64:
      print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
    data.append(None)
#5.14
import random
list_a=[1,2,3]
N=10000
count=0;count_1=0;count_2=0;count_3=0;count_4=0;count_5=0;
for i in range(N):
    random.shuffle(list_a)
    if list_a==[1,2,3]:
        count+=1
    elif list_a==[1,3,2]:
        count_1+=1
    elif list_a==[2,1,3]:
        count_2+=1
    elif list_a==[2,3,1]:
        count_3+=1
    elif list_a==[3,1,2]:
        count_4+=1
    elif list_a==[3,2,1]:
        count_5+=1
    else:
        raise ValueError('invalid value')
print('[1,2,3]概率为{0:2f}%'.format(100*count/N))
print('[1,3,2]概率为{0:2f}%'.format(100*count_1/N))
print('[2,1,3]概率为{0:2f}%'.format(100*count_2/N))
print('[2,3,1]概率为{0:2f}%'.format(100*count_3/N))
print('[3,1,2]概率为{0:2f}%'.format(100*count_4/N))
print('[3,2,1]概率为{0:2f}%'.format(100*count_5/N))
#5.16
def pop(self, index=-1):
    if index < 0:
        index = self._n + index
    if not 0 <= index < self._n:
        raise IndexError('invalid index')
    ret = self._A[index]
    if self._n < self._capacity // 4:  # 如果当前小于最大容量/4
        temp = self._make_array(self._capacity // 2)
        self._capacity //= 2
        for i in range(index):  # index之前的元素
            temp[i] = self._n[i]
        if index != self._n - 1:  # index之后的元素
            for i in range(index + 1, self._n):
                temp[i - 1] = self._A[i]
        self._A = temp
    else:
        for i in range(index, self._n - 1):
            self._A[i] = self._A[i + 1]
    self._n -= 1
    return ret
#5.18
def text18():
    import time
    for i in range(8):
        li = []
        s1 = time.time()
        for j in range(10**(i + 1)):
            li.append(None)
            li.pop()
        s2 = time.time()
        n = float(10**(i + 1))
        return (s2 - s1) / n  # 返回生成器
#5.19
def pop_519(self, index=-1):
    if index < 0:
        index = self._n + index
    if not 0 <= index < self._n:
        raise IndexError('invalid index')
    ret = self._A[index]
    if self._n < self._capacity // 4:  # 如果当前小于最大容量/4
        temp = self._make_array(self.n)
        self._capacity = self.n
        for i in range(index):  # index之前的元素
            temp[i] = self._n[i]
        if index != self._n - 1:  # index之后的元素
            for i in range(index + 1, self._n):
                temp[i - 1] = self._A[i]
        self._A = temp
    else:
        for i in range(index, self._n - 1):
            self._A[i] = self._A[i + 1]
    self._n -= 1
    return ret
#5.21
import random
import string
def generate_random_str(randomlength=16):
        """
        生成一个指定长度的随机字符串，其中
        string.digits=0123456789
        string.ascii_letters=abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
        """
        str_list = [random.choice(string.digits + string.ascii_letters) for i in range(randomlength)]
        random_str = ''.join(str_list)
        return random_str
    
def con(n):
        import time
        A = generate_random_str(n)
        t1=time.time()
        letter=''
        for c in A:
            if c.isalpha():
                letter+=c
        t2=time.time()
        print(t2-t1)
        t1=time.time()
        letter=''
        temp=[]
        for c in A:
            if c.isalpha():
                temp.append(c)
        letter=''.join(temp)
        t2=time.time()
        print(t2-t1)
        t1 = time.time()  # 列表解析式
        letter=''
        letter=''.join([c for c in A if c.isalpha()])
        t2 = time.time()
        print(t2-t1)  # 生成器解释
        t1 = time.time()
        letter=''
        letter=''.join(c for c in A if c.isalpha())
        t2 = time.time()
        print(t2-t1)  # 返回生成器   
#5.22
def text22(n):
    import time
    l1 = []
    l2 = []
    A = generate_random_str(n)
    
    t1 = time.time()
    l1.extend(A)
    t2 = time.time()
    print('extend:{}'.format(t2 - t1), end='')
    
    t1 = time.time()
    for i in A:
        l2.append(i)
    t2 = time.time()
    print('append:{}'.format(t2 - t1), end='')
#5.23
def text23(n):
    import time
    l1 = []
    l2 = []
    
    t1 = time.time()
    l1=[n*n for n in range(1,n+1)]
    t2 = time.time()
    print('列表推导式:{}'.format(t2 - t1), end='')
    
    t1 = time.time()
    for i in range(1,n+1):
        l2.append(i*i)
    t2 = time.time()
    print('重复调用append:{}'.format(t2 - t1), end='')
#5.24
from time import time
N=1000
list = [j for j in range(N)]
start = time()
while list:
    list.remove(list[0])
end = time()
print((end - start) / N)

list = [j for j in range(N)]
start = time()
while list:
    list.remove(list[len(list)//2])
end = time()
print((end - start) / N)

list = [j for j in range(N)]
start = time()
while list:
    list.remove(list[-1]) 
end = time()
print((end - start) / N)
#5.25 先找出所有的，放入另一个list，再pop
def remove_all(data, value):
    f = 0
    r = 0
    while(r != len(data)):
        if data[r] == value:
            r += 1
        else:
            data[f] = data[r]
            f += 1
            r += 1
    for i in range(r - f):  # 删除多余的
        data.pop()
    return data
#5.26
def text26(data):
    data.sort()
    for i in range(0, len(data)):
        if data[i] == data[i + 1] == data[i + 2] == data[i + 3] == data[i + 4]:
            return data[i]
#5.27
def text27(data):
    from math import log
    k_max = int(log(len(data), 2)) + 1
    flag = [False] * k_max
    for i in data:
        flag[len(str(i)) - 1] = True
    for i in range(k_max):
        if flag[i] == False:
            yield i + 1
#5.29
def text29(l1, l2):
    dic1 = {}
    dic2 = {}
    if len(l1) > len(l2):
        l1, l2 = l2, l1
    for i in l1:
        dic1[i[0]] = set(i[1])

    for i in l2:
        dic2[i[0]] = set(i[1])
        if i[0] in dic1:
            dic2[i[0]] = dic2[i[0]].union(dic1[i[0]])
        dic2[i[0]].add(i[0])

    return [tuple(dic2[i]) for i in dic2]
# print(text29([('a','b'),('c','e')],[('a','c')]))
#5.31 有bug
def text31(lis):
    if type(lis) != list:
        return 0
    su = 0
    for i in lis:
        if type(i) == int:
            su += i
        else:
            su += text31(i)
            return su
#5.32
def text32(A,B):
    for i in range(len(A)):
        for j in range(len(A[i])):
            for k in range(len(A[i][j])):
               A[i][j][k]+=B[i][j][k]
    return A
#5.33
#点乘
def text331(A,B,sign):
    if sign == '+':
        for i in range(len(A)):
            for j in range(len(A[i])):
                A[i][j] += B[i][j]
        return A
    elif sign == '*':
        C=[[0]*len(B[0]) for r in range(len(A))]
        temp=0
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(A[0])):
                    temp += A[i][k]*B[k][j]
                    C[i][j] = temp
        return C
    else:
        raise TypeError('pleace imput + or *')
#离散相乘
def text332(data1, data2, sign):
    temp = list(data1)
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if sign == '+':
                temp[i][j] += data2[i][j]
            elif sign == '*':
                temp[i][j] *= data2[i][j]
            else:
                raise TypeError('pleace imput + or *')
    return temp

    
    
    
