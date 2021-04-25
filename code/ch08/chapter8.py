import sys
sys.path.append('C:/Users/18613/Desktop/数据结构与算法/源文件/ch08')
from linked_binary_tree import LinkedBinaryTree
#8.5
'''思路：先全取后挑选'''
def text5(tree):
    l = [i for i in tree.positions() if tree.is_leaf(i)]     #get left child all of tree
#    for i in l:                                    
#        print('###',tree.left(tree.parent(i)).element(),i.element())
    l = [i for i in l if (tree.left(tree.parent(i)) == i)]   #positions是临时包装的类，不能使用 A is B
    return len(l)

#8.10
from binary_tree import BinaryTree 
class BinaryTree1(BinaryTree):
    def num_children(self):
        count = 0
        if self.left != None:
            count += 1
        if self.right != None:
            count += 1
        return count
    def num_children1(self,p): #计算子孙节点数
        if self.is_leaf(p):
            return 0
        else:
            return 1+num_children1(self.children(p))
#8.15
'''将非公共方法公共化'''
from collections import deque
class MutableLinkedBinaryTree(LinkedBinaryTree):
    '''this is a normal class'''
    def delete(self,p):
        return self._delete(p)
    def add_root(self,p):
        return self._add_root(p)
    def add_left(self,p,e):
        return self._add_left(p,e)
    def add_right(self,p,e):
        return self._add_right(p,e)
    def replace(self,p,e):
        return self._replace(p,e)
    def attach(self,p,t1,t2):
        self._attach(p,t1,t2)
        
t=MutableLinkedBinaryTree()           
t.add_root(1)        
a=t.add_left(t.root(),2)
b=t.add_right(t.root(),3)
for i in t.positions():
   print(i.element())
print(text5(t))
for i in t.breadthfirst():
   print(i.element())
#8.