def allSubsets(s):
    if len(s) == 0 :
        return [[]]
    return allSubsets(s[1:]) + [[s[0]] + r for r in allSubsets(s[1:])]

'''
一个例子 Y = [ [ int(x1+x2 < 1) ] for (x1, x2) in X ]
对X中的每一组元素(x1, x2)遍历一遍，当满足(x1+x2 < 1)时，
就把这个布尔值[True]/[False]转换成int型(1或0)，存放在[ ]里，作为Y的一个元素。
'''

def reverse_str(word, index=0):
    if index == len(word) - 1:
        return [word[index]]
    else:
        ans = reverse_str(word, index+1)
        ans.append(word[index])
        if index == 0:
            ans = ''.join(ans)
        return ans
#reverse_str('snap%^&*jsa')

def huiwen(s):
    s1 =s[::-1]
    if s == s1:
        print( '%s是回文字符串' %s)
    else:
        print('%s不是回文字符串' %s)
def confirm_hui_str(word):
    if len(word) == 1:
        return True
    else:
        if word[0] != word[len(word)-1]:
            return False
        return confirm_hui_str(word[1:-1])
    
def confirm_num(s):
    count = 0
    s.lower()
    s1 = ['a','e','i','o','u']
    s = list(s)
    for i in s1:
        if i in s:
            x = s.count(i)
            #print(x)
        count = count + x
        #print(count)
        
    if count > len(s)-count:
        return True
    else:
        return False
def confirm_vowel(word):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    if len(word) == 1:
        if word[0] in vowel_list:
            return 1
        else:
            return -1
    elif word[0] in vowel_list:
        return 1 + confirm_vowel(word[1:])
    else:
        return -1 + confirm_vowel(word[1:])
    
def realign_num(data):
    if len(data) == 1:
        return data
    elif data[0] % 2 == 1:
        data.append(data.pop(0))
        return data[:1] + realign_num(data[1:])
    elif data[0] % 2 == 0:
        return data[:1] + realign_num(data[1:])
    
def _organize_recurse(data, low, high):
    if low < high:
        if data[high] & 1 == 0: # data[high] is even
            data[low],data[high] = data[high],data[low]
            return _organize_recurse(data, low+1, high) # data[low] is known to be even
        else:
            return _organize_recurse(data, low, high-1) # data[high] is known to be odd
def organize(data):
    _organize_recurse(data, 0, len(data) -1)
def sort_by_k(S, k, index=0):
    if index == len(S) - 1:
        return [S[index]]
    else:
        if S[index] <= k:
            return [S[index]] + sort_by_k(S, k, index+1)
        else:
            return sort_by_k(S, k, index+1) + [S[index]]
        
####如何查找出相同值并删除？用集合set？    
def find_sum(S, k, index1=0, index2=1):
    if S[index1] + S[index2] == k:
        return S[index1], S[index2]
    elif index2 == len(S) - 1:
        index1 += 1
        index2 = index1 + 1
        return find_sum(S, k, index1, index2)
    else:
        return find_sum(S, k, index1, index2+1)
'''
 def findsum(s, k, index1=0, index2=1):
    x=[]
    count=[]
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i]+s[j]==k:
                print('1th number is',s[i])
                print('2nd number is',s[j])
                print([s[i], s[j]])
                x=[{'%sth'%i:s[i],'%sth'%j:s[j]}]
                count=count+x
    print(count)
s=[1,2,3,4,4,5,6,4]
k=8
findsum(s,k)
'''
'''
def FindPair(A,i,j,k):
    if i == j:
        return False
    else:
        if A[i]+A[j] < k:
            return FindPair(A, i+1, j,k)
        elif A[i]+A[j] > k:
            return FindPair(A, i,j-1,k)
        else:
            return True
A=[1,2,3,4,5,6]
k=7
i=0
j=4
FindPair(A,i,j,k)
'''

def power(x, n):
    k = 0
    while (1 << k) <= n:
        k += 1
        
    answer = 1.0
    for j in range(k-1,-1,1):
        answer *= answer
        if (1 << j) & n > 0:
            answer *= x
            return answer

import os
def find(path, filename):
    abspath = os.path.join(path, filename)
    if os.path.isdir(abspath):              #os.path.isdir()用于判断对象是否为一个目录
        for sub_filename in os.listdir(abspath):
            if os.path.isdir(os.path.join(abspath, sub_filename)):
                find(abspath, sub_filename)
            else:
                print(os.path.join(abspath, sub_filename))  
                
def walk(path):
    dirpath=path
    dir_path_list=[]
    film_path_list=[]
    if os.path.isdir(path):
        for i in os.listdir(path):
            if os.path.isdir(os.path.join(path,i)):
                dir_path_list.append(i)
            else:
                film_path_list.append(i)
    return dirpath,dir_path_list,film_path_list
                
                
                
                
                
                
    