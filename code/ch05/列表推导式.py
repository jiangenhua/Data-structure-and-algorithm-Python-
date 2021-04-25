# # 列表推导式
#1
'''
list = [[x*x] for x in range(10)]
print(list)
#########################如果正常写是这样的##########
list = []
for x in range(10):
    list.append([x*x])
print(list)

#2
list1=[[1,2,3],[4,5,6],[7,8,9]]
list2=[num for elem in list1 for num in elem]
print(list2)
###等价于####
list1=[[1,2,3],[4,5,6],[7,8,9]]
list2=[]
for elem in list1:
    for num in elem:
        list2.append(num)
print(list2)
'''
#3实现矩阵转置
matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
matrixlater=[[row[i] for row in matrix] for i in range(4)]
print(matrixlater)
#等价于
matrix=list(map(list,zip(*matrix)))
print(matrix)
'''
#4 列表表达式 if—else
#有两种形式
# 1：[x for x in data if condition]
#此处的if主要起判断的作用，data数据只有满足if条件的才会留下，最后统一生成一个数据列表
#2：[exp1 if condition else exp2 for x in data]
#此处的if -slse 主要起赋值的作用，如果x满足条件只想exp1不满足执行else
list  = [x for x in range (1,101) if x%3==0]
print(list)
p = [x if x %3==0 else -x for x in range(101)]
print(p)
'''