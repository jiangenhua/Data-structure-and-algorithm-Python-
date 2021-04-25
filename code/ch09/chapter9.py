import sys
sys.path.append('C:/Users/18613/Desktop/数据结构与算法/源文件/ch08')

#9.1
'''思路：先全取后挑选'''
def text5(tree):
    l = [i for i in tree.positions() if tree.is_leaf(i)]     #get left child all of tree
#    for i in l:                                    
#        print('###',tree.left(tree.parent(i)).element(),i.element())
    l = [i for i in l if (tree.left(tree.parent(i)) == i)]   #positions是临时包装的类，不能使用 A is B
    return len(l)

#8.10