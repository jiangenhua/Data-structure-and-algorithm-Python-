# 数据结构与算法（Python语言实现）

## ==**排序算法比较**==

==**任何基于比较的排序算法对有n个元素的序列排序所花费的时间都是Ω(nlogn)的运行时间下界（Ω=不低于）**==

![image-20210313170134244](数据结构与算法（Python语言实现）.assets/image-20210313170134244.png)

排序方式：*In-place：占用常数内存，不占用额外内存     Out-place：占用额外内存
稳定性：一个稳定的排序算法是指，对于S中任意两个条目($k_i$,$v_i$)和($k_j$,$v_j$)，$k_i=k_j$，并且排序前($k_i$,$v_i$)在($k_j$,$v_j$)前面，排序后($k_i$,$v_i$)也在($k_j$,$v_j$)前面。

**冒泡排序：**==它重复地走访过要排序的元素列，依次比较两个相邻的元素，==如果顺序（如从大到小、首字母从Z到A）错误就把他们交换过来。走访元素的工作是重复地进行直到没有相邻元素需要交换，也就是说该元素列已经排序完成。

**插入排序：**插入排序算法是==基于某序列已经有序排列的情况下，通过一次插入一个元素的方式按照原有排序方式增加元素。==这种比较是从该有序序列的最末端开始执行，即要插入序列中的元素最先和有序序列中最大的元素比较，若其大于该最大元素，则可直接插入最大元素的后面即可，否则再向前一位比较查找直至找到应该插入的位置为止。插入排序的基本思想是，每次将1个待排序的记录按其关键字大小插入到前面已经排好序的子序列中，寻找最适当的位置，直至全部记录插入完毕。

![image-20210327173536398](数据结构与算法（Python语言实现）.assets/image-20210327173536398.png)

**选择排序：**选择排序算法的基本思路是==为每一个位置选择当前最小的元素。==选择排序的基本思想是，基于直接选择排序和堆排序这两种基本的简单排序方法。==首先从第1个位置开始对全部元素进行选择，选出全部元素中最小的给该位置，再对第2个位置进行选择，在剩余元素中选择最小的给该位置即可；==以此类推，重复进行“最小元素”的选择，直至完成第(n-1)个位置的元素选择，则第n个位置就只剩唯一的最大元素，此时不需再进行选择。使用这种排序时，要注意其中一个不同于冒泡法的细节。举例说明：序列58539．我们知道第一遍选择第1个元素“5”会和元素“3”交换，那么原序列中的两个相同元素“5”之间的前后相对顺序就发生了改变。因此，我们说选择排序不是稳定的排序算法，它在计算过程中会破坏稳定性。

![image-20210327173639890](数据结构与算法（Python语言实现）.assets/image-20210327173639890.png)

**快速排序：**快速排序的基本思想是==通过一趟排序算法把所需要排序的序列的元素按设定值分割成两大块再递归该过程==，其中，一部分的元素都要小于或等于另外一部分的序列元素，然后仍根据该种方法对划分后的这两块序列的元素分别再次实行快速排序算法，排序实现的整个过程可以是递归的来进行调用，最终能够实现将所需排序的无序序列元素变为一个有序的序列。

![image-20210327173710945](数据结构与算法（Python语言实现）.assets/image-20210327173710945.png)

**归并排序：**归并排序算法就是==把序列递归划分成为一个个短序列，以其中只有1个元素的直接序列或者只有2个元素的序列作为短序列的递归出口，再将全部有序的短序列按照一定的规则进行排序为长序列。==归并排序融合了分治策略，即将含有n个记录的初始序列中的每个记录均视为长度为1的子序列，再将这n个子序列两两合并得到n/2个长度为2(当凡为奇数时会出现长度为l的情况)的有序子序列；将上述步骤重复操作，直至得到1个长度为n的有序长序列。需要注意的是，在进行元素比较和交换时，若两个元素大小相等则不必刻意交换位置，因此该算法不会破坏序列的稳定性，即归并排序也是稳定的排序算法。所谓归并排序是指<u>将两个或两个以上有序的数列（或有序表），合并成一个仍然有序的数列（或有序表）</u>。

![img](https://pic4.zhimg.com/80/v2-2958d4f3d9dd9156f1b5dca6788fe8a7_720w.jpg)

**堆排序：**堆排序的基本思想是：==将待排序序列构造成一个大顶堆，此时，整个序列的最大值就是堆顶的根节点。将其与末尾元素进行交换，此时末尾就为最大值。然后将剩余n-1个元素重新构造成一个堆，这样会得到n个元素的次小值。==如此反复执行，便能得到一个有序序列了。

![image-20210313171831910](数据结构与算法（Python语言实现）.assets/image-20210313171831910.png)

堆排序的基本步骤：
a.将无需序列构建成一个堆，根据升序降序需求选择大顶堆或小顶堆（**一般升序采用大顶堆，降序采用小顶堆**）;
b.将堆顶元素与末尾元素交换，将最大元素"沉"到数组末端;
c.重新调整结构，使其满足堆定义，然后继续交换堆顶元素与当前末尾元素，反复执行调整+交换步骤，直到整个序列有序。

**希尔排序：**希尔排序是==把记录按下标的一定增量分组，对每组使用直接插入排序算法排序==；随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。![img](数据结构与算法（Python语言实现）.assets/6095354-ff984d80dbc0455f.png)

**计数排序：**计数排序==使用一个额外的数组C，其中第i个元素（下标i）是待排序数组A中值等于i的元素的个数。==适用于一定范围的整数排序**。**在取值范围不是很大的情况下，它的性能在某些情况甚至快过那些O(nlogn)的排序，例如快速排序、归并排序。![image-20210313172136698](数据结构与算法（Python语言实现）.assets/image-20210313172136698.png)

**桶排序：**工作的原理是==将数组分到有限数量的桶里。每个桶再个别排序（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排序），最后依次把各个桶中的记录列出来记得到有序序列。==![img](https://pic2.zhimg.com/80/v2-ff4cdccdb1ff6b90ecdb3fc4d361f725_720w.jpg)

**基数排序：**原理是==将整数按位数切割成不同的数字，然后按每个位数分别比较。==基数排序的方式可以采用LSD（Least significant digital）或MSD（Most significant digital），LSD的排序方式由键值的最右边开始，而MSD则相反，由键值的最左边开始。![img](https://pic4.zhimg.com/80/v2-5ae4857fa248035ecec780583c5e3303_720w.jpg)

基数排序 VS 计数排序 VS 桶排序

![image-20201117235751811](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20201117235751811.png)

**混合方法排序：**利用分治算法使子序列的大小降到某个阈值（例如50个元素）以下；当处于该值以下，可以使用插入排序等适用于小规模序列的排序方法。

==排序算法优缺点==

|                     | 优点                                                   | 缺点                           |
| ------------------- | ------------------------------------------------------ | ------------------------------ |
| **插入排序**        | 进行小序列排序的优秀算法；对几乎已经排序好的序列很有效 | 时间复杂度O($n^2$)不适用大序列 |
| **堆排序**          | 小、中型序列优秀算法                                   | 存在元素交换，是非稳定排序     |
| **快速排序**        | 通用的内存排序算法                                     | 存在元素交换，是非稳定排序     |
| **归并排序**        | Python的list类的标准sort方法的本质                     | out-place占用额外内存          |
| **桶排序&基数排序** | 适用于程序较小的整型键、字符串、离散d元组键            |                                |

## 第1章 Python入门 

1.2  Python对象
**<u>类</u>**是所有数据类型的基础。
1.2.1  标识符、对象和赋值语句
每个标识符（变量名）与其所引用的对象的**<u>内存地址</u>**隐式相关联。
1.2.2	创建和使用对象
**调用方法**
一些方法返回一个对象的状态信息，但并不改变该状态。这些方法被称为**<u>访问器</u>**。其他方法会改变一个对象的状态，这些方法被称为**<u>应用程序</u>**或**<u>更新方法</u>**。
**元组类**
为了表示只有一个元素的元组，该元素之后必须有一个逗号，例(17,)是一元元组。
**set类**（可以用于去除重复的元素）
set类代表许多元素的集合，集合中没有重复的元素，而且这些元素没有内在的联系。python使用{}作为集合的分隔符。
集合有一个高度优化的方法来检查特定元素是否包含在集合内，基于一个名为<u>散列表</u>的数据结构。
有两个由算法基础产生的重要限制：①集合不保存任何有特定顺序的元素集。②只有不可变类型实例（int,float,str,tuple,frozenset）才能被添加到一个集合。
所有<u>**序列**</u>（列表等）规定的比较操作都是基于字典顺序，即一个元素一个元素比较，直至找到第一个不同的元素；<u>**集合**</u>并不保证他们内部元素以特定的顺序排列，所以比较运算符（<）不是以字典顺序进行比较的。
**扩展赋值运算符**

```
a=[1,2,3]
b=a
b+=[4,5]
print(a)
print(b)
b=b+[6,7]
print(a)
print(b)
>>>
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5, 6, 7]
```

语句 a+=b 与 a=a+b 在列表语义方面的微妙差异。                  
1.5.2	Python的内置函数

| 表1-4 常见的内置函数        |                    |
| :--- | :--- |
| 调用语法 |  含义   |
| chr(int) | 返回给定值的Unicode编码的字符 |
| ord(char) | 返回给定字符的Unicode编码值 |
| hash(obj) | 对于对象obj返回一个整数的散列值 |
| map(f,iter1,iter2,…) | 返回迭代器产生的函数调用f(e1,e2,…)的结果，其中元素e1,e2∈iter1,iter2 |
| iter(iterable) | 创建一个迭代器 |
| yield | 调用一个生成器，生成器是一个返回迭代器的函数，遇到 yield 时函数会暂停并保存当前所有的运行信息 |
| next(iter) | 输出迭代器下一个元素 |

1.6.2	文件

| 表1-5   文件对象fb与文件交互的常用方法 |                    |
| :--- | :--- |
| ![image-20200922205217973](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20200922205217973.png) |     |

1.7	异常处理

| 表1-6   Python中的常见异常类                                 |      |
| :----------------------------------------------------------- | :--- |
| ![image-20200922205909658](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20200922205909658.png) |      |

1.7.1	抛出异常

```python
raise ValueError('x cannot be negative')
```

1.7.2	捕捉异常

```
try:
	主程序块
except(ValueError,EOFError):
	print('Invalid response') #or pass

当一个错误发生在try块中时，try中剩下的语句会直接跳过。然后进入except块，执行其中语句（若希望不执行语句，可使用pass）。然后继续while循环。
```

1.8	迭代器和生成器（https://www.runoob.com/python3/python3-iterator-generator.html）
**迭代器**
迭代器是一个对象，通过一系列的值来管理迭代。
对象obj是可迭代的，通过语法iter(obj)可产生一个迭代器。
（通过语法i = iter(data)则可以产生一个迭代器对象，然后调用next(i)将返回列表中的元素）

**生成器**
在 Python 中，使用了 yield 的函数被称为生成器（generator）。
跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
在调用生成器运行的过程中，每次遇到 yield 时函数会暂停（程序暂时中断）并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
调用一个生成器函数，返回的是一个迭代器对象。

```python
import sys
 def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
 
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()
>>>
0 1 1 2 3 5 8 13 21 34 55
```

1.9.2	解析语法

| 解析语法                      |            |
| :---------------------------- | :--------- |
| [k*k for k in range(1,n+1)]   | 列表解析   |
| {k*k for k in range(1,n+1)}   | 集合解析   |
| (k*k for k in range(1,n+1)    | 生成器解析 |
| {k:k*k for k in range(1,n+1)} | 字典解析   |

当结果不需要存储在内存中时（无分配地址，不赋予变量名），生成器语法特别优势。

1.9.3	序列类型的打包、解包、同时分配

	>data=2,4,6,8
	>
	>return x,y

如果在大的上下文给出了一系列逗号分隔的表达式，它们将被视为一个单独的元组，使标识符data赋值成元组（2,4,6,8），这种行为被称为元组的自动<u>打包</u>。

> a,b,c,d = range(7,11)

允许单个标识符的一系列元素赋值给序列中的各个元素，称为自动<u>解包</u>。

> x,y,z = 6,2,5

实际上，赋值右边将自动打包成一个元组，然后自动解包，分配给左边三个标识符。此时右边打包值未命名元组相当于隐式的临时变量。
自动打包和解包结合起来就是<u>同时分配</u>技术。

1.10	命名空间
**python实现命名空间是用自己的字典将每个标识符字符串（例如'a'）映射到其相关值。**python还提供了几种方法来检查一个给定的命名空间。函数dir()报告给定命名空间中的标识符的名称（即字典的键），而函数var()返回完整的字典。

第一类对象
一些可以分配给一个标识符作为参数传递或由函数返回的类型的实例。

## 第2章 面向对象编程

面向对象模式中的主体被称为<u>**对象**</u>(object)。每个对象都是**<u>类</u>**(class)的实例。
面向对象设计目标：健壮性、适应性、可重用性
面向对象设计原则：模块化、抽象化、封装
面向对象设计关键：定义类和其实例变量及方法

调试的方法：①打印语句（print）②调试器（debugger）：在代码中插入断点（breakpoint），当程序中止时，可以检查变量当前的值。

2.3.2	运算符重载
见书p48

2.4	继承
在面向对象编程中，模块化和层次化组织的机制是一种称为<u>**继承**</u>的技术。
子类可以通过提供一个新的覆盖现有方法的实现方法特化一个现有的行为（重写一个已命名的函数）；也可以创建新的函数扩展父类。

```
super().__init__(para1,..,paran) 调用从父类继承的init()
```

2.4.1	保护成员
一个下划线开头的名字都被看作受保护的（_age），而以双下划线开头的名字（除了特殊的方法）是被看作私有的(__age)。
==被声明为受保护的成员可以访问子类，但是不能访问普通的公有类；被声明为私有的成员既不能访问子类，也不能访问公有类。==
在选择使用受保护的数据时，我们已经创建了一个依赖，在该依赖中，如果作者改变了内部设计，则子类可能也会改变。所以我们可以添加一个非公有的方法

```
（_set_balance）
```

子类就可以通过该方法来改变余额而不直接访问数据成员_balance（实例变量）

### ==2.4.3	抽象基类==

==如一个类的唯一目的是作为继承的基类，那么这个类就是一个抽象基类。==更正式的说，一个抽象类不能直接实例化，而具体的类（基类的子类）可以被实例化。

抽象基类依赖于一个面向对象的软件设计模式——模板方法模式，是一个抽象基类在提供依赖于调用其他抽象行为时的具体行为。在这种方式中，只要一个子类提供定义了缺失的抽象行为，继承的具体行为也就被定义了。

```python
from abc import ABCMeta, abstractmethod   # need these definitions

class Sequence(metaclass=ABCMeta):
  """Our own version of collections.Sequence abstract base class."""

  @abstractmethod
  def __len__(self):
    """Return the length of the sequence."""

  @abstractmethod
  def __getitem__(self, j):
    """Return the element at index j of the sequence."""

  def __contains__(self, val):
    """Return True if val found in the sequence; False otherwise."""
    for j in range(len(self)):
      if self[j] == val:                # found match
        return True
    return False

  def index(self, val):
    """Return leftmost index at which val is found (or raise ValueError)."""
    for j in range(len(self)):
      if self[j] == val:                # leftmost match
        return j
    raise ValueError('value not in sequence') # never found a match

  def count(self, val):
    """Return the number of elements equal to given value."""
    k = 0
    for j in range(len(self)):
      if self[j] == val:                  # found a match
        k += 1
    return k
```

这个实现依赖于Python的两个高级技术。==第一个技术是声明abc模块中的ABCMeta类声明Sequence类的元类。==元类不同于超类，它为类定义本身提供了一个模板。具体来说，ABCMeat声明确保类的构造函数引发异常。==第二个技术是在_ _len_ _ _和_ _ _getitm_ _方法声明前立即使用@abstractmethod装饰器，这就声明了这两种特定的方法是抽象的。==
强调：如果子类对从基类继承的行为提供自己的实现，那么新的定义会覆盖之前继承的。

2.5	命名空间
命名空间是一个抽象名词，它管理着特定范围内定义的所有标识符，将每个名称映射到相应的值。
**实例命名空间：**就是管理单个对象的特定属性。self作为限定符使用，这使得_balance标识符直接被添加到实例命名空间中。
**类命名空间：**用于管理一个类的<u>所有实例所共享的成员</u>或<u>没有引用任何特定实例的成员</u>，一个类命名空间包含所有直接在类定义体内的声明（函数、方法）

下面是三种命名空间的概念视图：

![image-20200924183944448](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20200924183944448.png)

​                                                    Credit Card类命名空间

![image-20200924184039227](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20200924184039227.png)

​                                          Predatory Credit Card类命名空间

![image-20200924184135975](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20200924184135975.png)

​                                    Predatory Credit Card对象的实例命名空间

**嵌套类**

```python
Class A：
	Class B：
```

B是嵌套类，标识符B是进入了A类的命名空间相关联的一个新定义的类。B不继承A类。

**_ _slots_ _ 声明**
Python提供了一种更直接的机制来表示实例命名空间：使用流来表示一个类的所有实例。类定义必须提供一个名为_ _slots_ _的的类级别成员。

```python
class CreditCard:
	_ _slots_ _ = '_customer','_bank',....
```

如果使用继承时，基类声明了_ _slots_ _，子类也必须声明，子类的声明只需包含新创建的补充方法的名称。

```python
class PredatoryCreditCard(CreditCard):
	_ _slots_ _ = '_apr'
```

我们将在所有期望有很多实例的嵌套类中使用显示的_ _slots_ _声明。

### ==2.6	深拷贝和浅拷贝==

我们考虑的是拷贝对象的一个副本，而不是一个别名。我们需要一种**独立**的方式修改原始或拷贝的内容。

==①当我们直接使用赋值语句时，直接在b中添加或删除元素，将直接作用到a上。==

```python
a = [1,2,3]
b = a
b.append(4)
print(a)
print(b)
>>>
[1, 2, 3, 4]
[1, 2, 3, 4]
```

![image-20200925212339763](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20200925212339763.png)

==②**浅拷贝**==
我们可以使用list语法创建一个新的列表实例：

```python
a = [1,2,3]
b = list(a)
b[0] = 0
print(a)
print(b)
>>>
[1, 2, 3]
[0, 2, 3]
```

在这种情况下，我们显式调用列表构造函数，将第一个列表作为参数，这将导致一个新的列表被创建，称为浅拷贝。此时我们可以向b中添加或删除元素而不影响a。

![image-20200925212756788](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20200925212756788.png)

==③**深拷贝**==
创建一个深拷贝，可以通过<u>显式复制</u>原始实例来填充列表。python提供了一个很方便的模块，即copy，能产生任意对象的浅拷贝和深拷贝。
copy模块有两个函数：copy函数和deepcopy函数。copy函数创建对象的浅拷贝，deepcopy函数创建对象的深拷贝。

```python
import copy 
a = [1,2,3]
b = copy.deepcopy(a)
b[0] = 0
print(a)
print(b)
>>>
[1, 2, 3]
[0, 2, 3]
```

![image-20200925213425479](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20200925213425479.png)

## 第3章 算法分析

<u>**数据结构**</u>是组织和访问数据的一种系统化方式，<u>**算法**</u>是在有限的时间里一步步执行某些任务的过程。

3.2	算法分析中最重要的7种函数
**3.2.1	常数函数**

```
f(n)=c
```

常数函数描述了在计算机上需要做的基本操作步数。

**3.2.2	对数函数**

```
f(n)=log(b^n)
```

**3.2.3	线性函数**

```
f(n)=n
```

线性函数出现在必须对所有n个元素做基本操作的算法分析的任何时间。例如，比较数字x与大小为n的序列中的每个元素，需要做n次比较。

**3.2.4	$nlogn$函数**

```
f(n)=nlogn
```

该函数出现在对n个任意数进行排序且运行时间与$nlogn$成比例的最快可能算法。

**3.2.5	二次函数**

```
f(n)=n^2
```

许多算法都有嵌套循环，其中内循环执行一个线性操作数，外循环着表示执行线性操作数的次数。此时算法执行了n*n=$n^2$个操作。

**3.2.6	三次函数和其他多项式**

```
f(n)=n^3
```

多项式
```
f(n)=a0+a1*n+a2*n^2+...+ad*n^d
```
求和
                                 $\sum_{i=a} ^b \ f(i) =f(a)+f(a+1)+...+f(b) $

循环的运行时间自然会引起求和。

**3.2.7	指数函数**

```
f(n)=b^n
```

函数f(n)分配给输入参数n的值是通过底数b乘以它自己n次获得的。

**3.2.8	比较增长率**

![image-20200928160548710](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20200928160548710.png)

在算法分析中使用的7个基本函数的增长率。我们希望数据结构的操作运行时间与<u>常数函数</u>或<u>对数函数</u>成正比，算法以<u>线性函数</u>或<u>$nlogn$函数</u>来运行。

3.3.1	算法复杂度
大O符号==（最高次项的量级，不高于）==表示最坏情况下的算法复杂度
大Ω符号==（最低次项的量级，不低于）==表示最好情况下的算法复杂度
大θ符号==（中间次项的量级，等同于）==介于最坏最好之间的算法复杂度

## 第4章 递归

递归是一种技术，这种技术通过一个函数在执行过程中一次或多次调用其本身，或者通过一种数据结构在其表示中依赖于相同类型的结构更小的实例。

4.1.1	阶乘函数的递归实现

```python
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)
```

![image-20200928212138125](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20200928212138125.png)

​                                                    **阶乘函数的递归追踪**

每一个新的递归函数调用用一个向下的箭头指向新的调用来表示。函数返回时，用一个弯曲的箭头表示，并将返回值标在箭头旁边。
在python中，每当一个函数（递归或其他方式）被调用时，都会创建一个被称为活动记录或框架的结构来存储信息，这些信息是关于函数调用过程的。这个活动记录包含一个用来存储函数调用的<u>参数</u>和<u>局部变量</u>的命名空间，以及关于在这个函数体中当前正在执行的命令的信息。

4.1.2	绘制英式标尺的函数的递归实现

```python
def draw_line(tick_length, tick_label=''):
  line = '-' * tick_length
  if tick_label:
    line += ' ' + tick_label
  print(line)

def draw_interval(center_length):
  if center_length > 0:                   
    draw_interval(center_length - 1)      
    draw_line(center_length)              
    draw_interval(center_length - 1)      

def draw_ruler(num_inches, major_length):
  draw_line(major_length, '0')            
  for j in range(1, 1 + num_inches):
    draw_interval(major_length - 1)       
    draw_line(major_length, str(j))       
```

![image-20200928212940583](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20200928212940583.png)

​                                               **用递归追踪说明标尺的绘制**

### ==4.1.3	二分查找==

当序列无序时，使用**顺序查找**算法，最坏情况是每个元素遍历一遍，时间复杂度为O(n)；
当序列有序时，使用**二分查找**算法，算法维持两个参数low和high，这样可使所有候选条目的索引位于low和high之间，然后比较目标值和中间值候选项，即索引项[mid]的数据。mid=[(low+high)/2]。此时，①若目标值<[mid]的数据，对前半部分序列重复这一过程，即索引范围从low到mid-1。②若目标值>[mid]的数据，对后半部分序列重复这一过程，即索引范围从mid+1到high。时间复杂度为O($logn$)

```python
def binary_search(data, target, low, high):
  if low > high:
    return False                    
  else:
    mid = (low + high) // 2
    if target == data[mid]:         
      return True
    elif target < data[mid]:
      return binary_search(data, target, low, mid - 1)
    else:
      return binary_search(data, target, mid + 1, high)
```

![image-20200928215311217](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20200928215311217.png)

​                                                    **目标值22的二分查找的例子**

4.1.4	文件系统递归追踪

```python
import os
def disk_usage(path):
  total = os.path.getsize(path)                 
  if os.path.isdir(path):                        
    for filename in os.listdir(path):           
      childpath = os.path.join(path, filename)  
      total += disk_usage(childpath)  #递归       

  print ('{0:<7}'.format(total), path)           
  return total    
>>> disk_usage(r'C:\Users\rt\courses')
8  C:\Users\rt\courses\cs016\grades
3  C:\Users\rt\courses\cs016\homeworks\hw1
2  C:\Users\rt\courses\cs016\homeworks\hw2
...
5124  C:\Users\rt\courses
```

![image-20200930105354763](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20200930105354763.png)

4.1.5	Python中的最大递归深度
递归可能存在<u>无限递归</u>！为了解决这个问题，Python解释器可以动态重置，以更改默认的递归限制。通过使用sys模块和其getrecursionlimit函数和setrecursionlimit函数实现。

```python
import sys
old = sys.getrecursionlimit()  #默认递归上限次数为1000
sys.setrecursionlimit(100)   #上限改为100
```

4.4	其他递归
如果一个递归调用最多开始一个其他递归调用，我们称之为<u>线性递归</u>；
如果一个递归调用可以开始两个其他递归调用，我们称之为<u>二路递归</u>；
如果一个递归调用可以开始三个或者更多其他递归调用，我们称之为<u>多重递归</u>。
4.4.1	线性递归
递归计算序列元素和、二分查找、阶乘函数、幂函数
4.4.2	二路递归
英式标尺、bad_fibonacci、二分求和
4.4.3	多重递归
文件系统、

### ==4.5	设计递归==

- ==对于基本情况的测试。==首先测试一组基本情况（至少应该有一个）。这些基本情况应该被定义，以便每个可能的递归调用链最终会达到一种基本情况，并且每个基本情况的处理不应使用递归。
- ==递归。==我们定义每个可能的递归调用，以便使调用向一种基本情况靠近。

**参数化递归**

```python
def binary_sum(S, start, stop):
  """Return the sum of the numbers in implicit slice S[start:stop]."""
  if start >= stop:                      
    return 0
  elif start == stop-1:                  
    return S[start]
  else:                                  
    mid = (start + stop) // 2
    return binary_sum(S, start, mid) + binary_sum(S, mid, stop)
```

**非递归实现**

```python
def binary_search_iterative(data, target):
  """Return True if target is found in the given Python list."""
  low = 0
  high = len(data)-1
  while low <= high:
    mid = (low + high) // 2
    if target == data[mid]:         
      return True
    elif target < data[mid]:
      high = mid - 1                
    else:
      low = mid + 1                 
  return False                      
```

## 第5章 基于数组的序列

5.2.1	引用数组

Python使用数组内部存储机制（即对象引用，来表示一列或元组实例。在最低层，存储的是一块连续的内存地址序列，这些地址指向一组元素序列。）

![image-20201106213648775](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20201106213648775.png)

5.2.2	紧凑数组

紧凑数组–就是数组存储的是原始数据，而不是元素的引用。像字符串就是采用的这种结构。

紧凑结构的优点：

- 1.使用紧凑结构会占用更少的内存
- 2.高性能计算

5.3	动态数组

python的列表类提供了更有趣的抽象。虽然列表在被构造时已经有了确定的长度，但该类可以进行增添操作，对列表的大小没有明显的限制。为了实现这种抽象，我们就需要用到动态数组这种算法技巧。

假如用户持续增添列表元素，所有的预留单元被耗尽。此时，列表类向系统请求一个新的、更大的数组，并初始化该数组，使其前面的部分能与原来的小数组一样。届时，原来的数组不再需要，因此被系统回收。

5.3.1	动态数组实现步骤

1)	分配一个更大的数组B。
2)	设B[i]=A[i] (i=0,…,n-1)，其中n表示条目的当前数量。
3)	设A=B，也就是说以后使用B作为数组来支持列表。
4)	在新的数组里增添元素。

![image-20201106221631349](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20201106221631349.png)

### **==摊销分析==**

5.3.2	动态数组的==摊销分析==

为什么数组替换总是增大一倍的容量？
在数组的替换过程中，由于增大了1倍的容量，新数组在被替换之前允许增添n个新元素。这种方式使得每一次==<u>大的代价的替换</u>==（数组满了）过程后，对每个元素进行添加操作。
![image-20201106224626010](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20201106224626010.png)

例子：

![image-20201108110821542](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20201108110821542.png)

![image-20201108110744509](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20201108110744509.png)

5.5	使用基于数组的序列

5.5.1	为游戏存储高分（移位部分code）

```python
# shift lower scores rightward to make room for new entry
j = self._n - 1
while j > 0 and self._board[j-1].get_score() < score:
  self._board[j] = self._board[j-1]# shift j-1 to j
  j -= 1                      # and decrement j
self._board[j] = entry        # when done, add new entry
```

![image-20201108153732218](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20201108153732218.png)

5.5.2	插入排序

外层循环轮流考虑每个元素，内层循环移动正被考虑的元素。

```python
def insertion_sort(A):
  """Sort list of comparable elements into nondecreasing order."""
  for k in range(1, len(A)):   # from 1 to n-1
    cur = A[k]       # current element to be inserted
    j = k            # find correct index j for current
    while j > 0 and A[j-1] > cur:    # element A[j-1] must be after current
      A[j] = A[j-1]
      j -= 1
    A[j] = cur         # cur is now in the right place

```

![image-20201108164902447](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20201108164902447.png)

图中每一行对应外部循环的一次迭代，一行内的每一次复制对应内层循环的一次迭代。

### **==列表推导式==**

列表推导式（又称列表解析式）提供了一种简明扼要的方法来创建列表。

它的结构是在一个中括号里包含一个表达式，然后是一个for语句，然后是 0 个或多个 for 或者 if 语句。那个表达式可以是任意的，意思是你可以在列表中放入任意类型的对象。返回结果将是一个新的列表，在这个以 if 和 for 语句为上下文的表达式运行完成之后产生。

==列表推导式的执行顺序：==各语句之间是嵌套关系，最左边语句是最外层，依次往右进一层，最右边语句是最后一层。

```python
[x*y for x in range(1,5) if x > 2 for y in range(1,4) if y < 3]
```

执行顺序是:

```python
for x in range(1,5)
    if x > 2
        for y in range(1,4)
            if y < 3
                x*y
```

5.6	多维数据集（创建多维列表）
==错误写法==

```python
data = ([0]*c)*r
>>>[2,4,6]*2 = [2,4,6,2,4,6]
data = [[0]*c]*r
```

![image-20201108233915307](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20201108233915307.png)

data列表的所有r个条目都指向了同一个实例，该实例即为有c个0的列表。

==正确写法==

```python
data = [[0]*c for j in range(r)]
```

![image-20201108234242948](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20201108234242948.png)

正确实例化二维列表，我们必须确保原始列表的每个单元都能指向一个独立的第二集列表。

## 第6章 栈、队列和双端队列

6.1	栈

栈是由一系列对象组成的一个集合，这些对象的插入和删除操作遵循后进先出（LIFO）的原则。栈是一个基本的数据结构。

6.1.2	基于数组的栈实现（用list类实现一个栈）

| 表6—1 通过改变一个列表实现一个栈|            |
| :------------------| :--------- |
| **栈的基本方法**                     |用列表实现            |
| **S.push(e)**                    |L.append(e)            |
| **S.pop()**                      |L.pop()   |
| **S.top()**                      | L[-1] |
| **S.is_empty()**                 | len(L)=0   |
| **len(S)**                       |  len(L)          |

**代码段6-2	基于数组的栈的实现**

```python
class ArrayStack:
  """LIFO Stack implementation using a Python list as underlying storage."""

  def __init__(self):
    """Create an empty stack."""
    self._data = []            # nonpublic list instance

  def __len__(self):
    """Return the number of elements in the stack."""
    return len(self._data)

  def is_empty(self):
    """Return True if the stack is empty."""
    return len(self._data) == 0

  def push(self, e):
    """Add element e to the top of the stack."""
    self._data.append(e) # new item stored at end of list

  def top(self):
    """Return (but do not remove) the element at the top of the stack.

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise Empty('Stack is empty')
    return self._data[-1]   # the last item in the list

  def pop(self):
    """Remove and return the element from the top of the stack (i.e., LIFO).

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise Empty('Stack is empty')
    return self._data.pop()  # remove last item from list
```

6.2	队列

队列是一个基本的数据结构。队列是由一系列对象组成的集合，这些对象的插入和删除遵循先进先出（FIFO）的原则。允许插入的一端称为队尾，允许删除的一端称为队头。

| 队列的基本方法 |      |
| ----------------- | ---- |
| **Q.enqueue(e):** |向队列Q的队尾添加一个元素      |
| **Q.dequeue():** |从队列Q中移除并返回第一个元素      |
| **Q.first():**       |在不移除的前提下返回队列的第一个元素      |
| **Q.is_empty():**             |判断队列Q是否为空      |
| **len(Q)**              |返回队列Q中元素的数量      |

6.2.2	循环队列

![image-20201111110515604](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20201111110515604.png)

用循环数组的方式实现时，为了判断队列是否为空或者满，可以采用以下方式：

   1) 设队列最大容量为 max_size，那么要开一个长度为 max_size+1的数组。因为，队列为0, 1, ..., max_size 个元素共 max_size+1 种状态。 
   2) 如上图所示， 设 rear 为当前队列尾部元素在数组中的下标位置，front 为**当前队列头部元素的逻辑上前一个位置**的数组下标，存储队列元素的数组下标范围 0 ~ max_size，则：
     初始时，front = rear = 0。
	 当有元素入队时，先判断是否满，不满则更新尾部位置 ==rear = (rear + 1) % (max_size + 1)==，然后将新入队元素加到数组下标为 rear 处。
     当有元素出队时，先判断是否空，不空则更新头部位置 ==front = (front + 1) % (max_size + 1)==，然后该 front 位置元素为出队元素。
      ==队列为满的条件是：(rear + 1) % (max_size + 1) == front。==
      ==队列为空的条件是：front == rear。==

**代码段6-6	基于数组的队列的实现**

```python
class ArrayQueue:
  """FIFO queue implementation using a Python list as underlying storage."""
  DEFAULT_CAPACITY = 10 #moderate capacity for all new queues

  def __init__(self):
    """Create an empty queue."""
    self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
    self._size = 0
    self._front = 0

  def __len__(self):
    """Return the number of elements in the queue."""
    return self._size

  def is_empty(self):
    """Return True if the queue is empty."""
    return self._size == 0

  def first(self):
    """Return (but do not remove) the element at the front of the queue.

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Empty('Queue is empty')
    return self._data[self._front]

  def dequeue(self):
    """Remove and return the first element of the queue (i.e., FIFO).

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Empty('Queue is empty')
    answer = self._data[self._front]
    self._data[self._front] = None #help garbage collection
    self._front = (self._front + 1) % len(self._data)
    self._size -= 1
    if 0 <self._size<len(self._data)//4:
        self._resize(len(self._data//2))#缩减底层数组
    return answer

  def enqueue(self, e):
    """Add an element to the back of queue."""
    if self._size == len(self._data):
      self._resize(2 * len(self.data)) # double arraysize
    #可用插入的队尾索引
    avail = (self._front + self._size) % len(self._data)
    self._data[avail] = e
    self._size += 1

  def _resize(self, cap):    # we assume cap >= len(self)
    """Resize to a new list of capacity >= len(self)."""
    old = self._data         # keep track of existing list
    self._data = [None] * cap   # allocate list with new capacity
    walk = self._front
    for k in range(self._size): # only consider existing elements
      self._data[k] = old[walk]  # intentionally shift indices
      walk = (1 + walk) % len(old)  # use old size as modulus
    self._front = 0           # front has been realigned
```

6.3	双端队列

双端队列是一个类队列的数据结构，支持在队列的头部和尾部都进行插入和删除操作。

| 双端队列的基本方法 |      |
| ----------------- | ---- |
| **D.adda_first(e):** |向双端队列D的前面添加一个元素e     |
| **D.add_last(e):** |向双端队列D的后面添加一个元素e      |
| **D.delete_first():**       |从双端队列D中移除并返回第一个元素      |
| **D.delete_last():**       |从双端队列D中移除并返回最后一个元素      |
| **D.first():**             |返回但不移除双端队列D的第一个元素      |
| **D.last():**             |返回但不移除双端队列D的最后一个元素      |
| **D.is_empty():**             |判断双端队列D是否为空      |
| **len(D)**              |返回双端队列D中元素的数量      |

**代码段6-7	基于数组的双端队列的实现**

```python
class DeArrayQueue(object):
   '''deque's ADT one parameter for the maxlen'''
   DEFAULT_LEN =10
   def __init__(self,maxlen=None):
      if maxlen!=None and maxlen<DeArrayQueue.DEFAULT_LEN:  #change the default len
         DeArrayQueue.DEFAULT_LEN=maxlen
      self._data=[None]*DeArrayQueue.DEFAULT_LEN
      self.maxlen=maxlen
      self._size=0
      self._front=0

   def __len__(self):
      return self._size
   
   def add_first(self,num):
      '''add a integer from the left'''
      #if self.maxlen!=None and self._size==self.maxlen:
      #   raise Exception('there is fulled!')
      if self._size==len(self._data):
      #exptend the data list，if size == maxlen,size-=1
         self._resize(2)       
      #在队头加入元素后，更新front指针位置
      self._front=(self._front-1+len(self._data))%len(self._data)
      self._data[self._front]=num
      self._size+=1

   def _resize(self, cap):   
      '''need a multiple to change self._data len,but dont max the maxlen'''
      #6.33
      if self.maxlen!=None and self.maxlen==self._size:
         self._size-=1          #when size == maxlen,need sub 1                      
         return
      if self.maxlen!=None and int(self._size*cap)>self.maxlen: #accurate expand the self._data
         temp=[None]*self.maxlen
      else:
         temp=[None]*int(len(self._data)*cap)
      for i in range(self._size):  #use the remainder to get the realy integer from old data
         #print(i,self._size,len(temp))       
         temp[i]=self._data[(self._front+i)%len(self._data)]
      self._data=temp
      self._front =0

   def add_last(self,num):
      ''' add a integer from the right'''
      #if self.maxlen!=None and self._size==self.maxlen:
      #   raise Exception('there is fulled!')
      if self._size==len(self._data):  #exptend the data list
         self._resize(2)            #get the new rear
      rear=(self._front+len(self._data)+self._size)%len(self._data)
      self._data[rear]=num
      self._size+=1

   def delete_first(self):
      '''  pop a integer from the left'''
      if self._size==0:
         raise Exception('Empty')
      if self._size==len(self._data)//4: #reduce the data list
         self._resize(1/2)
      temp=self._data[self._front]
      self._data[self._front]=None                             self._front=(self._front+1+len(self._data))%len(self._data) #get the new front
      self._size-=1
      return temp

   def delete_last(self):
      '''pop a integer from the right'''
      if self._size==0:
         raise Exception('Empty')
      if self._size==len(self._data)//4:        #reduce the data list
         self._resize(1/2)
      rear=(self._front-1+len(self._data)+self._size)%len(self._data)   #get the new rear
      temp=self._data[rear]
      self._data[rear]=None
      self._size-=1
      return temp

   def first(self):
      '''return the first integer of the duqueue'''
      return self._data[self._front]
   
   def last(self):
      '''return the last integer of the dequeue'''
      #返回双端队列的最后一个元素
      return self._data[(self._front-1+self._size)%len(self._data)]
```

## 第7章 链表（单向、循环、双向）

数组提供更加集中的表示法，一个大的内存块能够为许多元素提供存储和引用；
链表依赖于更多的分布式表示方法，采用<u>节点</u>的轻量级对象。每个节点包含元素引用（内容）和指向相邻节点的引用（地址）。

节点称为“对象”，每个节点指向“next”节点的引用称为“指针”。
==头指针（head）、尾指针（tail）包括整个节点，即内容和地址。==

7.1	单向链表
单向链表是由多个节点的集合共同构成的一个线性序列。

<img src="C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20201114163932098.png" alt="image-20201114163932098" style="zoom: 50%;" />

​                                                           单向链表基本单元

![image-20201114203148761](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20201114203148761.png)

​                                                                    单向链表

**在单链表头部插入元素**

![image-20201114164523576](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20201114164523576.png)

**在单链表头部删除元素**

![image-20201114164832600](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20201114164832600.png)

**在单链表尾部插入元素**

![image-20201114165022148](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20201114165022148.png)

**在单链表尾部删除元素**（因为单链表不走回头路，所以不建议操作）

### **==Class Node （单向链表节点类）==**

```python
class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):# initialize node
      self._element = element # reference to element
      self._next = next       # reference to next node
```

**next包含下一个node的所有信息（element、next）**

7.11	用单向链表实现栈

压栈操作（插入）：

```python
self.head = self.Node(e,self.head)
self.size+=1
```

出栈操作（删除）：

```python
answer = self.head.element;
self.head = self.head.next;
self.size-=1
```

7.12	用单向链表实现队列

入队操作

```python
def dequeue(self):
    if self.is_empty():
      raise Empty('Queue is empty')
    answer = self._head._element
    self._head = self._head._next
    self._size -= 1
    if self.is_empty():                     
      self._tail = None                     
    return answer
```

出队操作

```python
 def enqueue(self, e):
    newest = self._Node(e, None)            
    if self.is_empty():
      self._head = newest                   
    else:
      self._tail._next = newest
    self._tail = newest                     
    self._size += 1
```

7.2.2	循环链表实现队列

没有特定的头节点、尾节点，采用“current”标识符来表示一个指定的节点。

出队操作

```python
def dequeue(self):
    if self.is_empty():
      raise Empty('Queue is empty')
    oldhead = self._tail._next
    if self._size == 1:                   
      self._tail = None                   
    else:
      self._tail._next = oldhead._next    
    self._size -= 1
    return oldhead._element
```

入队操作

```python
 def enqueue(self, e):
    newest = self._Node(e, None)          
    if self.is_empty():
      newest._next = newest       # initialize circularly
    else:
      newest._next = self._tail._next # new node points to head
      self._tail._next = newest # old tail points to new node
    self._tail = newest        # new node becomes the tail
    self._size += 1
```

7.3	双向链表
双向链表：每个节点都维护了指向其先驱节点以及后继节点的引用。

<img src="C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20201114203036513.png" alt="image-20201114203036513" style="zoom:50%;" />

​                                                          双向链表基本单元

![image-20201114205836724](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20201114205836724.png)

​                                                                   双向链表

### **==Class Node （双向链表节点类）==**

```python
class _Node:
    __slots__ = '_element', '_prev', '_next'            

    def __init__(self, element, prev, next):# initialize node's 
      self._element = element  # user's element
      self._prev = prev        # previous node reference
      self._next = next        # next node reference
```

**prev包含上一个node的所有信息（element、prev、next）**
**next包含下一个node的所有信息（element、prev、next）**

7.3.1	双向链表的基本实现

**添加节点**

```python
def _insert_between(self, e, predecessor, successor):
    newest = self._Node(e, predecessor, successor) # linked to neighbors
    predecessor._next = newest
    successor._prev = newest
    self._size += 1
    return newest
```

![image-20201114212217168](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20201114212217168.png)

**删除节点**

```python
def _delete_node(self, node):
    predecessor = node._prev
    successor = node._next
    predecessor._next = successor
    successor._prev = predecessor
    self._size -= 1
    element = node._element      # record deleted element
    node._prev = node._next = node._element = None #删点
    return element               # return deleted element
```

![image-20201114212430144](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20201114212430144.png)

7.3.2	用双向链表实现双端队列

双端队列在队头队尾进行插入、删除操作：

```python
 def insert_first(self, e):
    """Add an element to the front of the deque."""
    self._insert_between(e, self._header, self._header._next)   # after header

  def insert_last(self, e):
    """Add an element to the back of the deque."""
    self._insert_between(e, self._trailer._prev, self._trailer) # before trailer

  def delete_first(self):
    """Remove and return the element from the front of the deque."""
    if self.is_empty():
      raise Empty("Deque is empty")
    return self._delete_node(self._header._next)   # 继承

  def delete_last(self):
    """Remove and return the element from the back of the deque."""
    if self.is_empty():
      raise Empty("Deque is empty")
    return self._delete_node(self._trailer._prev)  # 继承
```

### **7.4	位置列表的抽象数据类型（Class PositionalList）**

位置实例方法
| 表7—1   <br /><u>位置访问器方法</u> |            |
| :------------------| :--------- |
| **p.element()**             | 返回存储在位置p的元素               |
| **L.first()、L.last()** |返回列表L中第（最后）一个元素的位置，空为None  |
| **L.before(p)、L.after(p)** |返回L中p紧邻的前（后）面元素的位置，空为None |
| **L.is_empty()**     | 判断L是否为空 |
| **len(L)**            | 返回列表元素个数   |
| **iter(L)**                       |  返回列表元素的前向迭代器          |
| <u>**位置更新方法**</u> |  |
| **L.add_first(e)、L.add_last(e)** | 在L的前（后）面插入新元素e，返回新元素的位置 |
| **L.add_before(e)、L.add_after(e)** | 在L中位置p之前（后）插入一个新元素e，返回新元素的位置 |
| **L.replace(p,e)** | 用元素e取代位置p处的元素，返回之前p位置处的元素 |
| **L.delete(p)** | 删除并返回L中位置p处的元素，取消该位置 |

实现代码在书p184

7.5	基于双向链表实现插入排序

```python
def insertion_sort(L):
  if len(L) > 1:         # otherwise, no need to sort it
    marker = L.first()
    while marker != L.last():
      pivot = L.after(marker)       # next item to place
      value = pivot.element()
      if value > marker.element():  # pivot is already sorted
        marker = pivot        # pivot becomes new marker
      else:                   # must relocate pivot
        walk = marker         # find leftmost item＞value
        while walk != L.first() and L.before(walk).element() > value:
          walk = L.before(walk)
        L.delete(pivot)
        L.add_before(walk, value)   # reinsert value before walk
```

7.7	基于链表的序列与基于数组的序列

### **==基于数组的序列的优点==**

①数组提供时间复杂度为O(1)的基于整数索引的访问一个元素的方法。
②通常，具有等效边界的操作使用基于数组的结构运行一个常数因子比基于链表的结构运行更有效率
③相较于链式结构，基于数组的表示使用存储的比例更少。因为对于链表，内存不仅要存储每个所包含的对象的引用，还要明确地存储各个节点的引用。一个长度为n的单向链至少需要2n个引用（每个节点的元素引用和指向下个节点引用）

### **==基于链表的序列的优点==**

①基于链表的结构为他们的操作提供最坏情况的时间界限。当用于一个实时系统，我们仅关心总时间，数组的单（摊销）操作导致的长时间延迟可能造成较大的时间成本。
②插入、删除操作时间复杂度为O(1)。

## 第8章 树

树是一种将元素分层次存储的抽象数据类型。除了最顶部的元素，每个元素在树中都有1个父节点和0个或多个子节点。

树T定义为**存储一系列元素的有限节点集合，这些节点具有parent-children关系且满足如下属性：**

- 如果树T不为空，则一定有一个**根节点**，根节点没有父节点。
- 每个非根节点v都有唯一父节点w，每个v都是节点w的子节点

同一个父节点的子节点之间为**兄弟**关系，无子节点的节点为**叶子/外部**节点，有子节点的节点为**内部**节点。

树T的一条**边**指的是一对节点(u,v)，u是v的父节点或v是u的父节点；树T中的**路径**指的是一系列的节点，这些节点任意两个连续的节点之间都是一条边。

**有序树**通常按照从左至右的顺序对兄弟节点进行排序。

| 表8—1   树的位置对象方法 |            |
| :------------------| :--------- |
| **p.element()**             | 返回存储在位置p的元素               |
| **T.root()** |返回树T的根节点位置，空为None  |
| **T.is_root(p)** | 如果位置p是树T的根，返回True                          |
| **T.parent(p)** | 返回位置p的父节点的位置，如果p为根节点，返回None |
| **T.num_children(p)** | 返回位置p的子节点的编号 |
| **T.children(p)**      | 产生位置p的子节点的一个迭代                         |
| **T.is_leaf(p)** | 如果位置p没有任何子节点，返回True   |
| **len(T)** | 返回树T所包含的元素的数量 |
| **T.is_empty(p)** | 如果树T不包含任何节点，则返回True  |
| **T.positions** | 生成树T所有位置的迭代 |
| **iter(T)** | 生成树T中存储的所有元素的迭代 |

8.1.3	计算深度和高度
	p是树T中的一个节点，<u>p的深度就是p的祖先个数/p的层数（根节点深度为0）/根节点到p的路径长度</u>；<u>p的高度就是p的子孙个数/p节点到叶子节点的最长路径的长度（叶子节点高度为0）</u>。

**p的深度递归定义**

- 如果p是根节点，深度为0
- 否则，p的深度就是父节点的深度加1

```python
 def depth(self, p):
    """Return the number of levels separating Position p from the root."""
    if self.is_root(p):
      return 0
    else:
      return 1 + self.depth(self.parent(p))
```

**p的高度递归定义**

- 如果p是一个叶子节点，高度为0
- 否则，p的深度就是子节点的最大高度加1

```python
def _height2(self, p):                
    """Return the height of the subtree rooted at Position p."""
    if self.is_leaf(p):
      return 0
    else:
      return 1 + max(self._height2(c) for c in self.children(p))
```

### ==8.2	二叉树==

二叉树具有以下属性的有序树：
1）每个节点最多有两个子节点
2）每个子节点称为左孩子或右孩子
3）对于每个节点的子节点，在顺序上，左孩子先于右孩子
**左子树**、**右子树**：若子树的根为内部节点v的左孩子或右孩子，则该子树被称为节点v的**左子树**或**右子树**。

==定义一==
**完全二叉树：**一棵深度为k的有n个结点的二叉树，对树中的结点按从上至下、从左到右的顺序进行编号，如果编号为i（1≤i≤n）的结点与满二叉树中编号为i的结点在二叉树中的位置相同，则这棵二叉树称为完全二叉树。
**满二叉树：**深度为k且有2^k-1个结点的二叉树称为满二叉树。
![image-20201126232148247](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20201126232148247.png)

==定义二==

**完全二叉树/满二叉树：**除了最后一个叶子节点的父节点之外，若每个节点都有0个或2个子节点，则这样的二叉树为完全/满二叉树。
**不完全二叉树：**在完全二叉树中，每个内部节点都恰好有两个子节点。若二叉树不完全，则为不完全二叉树。

==决策树是完全二叉树。==
![image-20201126232847646](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20201126232847646.png)

8.2.1	二叉树的ADT

| 表8—2   二叉树访问方法 |                                             |
| :--------------------- | :------------------------------------------ |
| **T.left(p)**          | 返回p左孩子的位置，若无左孩子，返回None     |
| **T.right(p)**         | 返回p右孩子的位置，若无右孩子，返回None     |
| **T.sibling(p)**       | 返回p兄弟节点的位置，若无兄弟节点，返回None |

前面我们将Tree定义为抽象基类，依据继承性，对二叉树ADT定义一个新的BinaryTree类，该类保持抽象性，新的BinaryTree类声明了新的抽象方法left和right。

```python
from .tree import Tree
class BinaryTree(Tree):
  """在Tree抽象基类中扩展的二叉树抽象基类"""
  # ----------- additional abstract methods -----------
  def left(self, p):
    """Return a Position representing p's left child.
 Return None if p does not have a left child.
    """
    raise NotImplementedError('must be implemented by subclass')

  def right(self, p):
    """Return a Position representing p's right child.
Return None if p does not have a right child.
    """
    raise NotImplementedError('must be implemented by subclass')

  # --- concrete methods implemented in this class -----
  def sibling(self, p):
    """Return a Position representing p's sibling (or None if no sibling)."""
    parent = self.parent(p)
    if parent is None:             # p must be the root
      return None                  # root has no sibling
    else:
      if p == self.left(parent):
        return self.right(parent)   # possibly None
      else:
        return self.left(parent)    # possibly None

  def children(self, p):
    """Generate an iteration of Positions representing p's children."""
    if self.left(p) is not None:
      yield self.left(p)
    if self.right(p) is not None:
      yield self.right(p)
```

**二叉树属性：**

![image-20201127195604478](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20201127195604478.png)

### 8.3.1	二叉树的链式存储结构

![image-20201127200850357](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20201127200850357.png)

实现二叉树ADT方法：定义一个简单、非公开的_Node类表示一个节点，再定义一个公开的Position类用于封装节点。

#### ==链式二叉树==

![image-20201127204021875](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20201127204021875.png)

#### 链式二叉树类的==公开方法==

![image-20201127204233544](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20201127204233544.png)

#### 链式二叉树类的==私有更新方法==（不被子类继承）

| 表8—3 链式二叉树更新方法 |                                             |
| :----------------------- | :------------------------------------------ |
| **T.add_root(e)**            | 为空树创建根节点，元素为e，并返回根节点位置。若树非空，抛出错误 |
| **T.add_left(p,e)**           | 创建新节点，元素为e，将该节点链接为位置p的左孩子，返回结果位置。若p有左孩子，抛出错误 |
| **T.add_right(p,e)**           | 创建新节点，元素为e，将该节点链接为位置p的右孩子，返回结果位置。若p有右孩子，抛出错误 |
| **T.replace(p,e)**           | 用元素e替换存储在位置p的元素，返回之前存储的元素 |
| **T.delete(p)**           | 移除位置为p的节点，用其孩子代理，若有（无），返回存储在p中的元素（None）；若p有两个孩子，抛出错误。 |
| **T.attach(p,T1,T2)**         | 将树T1,T2分别链接为T的叶子节点p的左右子树，并将T1,T2重置为空树。若p不是叶子节点，抛出错误。 |

![image-20201127205600977](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20201127205600977.png)![image-20201127205639365](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20201127205639365.png)![image-20201127205657818](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20201127205657818.png)

链式二叉树实现方式的性能

| 表8—4 链式二叉树方法运行时间 |                                                              |
| :--------------------------- | :----------------------------------------------------------- |
| **操作** | **运行时间** |
| **len,is_empty**            | O(1) |
| **root,parent,left,right,sibling,children,num_children**          | O(1)|
| **is_root,is_leaf**         | O(1) |
| **depth(p)**           | O(dp+1)            |
| **height**              | O(n) |
| **add_root,add_left,add_right,replace,delete,attach**        | O(1) |

### 8.3.2	基于数组表示的二叉树

对T的每个位置p，编号函数$f$称为二叉树T的层编号，设$f(p)$为整数且定义为下：

- 若p是T的根节点，则$f(p)$=0
- 若p是位置q的左孩子，则$f(p)$=2$f(p)$+1（奇数）
- 若p是位置q的右孩子，则$f(p)$=2$f(p)$+2（偶数）

层编号是基于树内的标记位置，而不是所给树的实际位置，因此编号不一定连续。

![image-20201127221754051](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20201127221754051.png)

基于数组的优点：位置易知（p左孩子下标为2$f(p)$+1、右孩子为2$f(p)$+2、父节点为$f(p)$-1/2向下取整）用heaps类表示空间高效
基于数组的缺点：插入和删除操作时间复杂度O(n)（孩子节点需要移动，孙子节点也需要移动）

**一般树（非二叉）的链式存储结构**

一般树的一个节点所拥有的孩子节点之间没有优先级限制，故可以使每个节点都配置一个容器（type：列表），该容器存储指向每个孩子的引用。

![image-20201127222927373](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20201127222927373.png)

| 表8—5 链式一般树方法运行时间    |              |
| :------------------------------ | :----------- |
| **操作**                        | **运行时间** |
| **len,is_empty**                | O(1)         |
| **root,parent,is_root,is_leaf** | O(1)         |
| **children(p)**                 | O(cp+1)      |
| **depth(p)**                    | O(dp+1)      |
| **height**                      | O(n)         |

### 8.4	树的遍历算法

**前序遍历&中序遍历&后序遍历**

![image-20201127225838764](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20201127225838764.png)
**DLR--前序遍历**（对于当前节点，先输出该节点，然后输出他的左孩子，最后输出他的右孩子 ）
**LDR--中序遍历**（对于当前结点，先输出它的左孩子，然后输出该结点，最后输出它的右孩子）
**LRD--后序遍历**（对于当前结点，先输出它的左孩子，然后输出它的右孩子，最后输出该结点）

**广度优先遍历/层序遍历**

​                                           ![image-20210313111228303](数据结构与算法（Python语言实现）.assets/image-20210313111228303.png)
​	**BFS--层序遍历**（按层，从上到下，从左到右遍历）

中序遍历的应用——==二叉搜索树==
		二叉搜索树或者是一棵空树，或者是具有下列性质的二叉树： <u>若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值； 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值； 它的左、右子树也分别为二叉排序树。</u>二叉搜索树作为一种经典的数据结构，它**既有链表的快速插入与删除操作的特点，又有数组快速查找的优势**；所以应用十分广泛，例如在文件系统和数据库系统一般会采用这种数据结构进行高效率的排序与检索操作。

**1.树的前序遍历**（一般树的默认迭代顺序）
<img src="C:\Users\Administrator\OneDrive\桌面\数据结构与算法\image-20210312103344457.png" alt="image-20210312103344457" style="zoom: 67%;" />

**2.树的后序遍历**
![image-20210312103413679](C:\Users\Administrator\OneDrive\桌面\数据结构与算法\image-20210312103413679.png)

**3.树的层序遍历**
![image-20201128171340621](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20201128171340621.png)

**4.树的中序遍历**（二叉树的默认迭代顺序）
![image-20210312103446256](C:\Users\Administrator\OneDrive\桌面\数据结构与算法\image-20210312103446256.png)

8.4.5	树遍历的应用：目录表、计算磁盘空间

### ==8.5	表达式树==

![image-20210312103757374](C:\Users\Administrator\OneDrive\桌面\数据结构与算法\image-20210312103757374.png)

表达式树的计算
![image-20210312103936729](C:\Users\Administrator\OneDrive\桌面\数据结构与算法\image-20210312103936729.png)

表达式树的创建
![image-20201128215113907](C:\Users\18613\AppData\Roaming\Typora\typora-user-images\image-20201128215113907.png)

## 第9章  优先级队列

优先级队列：这是一个包含优先级元素的集合，这个集合允许插入任意的元素，并允许删除拥有最高优先级的元素。通过提供一个==键==来为该元素赋予一定的优先级。键值最小的元素将是优先级最高（下一个从队列中移除）的元素（即：键值为1的元素优先级高于键值为2的元素）
        在优先级队列的模型中，元素一旦被加入优先级队列，键值将保持不变（元组特性）

| 优先级队列的抽象数据类型的实现 |                                      |
| -------------------- | ------------------------------------ |
| **P.add(k,v):**    | 向优先级队列P中插入一个拥有键k和值v的元组 |
| **P.min():**     | 返回一个优先级队列P中最小键值的元组(k,v)，不移除，队列空返回错误|
| **P.remove_min():**       | 移除一个优先级队列P中最小键值的元组(k,v)，并返回，(k,v)代表这个被移除的元组的键和值 |
| **P.is_empty():**    | 逻辑运算，判断是否为空                    |
| **len(P)**           | 返回优先级队列P中元组的数量                |

### 9.2	优先级队列的实现

9.2.1	组合设计模式

```python
代码段9-1，见书238
```

9.2.2	使用未排序列表实现优先级队列（必须检查所有元组才能找到键值最小元组）

```python
代码段9-2，见书239
```

9.2.3	使用排序列表实现优先级队列（第一个元组是最小键值元组）

```python
代码段9-3，见书240
```

| 表9-2 比较基于两种列表的实现     |  |  |
| :------------------------------ | :----------: | :-----------------------------: |
| **操作**                        | **未排序列表** | **排序列表** |
| **len**                | **O(1)** | **O(1)** |
| **is_empty** | **O(1)** | **O(1)** |
| **add**                 | **O(1)** | **O(n)** |
| **min**                    | **O(n)** | **O(1)** |
| **remove_min**                      | **O(n)** | **O(1)** |

**未排序列表插入操作快，查询和删除操作慢；排序列表查询和删除操作快，插入操作慢。**

### 9.3	堆

堆是一棵二叉树T，该树在他的节点上存储了集合中的元组并且满足两个附加属性：关系属性以存储键的形式在T中定义；结构属性以树T自身形式的方式定义。

![image-20210313105000816](数据结构与算法（Python语言实现）.assets/image-20210313105000816.png)

​		**Heap-Order属性**（关系属性附加属性）：在堆T中，对于除了根的每个位置p，存储在p中的键值大于或等于存储在p的父节点的键值。（子节点键值小于根节点）==一个最小的键总是存储在T的根节点中，调用min或remove_min时，时间复杂度较小。==该数据结构与Python运行环境的内存堆无关系。
​		**完全二叉树属性**（结构属性附加属性）：由于效率，堆T的高度应尽可能小，一个高度为h的堆T是一棵完全二叉树。
​		堆的高度：堆T有n个元组，则它的高度h=$\lfloor logn \rfloor$

9.3.2	用堆实现优先级队列

**min**

min操作简单，堆保证了树的根部元组有最小键值。

**add(k,v)**

新节点应该被放在位置p上，即树底层最右节点相邻的位置。若底层已满（或堆为空），则应存放在新一层的最左位置。因为是插入在最底层位置，所以很可能会破坏Heap-order属性，所以需要**堆向上冒泡**（即将添加的元素的优先级与其父节点相比较，如果小于父节点，则该元素与父节点交换，然后再与新的父节点比较，直到父节点小于了自己的优先级或者自己成为了根节点。）

![image-20210313115515801](数据结构与算法（Python语言实现）.assets/image-20210313115515801.png)![image-20210313115535743](数据结构与算法（Python语言实现）.assets/image-20210313115535743.png)

在最坏情况下，堆向上冒泡会一直移动到堆T的根节点位置，所以add方法所执行的交换次数在最坏情况下等于T的高度。时间复杂度为O(n)=h=$\lfloor logn \rfloor$

**remove_min**

首先将根节点与最下层的最右端的节点交换，然后删除这最下层最右端的节点，然后再进行**堆向下冒泡**（即为将根节点与两个孩子中最小的比较，如果该节点比孩子节点大，则与孩子节点交换，然后继续向下进行直到该节点比两个孩子节点都小或者该节点已经没有孩子了为止。如图：）。

![image-20210313120207514](数据结构与算法（Python语言实现）.assets/image-20210313120207514.png)![image-20210313120217933](数据结构与算法（Python语言实现）.assets/image-20210313120217933.png)![image-20210313120354551](数据结构与算法（Python语言实现）.assets/image-20210313120354551.png)![image-20210313120322932](数据结构与算法（Python语言实现）.assets/image-20210313120322932.png)

在最坏情况下，堆向下冒泡所执行的交换次数在最坏情况下等于堆T的高度。时间复杂度为O(n)=h=$\lfloor logn \rfloor$

9.3.3	基于数组的堆结构表示

![image-20210313121832497](数据结构与算法（Python语言实现）.assets/image-20210313121832497.png)

对于二叉树的实现，这次我们不使用链式结构，因为堆的排序中，需要定位最下层最右端的这个节点，链式实现起来较为复杂，同时堆是完全二叉树，所以使用基于列表的方式会使问题方便很多。

先介绍一下这种实现方式：

列表的首个元素即为二叉树的根节点，所以根节点的索引为1，设节点p的索引函数为f(p)

- 如果p是T的根节点，则f(p)=0.

- 如果p是位置q的左孩子，则f(p) = 2f(q)+1.

- 如果p是位置q的右孩子，则f(p) = 2f(q)+2.

列表中的最后一个元素就是二叉树的最下层的最右端的元素

#### 9.3.2	Python的堆实现

```python
代码段9-4.9-5，见书246
```

| 表9-3 基于堆的优先级列表实现 |              |
| :--------------------------- | :----------: |
| **操作**                     | **运行时间** |
| **len(),is_empty()**         |   **O(1)**   |
| **min()**                    |   **O(1)**   |
| **add()**                    | **O(logn)*** |
| **remove_min()**             | **O(logn)*** |

*如果是基于数组的，则为摊销结果。

9.3.7	Python的heapq模块

Python标准包含了heapq模块，但他并不是一个独立的数据结构，而是提供了一些函数，这些函数把列表当做堆进行管理，而且元素的优先级就是列表中的元素本身，除此之外它的模型与实现方式与刚才我们自己定义的基本相同：基于层次编号的索引，将n个元素存储在L[0]-L[n-1]的单元中，最小元素存储在根L[0]中。

| 表9-3 Heapq模块支持的函数 |                                                              |             |
| :------------------------ | :----------------------------------------------------------: | ----------- |
| **heappush(L,e)**         |              **将元素e存入列表L中并进行堆排序**              | **O(logn)** |
| **heappop(L)**            |         **取出并返回优先级最小的元素，并重新堆排序**         | **O(logn)** |
| **heappushpop(L,e)**      | **将e放入列表中，同时返回最小元素，相当于先执行push，再pop。** | **O(logn)** |
| **heapreplace(L,e)**      | **与heappushpop类似，是先执行pop，再执行push，即使新插入的元素是最小值也不能返回** | **O(logn)** |
| **heapify(L)**            | **将未堆排序的列表进行调整使之满足堆的结构。采用了自底向上的堆构造算法** | **O(n)**    |

### **9.4	使用优先级队列排序**

```Python
def pq_sort(C):
    """sort a collection of elements stored in a positional list."""
    n = len(C)
    P = PriorityQueue()
    for j in range(n):             #阶段一
        elemnet = C.delete(C.first())
        P.add(element,element)
    for j in range(n):             #阶段二
        (k,v) = P.remove_min()
        C.add_last()
```

#### **9.4.2 堆排序**

阶段一，由于第$i$次add操作完成后堆有$i$个元组，所以第$i$次add操作的时间复杂度为O($logi$)取决于树的高度/层数h，阶段一的整体时间复杂度为O($nlogn$)；阶段二，第$i$次remove_min操作的时间复杂度为o($log(n-j+1)$)向下冒泡。阶段二的整体时间复杂度为O($nlogn$)。

**步骤一 构造初始堆。将给定无序序列构造成一个大顶堆（一般升序采用大顶堆，降序采用小顶堆)。**

![image-20210313174536466](数据结构与算法（Python语言实现）.assets/image-20210313174536466.png)![image-20210313174554318](数据结构与算法（Python语言实现）.assets/image-20210313174554318.png)

<img src="数据结构与算法（Python语言实现）.assets/image-20210313174615782.png" alt="image-20210313174615782" style="zoom:150%;" />

![image-20210313174653469](数据结构与算法（Python语言实现）.assets/image-20210313174653469.png)

**步骤二 将堆顶元素与末尾元素进行交换，使末尾元素最大。然后继续调整堆，再将堆顶元素与末尾元素交换，得到第二大元素。如此反复进行交换、重建、交换。**

![image-20210313174725819](数据结构与算法（Python语言实现）.assets/image-20210313174725819.png)

![image-20210313174735339](数据结构与算法（Python语言实现）.assets/image-20210313174735339.png)

![image-20210313174745819](数据结构与算法（Python语言实现）.assets/image-20210313174745819.png)

![image-20210313174800507](数据结构与算法（Python语言实现）.assets/image-20210313174800507.png)



### 9.5	适应性优先级队列

为了实现更多自由度的方法，我们需要定义一些附加方法。

| 表9-5 适应性优先级队列 |                                            |                                              |
| :--------------------- | :----------------------------------------: | -------------------------------------------- |
| **P.update(loc,k,v)**  |  **用定位器loc代替键和值作为元组的标识**   | 加上第三个域变量                             |
| **P.remove(loc)**      | **删除以loc标识的特定元组，并返回(k,v)对** | 移除任意位置元组，并使用bubble函数维持堆属性 |

用一个定位器表示堆，数组中每个元组的索引对应每个定位器实例中的第三个元素。

![image-20210313185617527](数据结构与算法（Python语言实现）.assets/image-20210313185617527.png)

![image-20210313185635456](数据结构与算法（Python语言实现）.assets/image-20210313185635456.png)

上图显示了调用remove_min()方法后状态的一个例子。堆操作使得最小元组(4,C)被删除，并使元组(16,X)暂时从最后一个位置移到根位置，之后再向下冒泡。==这就是借助第三个域来指明该元素在堆中的位置。==

Python实现

```Python
代码段9-8、9-9，见书258页
def _bubble(self,j):
    """该函数保证堆中任意位置键改变时维持heap-order属性"""
    if j>0 and self._data[j]<self._data[self.parent(j)]: #j不是数组第一个元素&小于父节点
        self._upheap(j)                                  #向上冒泡
    else:
        self._downheap(j)
```

| 表9-5 基于堆的优先级列表实现 |              |
| :--------------------------- | :----------: |
| **操作**                     | **运行时间** |
| **len(),is_empty(),min()**   |   **O(1)**   |
| **add(k,v)**                 | **O(logn)*** |
| **update(loc,k,v)**          | **O(logn)*** |
| **remove(loc)**              | **O(logn)*** |
| **remove_min()**             | **O(logn)*** |

*动态数组摊销

## 第10章  映射、哈希表和跳跃表

10.1.1  映射的抽象数据类型

| 表10-1 映射的方法     |                                                              |
| :-------------------- | :----------------------------------------------------------: |
| **M[k]**              |                 返回在映射M中与键k相对应的值                 |
| **M[k]=v**            | 将映射 M 中的键 k 与值 v 建立关联，如果映射中的键 k 已经有对应的值存在，则替换该值。 |
| **del M[k]**          | 从映射 M 中删除键为 k 的元组，如果 M 中不存在这样的元组，则返回 KeyError 错误。 |
| **len(M)**            |                 返回在映射 M 中元组的数量。                  |
| **item(m)**           |      默认的对一个映射迭代生成其中所包含的所有键的序列。      |
| **K in M**            |           如果映射中包含键为 k 的元组则返回 True。           |
| **M.get(k,d=None)**   | 如果在映射中存在键 k 则返回 M[k]，否则返回缺省值 d，但不把键k加入映射集合。这种方法提供了一种避免返回 KeyError 风险的 M[k] 查询方法。 |
| **M.setdefault(k,d)** | 如果在映射 M 中存在键 k ，则返回 M[k]，如果键 k 不存在，则设置 M[k] = d，并返回这个值。（若有，则返回；若无，则创建） |
| **M.pop(k,d=None)**   | 从映射 M 中删除键为 k 的元组，并且返回与其对应的值 v 。如果键 k 不在映射中，则返回缺省值 d （或者如果参数 d 为 None，则抛出 KeyError） |
| **M.popitem()**       | 从映射M中随机删除一个键值对，并返回一个被删除的(k,v)键值对元组。如果映射M为空，则抛出keyerror。 |
| **M.clear()**         |            从映射中删除所有的 key-value 键值对。             |
| **M.keys()**          |          返回一个含有映射 M 中所有键的集合的视图。           |
| **M.values()**        |          返回一个含有映射 M 中所有值的集合的视图。           |
| **M.items()**         |         返回一个含有映射 M 中所有键值对元组的集合。          |
| **M.update(M2)**      |      对于 M2 中每一个 (k, v) 对进行赋值，设置 M[k]=v。       |
| **M == M2**           | 如果映射 M 和 M2 中所有的 key-value 键值对完全相同，则返回 True。 |
| **M != M2**           | 如果映射 M 和 M2 中包含有不同的 key-value 键值对，则返回 True。 |

10.1.4	map的层次结构

<img src="数据结构与算法（Python语言实现）.assets/image-20210316103148455.png" alt="image-20210316103148455" style="zoom: 67%;" />

MutableMapping这个来自于collection模块的抽象基类。

```python
from collections import MutableMapping
class MapBase(MutableMapping):
  """通过扩展MutableMapping抽象基类实现非公有类_Item，以满足各种映射应用."""

  #------------------------------- nested _Item class -------------------------------
  class _Item:
    """Lightweight composite to store key-value pairs as map items."""
    __slots__ = '_key', '_value'

    def __init__(self, k, v):
      self._key = k
      self._value = v

    def __eq__(self, other):               
      return self._key == other._key   # compare items based on their keys

    def __ne__(self, other):
      return not (self == other)       # opposite of __eq__

    def __lt__(self, other):               
      return self._key < other._key    # compare items based on their keys
```

### ==10.2	哈希表==

Python用哈希表实现dict类。

<img src="数据结构与算法（Python语言实现）.assets/image-20210316104718162.png" alt="image-20210316104718162" style="zoom:67%;" />

将这个框架扩展到更一般的映射设置有两个 **挑战** 。 **首先** ，如果在 N >> n 的情况下，长度为 N 的数组过长，空间占用将会非常稀疏。 **第二** ，我们一般不会要求一个映射的键必须是整数，于是有了哈希函数这种类似编码的功能。

在实践中可能有两个或者更多的不同键被映射到同一个索引上，因此，我们把表概念化为 **桶数组** 其中每个桶都管理一个元组集合，而这些元组则通过哈希函数发送到具体的索引。（为了节约空间，空桶可以用 None 代替。）

<img src="数据结构与算法（Python语言实现）.assets/image-20210316104844517.png" alt="image-20210316104844517" style="zoom:67%;" />

#### 10.2.1	哈希函数（address = H [key]）

> <u>哈希函数是一种映射关系，根据数据的关键词 key ，通过一定的函数关系，计算出该元素存储位置的函数。</u>

> **哈希函数 h  的目标就是把每个键 k 映射到 [0, N-1] 区间内的整数，其中 N 是哈希表的桶数组的容量。主要思想是使用哈希函数值 h(k) 作为哈希桶数组 A 内部的索引，而不用键 k 做索引。也就是说，我们在桶 A[h(k)] 中存储元组 (k, v) （产生冲突时，桶 A[h(k)]中可能会存储多个元组）***。

评价哈希函数 h(k) 最常见的方法由两部分组成：① **哈希码**，将一个键映射到一个整数；②**压缩函数** ，将哈希码映射到一个桶数组的索引（ 区间为 [0, N-1] 的一个整数）。

将哈希函数分为这样两部分的优势是： **哈希码计算部分独立于具体的哈希表的大小** 。这样就可以为每个对象开发一个通用的哈希码，并且可以用于任何大小的哈希表，只有压缩函数与表的大小（N）有关。

<img src="数据结构与算法（Python语言实现）.assets/image-20210316105329861.png" alt="image-20210316105329861" style="zoom:67%;" />![image-20210316110100124](数据结构与算法（Python语言实现）.assets/image-20210316110100124.png)

##### **几种常见的哈希函数（散列函数）构造方法**

- ==直接定址法== 
  - 取关键字或关键字的某个线性函数值为散列地址。
  - 即 H(key) = key 或 H(key) = a*key + b，其中a和b为常数。
  - 比如![这里写图片描述](https://img-blog.csdn.net/20161026171706654)
- ==除留余数法== 
  - 取关键字被某个不大于散列表长度 m 的数 p 求余，得到的作为散列地址。
  - 即 H(key) = key % p, p < m。 
  - 比如![这里写图片描述](https://img-blog.csdn.net/20161026171807417)
- ==数字分析法== 
  - 当关键字的位数大于地址的位数，对关键字的各位分布进行分析，选出分布均匀的任意几位作为散列地址。
  - 仅适用于所有关键字都已知的情况下，根据实际应用确定要选取的部分，尽量避免发生冲突。
  - 比如 ![这里写图片描述](https://img-blog.csdn.net/20161026172017748)
- ==平方取中法== 
  - 先计算出关键字值的平方，然后取平方值中间几位作为散列地址。
  - 随机分布的关键字，得到的散列地址也是随机分布的。
  - 比如 ![这里写图片描述](https://img-blog.csdn.net/20161026171618181)
- ==折叠法（叠加法）== 
  - 将关键字分为位数相同的几部分，然后取这几部分的叠加和（舍去进位）作为散列地址。
  - 用于关键字位数较多，并且关键字中每一位上数字分布大致均匀。 
  - 比如 ![这里写图片描述](https://img-blog.csdn.net/20161026173032699)
- ==随机数法== 
  - 选择一个随机函数，把关键字的随机函数值作为它的哈希值。
  - 通常当关键字的长度不等时用这种方法。 

构造哈希函数的方法很多，实际工作中要根据不同的情况选择合适的方法，总的原则是**尽可能少的产生冲突**。

通常考虑的因素有**关键字的长度**和**分布情况**、**哈希值的范围**等。如：当关键字是整数类型时就可以用除留余数法；如果关键字是小数类型，选择随机数法会比较好。

**10.2.2	哈希码（只有不可变数据类型（int,float,str,tuple,frozenset等）是可哈希的）**

> **哈希函数执行的第一步：**取出映射中的任意一个键 k ，并且计算得到一个整数作为键 k 的哈希码；这个整数不需要在 [0, N-1] 范围内，甚至可以是负数。我们希望分配给键的哈希码集合尽可能避免冲突。

- ==将位作为整数处理==

如果按位表示长于所需的哈希码长度，比如Python中的哈希码的长度是 32 位，而一个浮点数采用 64 位表示，此时可以将 64 位键的高阶 32 位和低阶 32 位采用一定的方式进行合并，生产一个32位的哈希码。
对象 x 的二进制表示可以视为 32 位整数的 n 元组$ (x_{0},x_{1},\cdots,x_{n-1})$则可以用 $\sum_{i=0}^{n-1}x_{i}$或者$x_{0} \oplus x_{1} \oplus \cdots \oplus x_{n-1}$来生成 x 的哈希码，这里符号 ⊕ 表示按位异或操作。

- ==多项式哈希码==

上面所描述的方法没有考虑元组中 $x_{i}$的顺序（“stop”和“tops”会产生相同的Unicode值，简单相加会发生冲突），为解决这一问题，我们可以选择一个非零常数 a 且 a≠1，并这样计算哈希码：
                                            $x_{0}a^{n-1} + x_{1}a^{n-2} + \cdots + x_{n-2}a + x_{n-1}$
这种哈希码被称为 **多项式哈希码** ，直观地说，一个多项式的哈希码通过乘以不同权值的方式来分散每一部分对哈希码结果的影响。

- ==循环移位哈希码==

一个多项式哈希码的变种，是用一定数量的位循环位移得到的部分和来替代乘以 a。例如，一个 32 位数 ***00111*** 101100101101010100010101000 的5位循环位移值，是取其最左边5位，并且将它们放置到数据的最右边，得到结果 101100101101010100010101000 ***00111***。

10.2.3	压缩函数

> **哈希函数处理的第二步：压缩函数**
> 通常，键 k 的哈希码不适合立即用于桶数组，因为整数哈希码可能是负的或可能超过桶数组的容量。因此我们需要吧整数映射到 [0, N-1] 区间上。一个很好的压缩函数会使给定的一组哈希码的冲突数达到最小。

**MAD方法**:$[(ai+b) \; mod \; p] \; mod \; N$

#### **10.2.4	哈希冲突的解决**

选用哈希函数计算哈希值时，可能不同的 key 会得到相同的结果，一个地址怎么存放多个数据呢？这就是冲突。

常用的主要有两种方法解决冲突：

==**1.分离链表**==（λ<0.9）

处理冲突的一个简单有效的方式是使每个桶 A[j] 存储其自身的二级容器，我们可以用一个很小的 list 来实现二级容器，这种解决冲突的方法称为 **分离链表**。

<img src="数据结构与算法（Python语言实现）.assets/image-20210316154742263.png" alt="image-20210316154742263" style="zoom: 67%;" />

> ​         一个用单独列表处理冲突的大小为13且存储10个以整数为键的元组的哈希表。h(k)=k mod 13

假设我们使用一个比较合适的哈希函数来在容量为 N 的哈希桶（其实就是长度为 N 的哈希桶数组）中索引 map 中的 n 个元组，则桶的理想大小为 n/N。**比值 λ=n/N 被称为哈希表的 \*负载因子\***，λ<0.9。

==**2.开放定址法**==

开放寻址模式是几种方法的统称，开放寻址需要负载因子总是最大不超过 1，并且元组 **直接存储在桶数组自身的单元中**。

用开放定址法解决冲突的做法是：

> 当冲突发生时，使用某种探测技术在散列表中形成一个探测序列。沿此序列逐个单元地查找，直到找到给定的关键字，或者碰到一个开放的地址（即该地址单元为空）为止（若要插入，在探查到开放的地址，则可将待插入的新结点存入该地址单元）。查找时探测到开放的地址则表明表中无待查的关键字，即查找失败。

简单的说：当冲突发生时，**使用某种探查(亦称探测)技术在散列表中寻找下一个空的散列地址，只要散列表足够大，空的散列地址总能找到**。

按照形成探查序列的方法不同，可将开放定址法区分为线性探查法、二次探查法、双重散列法等。

**a.线性探查法(若占用，则找空；若删除，先补上，再查询)**

​                                                             $hi=(h(key)+i) ％ m ，0 ≤ i ≤ m-1 $

基本思想是： 
探查时从地址 d 开始，首先探查 T[d]，然后依次探查 T[d+1]，…，直到 T[m-1]，此后又循环到 T[0]，T[1]，…，直到探查到 **有空余地址** 或者到 T[d-1]为止。

![image-20210316155911948](数据结构与算法（Python语言实现）.assets/image-20210316155911948.png)

> ​                                         用线性探测的方法向哈希表中插入整数键，h(k)=k mod 11

相应的，为了实现删除操作，我们不能把找到的元组简单地从插槽中移除，这样会破坏存储哈希函数值相同元素的空间的连续性。解决这一问题的典型方法是 **用一个带标记的特殊对象来替换被删除的对象（继续被占用）** 。这种方法会占用哈希表中的空间；同时，在查找键为 k 的元组时，搜索将跳过所有包含可用标记的单元；此外，可用标记单元是可插入新元组的有效位置。
缺点：可能造成重叠（尤其是哈希表中的一半以上的单元已经被占用时）。这种使用连续的哈希单元的运行方式会导致搜索速度大大降低。

**b.二次探查法**

​                                                              $hi=(h(key)+i*i) ％ m，0 ≤ i ≤ m-1 $

基本思想是： 
探查时从地址 d 开始，首先探查 T[d]，然后依次探查 T[d+1^2^] ,T[d+2^2^]，T[d+3^2^],…，等，直到探查到 **有空余地址** 或者到 T[d-1]为止。

缺点：无法探查到整个散列空间。

**c.双重散列法**

​                                                      $hi=(h(key)+i*h1(key)) ％ m，0 ≤ i ≤ m-1 $

基本思想是： 
探查时从地址 d 开始，首先探查 T[d]，然后依次探查 T[d+h1(d)], T[d + 2*h1(d)]，…，等。

$h1(k) = q - (k ％ q)$ 是一个常被选用的函数，对于素数 q 满足 q < N，且 N 也应该是素数。

该方法使用了两个散列函数 h(key) 和 h1(key)，故也称为双散列函数探查法。该方法是开放定址法中最好的方法之一。

**d.伪随机迭代法**

迭代地探测桶 $A[h(k)+f(i) ％ N] $，这里 f(i) 是一个基于伪随机数产生器的函数，它提供一个基于原始哈希码位的可重复的但是随机的、连续的地址探测序列。目前Python的字典就是使用这种方法。



| 表10-2 哈希表的效率 |      |                  |                    |
| :------------------ | :--- | :--------------- | :----------------- |
| 操作                | 列表 | 期望值（哈希表） | 最坏情况（哈希表） |
| _ _getitem_ _       | O(n) | O(1)             | O(n)               |
| _ _setitem_ _       | O(n) | O(1)             | O(n)               |
| _ _delitem_ _       | O(n) | O(1)             | O(n)               |
| _ _len_ _           | O(1) | O(1)             | O(1)               |
| _ _iter_ _          | O(n) | O(n)             | O(n)               |

10.2.6	哈希表的Python实现

- 一个哈希表实现的基类    HashMapBase

```
代码段10-4，见书278
```

- 分离链表    ChainHashMap

```
代码段10-5，见书279
```

- 开放寻址线性探测  ProbeHashMap

```
代码段10-6，见书280
```

**10.3	有序映射**

| 表10-3 有序映射               |                                                              |
| :---------------------------- | :----------------------------------------------------------: |
| **M.find_min()**              |   用最小键返回 (key, value) 对（或 None，如果映射为空）。    |
| **M.find_max()**              |   用最大键返回 (key, value) 对（或 None，如果映射为空）。    |
| **M.find_lt(k)**              |    用严格小于 k 的最大键返回(key, value) 对（或 None）。     |
| **M.find_le(k)**              |  用严格小于等于 k 的最大键返回(key, value) 对（或 None）。   |
| **M.find_gt(k)**              |    用严格大于 k 的最小键返回(key, value) 对（或 None）。     |
| **M.find_ge(k)**              |  用严格大于等于 k 的最小键返回(key, value) 对（或 None）。   |
| **M.find_range(start, stop)** | 用 start <= 键 < stop迭代遍历所有(key, value) 对。如果 start 指定为 None，从最小的键开始迭代；如果 stop 指定为 None，到最大键迭代结束。 |
| **iter(M)**                   |       根据自然顺序从最小到最大迭代遍历映射中的所有键。       |
| **reversed(M)**               | 根据逆序迭代映射中的所有键 r，这在 Python 中是用 _ _reversed_ _ 来实现的。 |

  10.3.1	排序检索表

<img src="数据结构与算法（Python语言实现）.assets/image-20210316174850652.png" alt="image-20210316174850652" style="zoom: 80%;" />

这种表示最主要的优势是，它支持使用 **二分查找算法**（运行时间为 O(log n)） 来做各种有效的操作。查找成功则能查找到目标或是临近目标的索引，查找失败也能确定一组索引有效地指定集合中的元素是小于还是大于目标。

- 上述有序映射的方法

```
代码段10-8，10-9,1-10，见书283
```

| 表10-3 有序映射的效率                                    |                                            |
| :------------------------------------------------------- | :----------------------------------------- |
| 操作                                                     | 运行时间                                   |
| **len(M)**                                               | O(1)                                       |
| **k in M**                                               | O(log n)                                   |
| **M[k]=v**                                               | 最坏情况下为 O(n) 如果存在 k 则为 O(log n) |
| **del M[k]**                                             | 最坏情况下为 O(n)                          |
| **M.find_min(), M.find_max()**                           | O(1)                                       |
| **M.find_lt(k), M.find_gt(k)M.find_le(k), M.find_ge(k)** | O(log n)                                   |
| **M.find_range(start ,stop)**                            | O(s + log n)，报告 s 项                    |
| **iter(M), reversed(M)**                                 | O(n)                                       |

**排序映射主要是用于含有查找较多但更新较少的情况。同时排序映射也支持模糊查找和范围查找的优势**

### **10.4	跳跃表**

排序数组可以通过二分查找以O(logn)时间做查询，但更新操作最坏情况下需要O(n)。为了优化，二分查找需要一个有效的手段来通过索引直接访问一个元素的序列。

一个映射 M 的跳跃表 S 包含一列表序列$ \lbrace S_{0},S_{1}, \cdots ,S_{h} \rbrace$。每一个列表 S_{i}Si 依照键的升序存储着 M 的一个元组子集，用两个标注为 $- \infty $和 $+\infty$ 的哨兵键追加元组，其中$- \infty $比每一个可能的插入 M 的键都要小，$+\infty$ 比每一个可能插入 M 的键都大。此外，列表 S 还要满足下面的条件：

- 列表 $S_{0}$ 包含映射 M 中的每一项（包含 $- \infty $ 和 $+\infty$）。
- 对于$i=1, \cdots ,h-1$，列表 $S_{i}$包含一个列表 $S_{i}-1$ 随机生成的元组的子集（还有$- \infty $和 $+\infty$ ）。
- 列表 $S_{h}$ 仅包含$- \infty $ 和 $+\infty$ 。

我们称 h 为列表 S 的高度。

<img src="数据结构与算法（Python语言实现）.assets/image-20210316213414158.png" alt="image-20210316213414158"  />

跳跃表链结构的本质是在垂直塔方向上对齐的双链表集合h，这样的链表本身也是双链表。（图中的线皆双链表）

![image-20210316222451531](数据结构与算法（Python语言实现）.assets/image-20210316222451531.png)

10.4.1	跳跃表中的查找和更新操作

所有的跳跃表查找和更新算法都依赖于一个简洁的 SkipSearch 方法，其需要一个键 k 并发现 S 列表中具有小于等于键 k (可能为 $-\infty$)的最大键的元组 p 的位置。

- 在跳跃表中==查找==

```
Algorithm SkipSearch(k):
	Iuput:A search key k
	output:Position p in the bottom list S0 with largest key such that key(p)≤k
	p=start
	while below(p)≠None do
		p=below(p)
		while k≥key(next(p)) do
			p=next(p)
	return p
```

<img src="数据结构与算法（Python语言实现）.assets/image-20210316220222389.png" alt="image-20210316220222389"  />

- 在跳跃表中==插入==

假设要插入一个键为 k 的元组。先在跳跃表中查找键大于 k 的最底层的位置，并在查找过程中标记需要进行链接的位置。在最底层插入新元组项后，通过 **随机方式** 决定新元组的垂直塔高度。

<img src="数据结构与算法（Python语言实现）.assets/image-20210316220608453.png" alt="image-20210316220608453" style="zoom:80%;" />

<img src="数据结构与算法（Python语言实现）.assets/image-20210316220428088.png" alt="image-20210316220428088"  />

- 在跳跃表中==移除==

为了执行映射操作 del M[k]，首先执行方法 SkipSearch(k)。如果位置 p 存储的条目与键 k 不同，则返回 KeyError。否则，移除 p 和 p 之上所有的位置。同时重新建立每一个移除位置与水平邻居之间的链接。

![image-20210316220645533](数据结构与算法（Python语言实现）.assets/image-20210316220645533.png)

10.4.2	性能分析

对于常量 c > 1，跳跃表 S 的高度大于$ c log n$ 的概率至多为 $1/n^{c-1}$
搜索时间： O(log n)
空间使用： O(n)

| 表10-4 跳跃表实现的排序表的性能                          |                               |
| :------------------------------------------------------- | :---------------------------- |
| 操作                                                     | 运行时间                      |
| **len(M)**                                               | O(1)                          |
| **k in M**                                               | 期望为O(log n)                |
| **M[k]=v**                                               | 期望为O(log n)                |
| **del M[k]**                                             | 期望为O(log n)                |
| **M.find_min(), M.find_max()**                           | O(1)                          |
| **M.find_lt(k), M.find_gt(k)M.find_le(k), M.find_ge(k)** | 期望为O(log n)                |
| **M.find_range(start ,stop)**                            | 期望为O(s + log n)，报告 s 项 |
| **iter(M), reversed(M)**                                 | O(n)                          |

### 10.5	集合、多集和多映射

- **集合(set)** 是无序元素的一个聚集，这些==元素不重复并且通常支持高效的成员检测==。从本质上说，集合中的元素像是映射中的键，但是它没有任何的附加值。
- **多集(multiset)** (也称为包(bag))是一个==允许有重复元素的类集合(set-like)容器==。
- **多映射(multimap)** 与传统的映射类似，在映射中它将键和值联系起来。然而，在==多映射中多个值可以映射到同一个键上==。

10.5.1 集合的抽象数据类型

| 表10-5 集合(set)抽象数据类型 |                                                              |
| :--------------------------- | :----------------------------------------------------------- |
| **S.add(e)**                 | 向集合中添加元素 e，如果集合中已经包含元素 e，则行为无效。   |
| **S.discard(e)**             | 如果集合中包含元素 e，则从集合中删除该元素。如果集合中不包含元素 e，则行为无效。 |
| **e in S**                   | 如果集合中包含元素 e，则返回 True，该行为是通过特定的方法 _ _contains_ _ 来实现的。 |
| **len(S)**                   | 返回集合 S 中的元素个数。                                    |
| **iter(S)**                  | 生成集合中所有元素的迭代。                                   |
| **S.remove(e)**              | 将元素e从集合中删除。                                        |
| **S.pop()**                  | 从集合中删除并返回一个任意元素                               |
| **S.clear()**                | 删除集合中的所有元素                                         |
| **S.isdisjoint(T)**          | 如果集合S和集合T没有公共元素，返回True                       |

10.5.3 集合、多集和多映射的实现

> 集合：**一个集合是一个简单的映射** ，这个映射中没有相关联的值。
>
> 多集：一种实现多集的方法是使用映射，该映射的键是多集中的元素（互不相同的），而键所关联的值是这个元素在多集中出现的次数。
>
> 多映射：**Python 的标准库中没有多映射** ，一个常见的实现方法是使用一个标准映射，该映射与键相关联的值是一个本身存储任意数量的关联值的容器类。



## 第11章  搜索树

**搜索树** 是树型数据结构的一个重要用途。我们使用搜索树结构来实现 **==有序==映射**。

### 11.1  二叉搜索树==（中序遍历：左根右）==

**二叉搜索树** 是每个节点 p 存储一个键值对 (k,v) 的二叉树 T ，使得：

- 存储在 p 的左子树的键都小于 k
- 存储在 p 的右子树的键都大于 k

<img src="数据结构与算法（Python语言实现）.assets/image-20210317202147143.png" alt="image-20210317202147143" style="zoom: 80%;" />

| 表11-1 二叉搜索树方法 |                                                              |
| :-------------------- | :----------------------------------------------------------- |
| **first()**           | 返回一个包含最小键的节点，如果树为空，返回None               |
| **last()**            | 返回一个包含最大键的节点，如果树为空，返回None               |
| **before(p)**         | 返回比节点p的键小的所有节点中键最大的节点（中序遍历中在p之前最后一个被访问的节点），如果p是第一个节点，返回None |
| **after(p)**          | 返回比节点p的键大的所有节点中键最小的节点（中序遍历中在p之后第一个被访问的节点），如果p是第一个节点，返回None |

- ==搜索(__finditem_)==

> 二叉搜索算法：想象把二叉搜索树表示为决策树，在每个节点 p 的问题就是期望的键 k 是否小于、等于或大于存储在节点 p 的键，表示为 p.key()。如果“小于”，则继续搜索左子树。如果“等于”，则搜索成功终止。如果“大于”，则继续搜索右子树。最后，如果得到空的子树，就是没有搜索到。

![image-20210317205248758](数据结构与算法（Python语言实现）.assets/image-20210317205248758.png)

二叉搜索的递归调用：

```python
Algorithm TreeSearch(T, p, k):
    if k == p.key() then
        return p
    else if k < p.key() and T.left(p) is not None then
        return TreeSearch(T, T.left(p), k)
    else if k > p.key() and T.right(p) is not None then
        return TreeSearch(T, T.right(p), k)
    return p
```

设每个节点的搜索时间为 O(1)，则总搜索时间为 O(h)，h 是二叉搜索树 T 的高度。
在有序映射 ADT 中，搜索将作为实现 _ _getitem_ _，_ _setitem_ _和_ _delitem_ _方法的子程序。树的高度为 h 时，所有这些操作在最坏情况下的时间复杂度为 O(h)

<img src="数据结构与算法（Python语言实现）.assets/image-20210317210250940.png" alt="image-20210317210250940" style="zoom:80%;" />

> ​                           二叉搜索树的运行时间。从根节点开始的搜索路径就是三角形内的锯齿形线

- ==插入(__setitem_)==

首先搜索键为 k 的项（假设映射不为空）。如果找到，该节点将被重新赋值；否则，新的节点可以放置在搜索失败结束时得到的空子树的位置。

```python
Algorithm TreeInsert(T, k, v):
    Input:A search key k to be associated with value v
        
    p = TreeSearch(T, T.root(), k)
    if k == p.key() then
        Set p’s value to v
    else if k < p.key then
        add node with item (k,v) as left child of p
    else
        add node with item (k,v) as right child of p
```

![image-20210317212017765](数据结构与算法（Python语言实现）.assets/image-20210317212017765.png)

- ==删除(__delitem_)==

首先找到 T 中键等于 k 的节点的位置 p。如果搜索成功，则分以下两种情况：

- 如果 p 最多有一个孩子，删除位置 p 的节点并用其子节点替换它。
- 如果位置 p 有两个孩子，采用如下步骤：
  （1）通过公式 r = before(p) 定位严格小于 p 处键的所有节点中拥有最大键的节点所在的位置 r。
  （2）使用位置 r 的节点作为位置 p 的替代。
  （3）使用第一种方法从树中删除 r 节点。（因为 r 节点无右子树）

![image-20210317212833679](数据结构与算法（Python语言实现）.assets/image-20210317212833679.png)

> ​                                                                                 p节点只有一个子节点r

![image-20210317212918142](数据结构与算法（Python语言实现）.assets/image-20210317212918142.png)

> ​                                                                                 p节点有两个孩子

二叉搜索树的Python实现

```
代码段11-4,11-5,11-6,11-7,11-8,见书308
```

11.1.5 二叉搜索树的性能

| 表11-2 二叉搜索树最坏时间复杂度                         |          |
| ------------------------------------------------------- | -------- |
| 操作                                                    | 运行时间 |
| **k in T**                                              | O(h)     |
| **T[k], T[k] = v**                                      | O(h)     |
| **T.delete(p),del T[k]**                                | O(h)     |
| **T.find_position(k)**                                  | O(h)     |
| **T.first(),T.last(),T.find_min(),T.find_max()**        | O(h)     |
| **T.before(p),T.after(p)**                              | O(h)     |
| **T.find_lt(k),T.find_le(k),T.find_gt(k),T.find_ge(k)** | O(h)     |
| **T.find_range(start,stop)**                            | O(s + h) |
| **iter(T),reversed(T)**                                 | O(n)     |


通常来说，通过一系列随机的插入或删除操作生成的有 n 个键的二叉搜索树的期望复杂度是 O(log n)。

### **11.2  平衡搜索树**==（旋转，重新调整树并降低树的高度，同时保持树的属性不变）==

由于某些操作序列会生成高度与n成比例的不平衡树，该树的时间复杂度为O(n)。例如右图：<img src="数据结构与算法（Python语言实现）.assets/image-20210318155721340.png" alt="image-20210318155721340" style="zoom: 25%;" />

后续的3种数据结构（AVL树、伸展树和红黑树）用少量操作对标准二叉树进行扩展，以重新调整树并降低树的高度，因此能提供更强的性能保证。

平衡二叉搜索树的主要操作是 **旋转**。在旋转中，我们“旋转”大于其父亲节点的孩子节点：

<img src="数据结构与算法（Python语言实现）.assets/image-20210318162147646.png" alt="image-20210318162147646" style="zoom:80%;" />

Python实现（relink、rotate、restructure操作）

```python
#--------------------- nonpublic methods to support tree balancing ---------------------
def _relink(self, parent, child, make_left_child):
    """Relink parent node with child node (we allow child to be None)."""
    if make_left_child:                           # make it a left child
      parent._left = child
    else:                                         # make it a right child
      parent._right = child
    if child is not None:                         # make child point to parent
      child._parent = parent

def _rotate(self, p):
    """Rotate Position p above its parent.

    Switches between these configurations, depending on whether p==a or p==b.

          b                  a
         / \                /  \
        a  t2             t0   b
       / \                     / \
      t0  t1                  t1  t2

    Caller should ensure that p is not the root.
    """
    """Rotate Position p above its parent."""
    x = p._node
    y = x._parent                                 # we assume this exists
    z = y._parent                                 # grandparent (possibly None)
    if z is None:            
      self._root = x                              # x becomes root
      x._parent = None        
    else:
      self._relink(z, x, y == z._left)            # x becomes a direct child of z
    # now rotate x and y, including transfer of middle subtree
    if x == y._left:
      self._relink(y, x._right, True)             # x._right becomes left child of y
      self._relink(x, y, False)                   # y becomes right child of x
    else:
      self._relink(y, x._left, False)             # x._left becomes right child of y
      self._relink(x, y, True)                    # y becomes left child of x
        
Algorithm restructure(x):
    INPUT: 二叉搜索树 T 的一个位置 x ，x 的父节点为 y ，祖父节点为 z
    OUTPUT: trinode 重组后的二叉搜索树，包括位置 x，y 和 z
1：让 (a,b,c) 为位置 x,y 和 z 的从左到右（中序）列表，令 (T1,T2,T3,T4) 为 x,y 和 z 的 4 个根不为 x,y 或 z 的子树的从左到右（中序）列表。
2：用根为 b 的子树来替换根为 z 的子树。
3：让 a 为 b 的左孩子，让 T1 和 T2 分别为 a 的左右子树。
4：让 c 为 b 的右孩子，让 T3 和 T4 分别为 c 的左右子树。
def _restructure(self, x):
    """Perform a trinode restructure among Position x, its parent, and its grandparent.
	Return the Position that becomes root of the restructured subtree.
	Assumes the nodes are in one of the following configurations:

        z=a                 z=c           z=a               z=c  
       /  \                /  \          /  \              /  \  
      t0  y=b             y=b  t3       t0   y=c          y=a  t3 
         /  \            /  \               /  \         /  \     
        t1  x=c         x=a  t2            x=b  t3      t0   x=b    
           /  \        /  \               /  \              /  \    
          t2  t3      t0  t1             t1  t2            t1  t2   

    The subtree will be restructured so that the node with key b becomes its root.

              b
            /   \
          a       c
         / \     / \
        t0  t1  t2  t3

    Caller should ensure that x has a grandparent.
    """
    """Perform trinode restructure of Position x with parent/grandparent."""
    y = self.parent(x)
    z = self.parent(y)
    if (x == self.right(y)) == (y == self.right(z)):  # matching alignments
      self._rotate(y)                                 # single rotation (of y)
      return y                                        # y is new subtree root
    else:                                             # opposite alignments
      self._rotate(x)                                 # double rotation (of x)     
      self._rotate(x)
      return x                                        # x is new subtree root
```

在实践中，由旋转重建造成的树 T 的修改可以通过单个旋转或者双旋转来实现。在任何情况下，旋转重建都可以在 O(1) 时间内完成。

<img src="数据结构与算法（Python语言实现）.assets/image-20210318164830172.png" alt="image-20210318164830172"  />

![image-20210323205832037](数据结构与算法（Python语言实现）.assets/image-20210323205832037.png)

![image-20210323210057980](数据结构与算法（Python语言实现）.assets/image-20210323210057980.png)

### 11.3  AVL树==（维持对数的高度，h=log(n)，平衡因子）==

> AVL树的定义：任何满足高度平衡属性的二叉搜索树 T 被称为 AVL 树，且树维持对数的高度。
>
> 对于一棵树来说，它的**高度(height)**定义如下：**从根节点(root)开始到某一个叶子节点(leaf)的最长路径(path)上结点的个数**
>
> 高度平衡属性：`AVL树`中的任意一个结点, 其`平衡因子`的值只能为-1,0,1
>
> 高度平衡属性带来的结果：（1）AVL 子树也是 AVL 树；（2）AVL 树可以保持高度最小。

<img src="数据结构与算法（Python语言实现）.assets/image-20210318171323853.png" alt="image-20210318171323853" style="zoom: 80%;" />

==**平衡因子**==（**一个节点的左孩子的高度减去其右孩子的高度**）

**AVL 树最核心的思想就是计算每个节点的平衡因子**（**balance factor**），平衡因子的定义是**一个节点的左孩子的高度减去其右孩子的高度**。这里的**高度**（**height**）就是指从**一个节点出发到达最远叶子节点所经过的最长路径**。

![image-20210318175226550](数据结构与算法（Python语言实现）.assets/image-20210318175226550.png)



给定一颗二叉搜索树，如果一个位置的子树高度之差的绝对值最多为 1，我们就说这个位置是 **平衡的**，否则这个位置就是 **不平衡的**。因此，AVL 树的高度平衡属性相当于 **每个位置都是平衡的**。

- ==插入==

AVL 树的插入操作也跟二叉搜索树一样，**先找到插入的位置**，即通过搜索操作找到插入位点，然后**创建一个新节点**，最后**父节点指向该新节点**。但由于 AVL 树是一棵自平衡的树，所以**每插入一个节点都会更新搜索过程中所经过节点的高度**，如发现有节点的**高度的绝对值大于等于 2**，则**采取相应的旋转操作使之保持平衡**。

![image-20210318224553122](数据结构与算法（Python语言实现）.assets/image-20210318224553122.png)

![image-20210318174606582](数据结构与算法（Python语言实现）.assets/image-20210318174606582.png)

- ==删除==

如果 p 代表在树 T 中删除节点的父节点，最多可能有一个不平衡的节点在 p 到根节点之间的路径上。与插入一样，使用 trinode 重组恢复树 T 的平衡。

![image-20210318231632106](数据结构与算法（Python语言实现）.assets/image-20210318231632106.png)

- 性能

| 表11-3 AVL树最坏时间复杂度                              |             |
| ------------------------------------------------------- | ----------- |
| 操作                                                    | 运行时间    |
| **k in T**                                              | O(log n)    |
| **T[k], T[k] = v**                                      | O(log n)    |
| **T.delete(p),del T[k]**                                | O(log n)    |
| **T.find_position(k)**                                  | O(log n)    |
| **T.first(),T.last(),T.find_min(),T.find_max()**        | O(log n)    |
| **T.before(p),T.after(p)**                              | O(log n)    |
| **T.find_lt(k),T.find_le(k),T.find_gt(k),T.find_ge(k)** | O(log n)    |
| **T.find_range(start,stop)**                            | O(s + logn) |
| **iter(T),reversed(T)**                                 | O(n)        |

### 11.4  伸展树（将某位置p移动到根节点，类似于二叉搜索树的一个附加功能）

伸展树的效率取决于某一位置移动到根的操作（称为 **伸展** ），==每次在插入、删除或者搜索都要 **从最底层的位置 p 开始** 。==直观上，伸展树会使得被频繁访问的元素更快接近于根，从而减少典型的搜索时间。伸展树保障了插入、删除、搜索操作具有 **对数运行时间** 。

11.4.1 伸展

已知二叉搜索树 T 的一个节点 x，通过一系列的重组将 x 移动到 T 的根来对 x 进行 **伸展**。将 x 向上移动的特定操作取决于 x 、其父节点 y 和 x 的祖先节点 z（如果存在的话）的相对位置。考虑以下三种情况：

 <img src="数据结构与算法（Python语言实现）.assets/image-20210323151841876.png" alt="image-20210323151841876" style="zoom: 80%;" /><img src="数据结构与算法（Python语言实现）.assets/image-20210323151902568.png" alt="image-20210323151902568" style="zoom: 80%;" />

<img src="数据结构与算法（Python语言实现）.assets/image-20210323151938169.png" alt="image-20210323151938169" style="zoom:80%;" />

11.4.2 伸展规则（要对一节点p进行操作，则对p进行伸展，即从最后一个移位到根节点）

- ==搜索==：搜索键 k 时，如果在位置 p 处找到 k ，则伸展 p；否则，在搜索失败的位置伸展叶子节点。

  > 上述的zig-zig型、zig-zag型、zig型

- ==插入==：当插入键 k 时，我们将伸展新插入的内部节点 k。

  ![image-20210323152949671](数据结构与算法（Python语言实现）.assets/image-20210323152949671.png)

- ==删除==：当删除键 k （被删除节点k）时，在位置 p 进行伸展，其中 p 是被移除节点（最底层最后一个节点，数组中k的前一个元素的节点）的父节点。

<img src="数据结构与算法（Python语言实现）.assets/image-20210323153033324.png" alt="image-20210323153033324"  />

11.4.3 python实现

```Python
见书p324，代码段11-14
```

> 伸展树的优势：（1）仅使用一棵不需要存储每个节点的附加平衡信息的简单二叉树就能实现这样的性能。（2）实现简单，仅需要对标准二叉树进行简单的改编。

### 11.5 （2,4）树（多个孩子节点的有序搜索树）

11.5.1 **多路搜索树**（一棵有以下属性的有序树 T）

令 w 为有序树的一个节点，如果 w 有 d 个孩子，则称 w 是 d-node。

- T 的每个内部节点至少有两个孩子。也就是说每个内部节点是一个 d-node，其中 d >= 2。
- T 的每个内部 d-node w（其孩子为 c1,…,cd ）按顺序存储 d-1 个键-值对 (k1, v1),…,(kd-1,vd-1)，k1 <= … <= kd-1。
- 通常定义 k0 = -∞ 和 kd = +∞。每个条目 (k,v) 存储在一个以 ci 为根的 w 的子树的一个节点上，其中 i=1, …, d, ki-1 <= k <= ki。

根据上述定义， **多路搜索的外部（叶子）节点不存储任何数据并且仅仅作为“占位符”**。这些外部节点可以有效地以 None 引用表示。

>**一棵有 n 个键值对的多路搜索树有 n+1 个外部节点**

![image-20210323163457111](数据结构与算法（Python语言实现）.assets/image-20210323163457111.png)

**多路树搜索**（在 T 中从根节点开始跟踪路径执行搜索）

在搜索 d-node 节点 w 时，比较键 k 和存储在 w 上的键$k_{1}$, …, $k_{d-1}$。如果 k =$k_{i}$，搜索成功；否则，继续搜索 w 的孩子 $c_{i}$，使得$ k_{i-1}$ < k <$k_{i}$（通常定义 $k_{0}$= -∞ 和$k_{d}$ = + ∞ ）。如果到达外部节点，搜索不成功并终止。



![img](数据结构与算法（Python语言实现）.assets/20200531113324932.png)

#### **11.5.2 （2,4）树**

>**存储 n 个节点的 (2, 4) 树的高度为 O(log n)** 

- 大小属性：每个内部节点最多有 4 个孩子。
- 深度属性：所有外部节点具有相同的深度。

<img src="数据结构与算法（Python语言实现）.assets/image-20210323164524430.png" alt="image-20210323164524430" style="zoom: 50%;" />

- ==插入==

插入一个键为 k 的新节点 (k, v) 到 (2, 4) 树 T 中，首先对键 k 执行搜索。假设 T 中没有键为 k 的节点，这个搜索非正常终止于外部节点 z 中。令 w 为 z 的父节点。我们在节点 w 上插入新的项，并且在 z 的左边对 w 添加一个新的孩子节点（外部节点） y（因为要满足一棵n个节点的多路搜索树有n+1个外部节点这个命题）。
> 上述插入方法维持了深度属性，但可能违反大小属性。解决方法：
>
> 1. 用 w’ 和 w" 来代替 w，其中：
>    - **w’ 是存储 k1 和 k2 的 3-node （其孩子节点为 c1,c2,c3）**
>    - **w" 是存储 k4 的 2-node（其孩子节点为 c4,c5）**
> 2. 如果 w 是 T 的根节点，创建一个新的根节点 u，让 u 为 w 的父节点。
> 3. 插入键值 k3 到 u 中，并使得 w" 和 w’ 成为 u 的孩子节点。如果 w 是 u 的第 i 个孩子，那么 w’ 和 w" 将分别为 u 的第 i 个和第 i+1 个孩子节点。

![image-20210323165938406](数据结构与算法（Python语言实现）.assets/image-20210323165938406.png)

- ==删除==

**要删除的项存储在无外部孩子的节点 z：（也是找删除键k的前一个键，先替换，发生下溢，再合并）**
假设要删除的键为 k 的项存储在节点 z 的第 i 个项 (ki, vi)，则选出如下节点 w 中的项并与 (ki, vi) 交换：
（1）w 在以 z 的第 i 个孩子为根的子树上； w 是最右边的子树的内部节点；w 的所有孩子节点都是外部节点。
（2）用 w 的最后一个节点交换节点 z 的 (ki, vi)。

**要删除的项存储在只有外部孩子的节点 w：（先删除，发生下溢，再转移/融合）**
（1）如果删除项后不怕破坏大小属性，此时可直接删除项并删除 w 的第 i 个外部节点。（见下图中 g,h)
（2）如果删除项后破坏大小属性，这种情况称为在节点 w 下溢。为了修复下溢，我们检查 w 的兄弟节点是否是一个 3-node 或 4-node。如果发现这样一个兄弟 s，就进行 **转移** 操作，也就是将 s 的一个孩子移到 w 上，将 s 的一个键移到 w 和 s 的父节点 u 上，将 u 的一个键移动到 w （见下图中 b,c）。如果 w 只有一个兄弟或者兄弟都是 2-node ，就进行 **融合** 操作，合并 w 及其一个兄弟，创建一个新节点 w’ 并将 w 的父节点 u 的键移动到 w’。（见下图中 e,f)

![在这里插入图片描述](数据结构与算法（Python语言实现）.assets/20200531113503803.png)<img src="数据结构与算法（Python语言实现）.assets/20200531113503262.png" alt="在这里插入图片描述" style="zoom: 80%;" />

- 性能

有 n 个键-值对的 (2, 4) 树的时间复杂度的分析基于以下几点：

- 存储 n 个节点的 (2,4) 树的高度是 O(log n)。
- 分裂、交换或合并操作需要 O(1) 时间。
- 搜索、插入或删除一个节点需要访问 O(log n) 个节点。

### **11.6 红黑树**

> 红黑树在一次更新之后，使用 O(1) 次结构变化来保持平衡。

#### **11.6.1 红黑树**

> **存储 n 个节点的红黑树的高度为 O(log n)** ，**因为可以和（2,4）树相互转换**

- 根属性：根节点是黑色的。
- 红色属性：红色节点（如果有的话）的子节点是黑色的。
- 深度属性：具有零个或一个子节点的所有节点都具有相同的 **黑色深度** （被定义为黑色祖先节点的数量，且一个节点是它自己的祖先）

<img src="数据结构与算法（Python语言实现）.assets/image-20210323195559966.png" alt="image-20210323195559966" style="zoom:80%;" />

红黑树和 (2,4) 树之间存在着一个对应关系，它们之间可以相互转换：

![image-20210323200842720](数据结构与算法（Python语言实现）.assets/image-20210323200842720.png)

- ==搜索==

与二叉搜索树算法相同

- ==插入==

首先在 T 中搜索 k，直到达到一个空子树，然后在这个位置插入一个新的叶子节点 x，存储项。如果 x 是根节点，将其设为黑色，否则将其设为红色。

上述操作可能违反红色属性，即 x 和 x 的父节点 y 都是红色的，我们将这种情况称为**双红色**。
为了解决双红色问题，考虑以下两种情况：

**情况1： y 的兄弟姐妹为黑色（或无）——重构**

此时进行 T 的 trinode 重组，通过11.2节restructure(x)函数实现。

>重构后，将b着色为黑色，a,c着色为红色。

![image-20210323202107996](数据结构与算法（Python语言实现）.assets/image-20210323202107996.png)

可以注意到重组后任何路径中的黑色节点数不改变，因此树的**黑色深度不受影响**。

**情况2：** **y 的兄弟姐妹是红色的——重新着色**

此时双红色表示在相应的 (2,4) 树中溢出（图a）为解决这个问题，进行一个相当于 **分裂** 的操作，即重新着色。

> **重新着色**：将y和s着色为黑色，其父节点z着色为红色（除非z是根节点必须是黑色）

![image-20210323202934613](数据结构与算法（Python语言实现）.assets/image-20210323202934613.png)

一个具体的插入例子

<img src="数据结构与算法（Python语言实现）.assets/image-20210323212045657.png" alt="image-20210323212045657"  />

- ==删除==（这部分看书p338）

从红黑树 T 中删除键为 k 的项和二叉搜索树的删除过程相似。在结构上，这种处理结果导致删除至多有一个孩子的节点（要么是最初包含 k 的节点要么是k的前面那个键），并提升其剩余的节点（如果有的话）。

![img](数据结构与算法（Python语言实现）.assets/2020053111365026.png)

如果删除节点是红色的，这种结构性变化不会影响树中任何路径的黑色深度，也不会违反红色属性，所以结果树仍然是有效的红黑树。在相应的 (2,4) 树中，这表示 3-node 或 4-node 的萎缩。如果删除的节点是黑色的，那么它要么没有孩子要么有一个子节点，这个子节点是一个红色的叶子节点（因为删除的节点的空子树黑色高度为 0，由深度属性和红色属性，此子节点必须是红色的叶子节点）。在后一种情况下，将除去的节点代表一个相应的 3-node 的黑色部分，我们通过重新将提升的孩子着色为黑色来恢复红黑属性：

![img](数据结构与算法（Python语言实现）.assets/20200531113708631.png)

更为复杂的情况是一个（非根）黑色叶节点被删除。考虑一个更一般的设置，用一个已知有两个子树的 z 节点、T_heavy 和 T_light，T_light （如果有）在删除前的根节点是黑色，同时 T_heavy 的黑色深度恰好比 T_light 高 1，如下图所示。在一个除去黑色叶子的情况下，z 是该叶子的父亲，T_light 是删除之后仍然存在的空子树。用 y 表示 T_heavy 的根（y 一定存在，因为 T_heavy 的黑色深度至少为 1）

<img src="数据结构与算法（Python语言实现）.assets/20200531113730401.png" alt="img" style="zoom: 80%;" />

为了弥补黑色深度不足，考虑以下三种情况：

**情况1：节点 y 是黑色的，同时有一个红色的孩子节点 x——重构**

> 对于该情况执行 trinode 重组。这种情况对应于 (2,4) 树 T’ 中在 z 的两个子节点之间的转换操作。

![img](数据结构与算法（Python语言实现）.assets/20200531113751924.png)

**情况2：节点 y 是黑色，并且 y 的两个子节点是黑色（或无）——重新着色** 

> 对于该情况执行 **重新着色** 。这种情况相当于在 (2,4) 树中进行一个融合操作。

![img](数据结构与算法（Python语言实现）.assets/202005311138079.png)

**情况3：节点 y 是红色的——旋转** 

因为 y 是红色的，同时 T_heavy 有至少为 1 的黑色深度，所以 z 必须是黑色的，且 y 的两个子树必须每一个都有一个黑色的根，并且黑色的深度等于 T_heavy 的深度。

> 这种情况下，我们把 y 和 z 进行旋转，然后重新将 y 着为黑色，将 z 着为红色。

这并不能立即解决不足，因此还需要继续采用情况 1 或者情况 2 ，且一定能在下一次终止（对应情况2图a）。

![img](数据结构与算法（Python语言实现）.assets/202005311138250.png)

一个具体的删除例子

![image-20210323225312145](数据结构与算法（Python语言实现）.assets/image-20210323225312145.png)

- 性能

红黑树的渐进性能与 AVL 树或 (2,4) 树的渐进性能相同，对于大多数操作保证了log(n)时间界限。红黑树的主要优点在于插入或删除只需要常数步的调整操作（这是相对于 AVL 树和 (2,4) 树）

> 在一棵存储 n 个项目的红黑树中**插入**一个项可在 O(log n) 的时间内完成，并且需要 O(log n) 的重新着色且至多需要一次的 trinode 重组；
>
> 在一棵存储 n 个项目的红黑树中**删除**一个项可在 O(log n) 的时间内完成，并且需要 O(log n) 的重新着色且最多需要两次调整操作。

11. 6.2 python实现

```
见书p341，代码段11-15
```

## 第12章  排序与选择

![image-20210327162942115](数据结构与算法（Python语言实现）.assets/image-20210327162942115.png)

### 12.2 归并排序——O(nlogn)

#### 12.2.1 分治法

分治法设计模式步骤：
1）分解：如果输入值的规格小于确定的数量阈值（就0,1,2个元素数目），我们就通过使用直截了当的方法来解决这些问题并返回所获得的答案。否则，我们把输入值分解为两个或者更多的互斥子集。
2）解决子问题：递归地解决这些与子集相关的子问题。
3）合并：整理这些子问题的解，然后把他们合并成一个整体用以解决最开始的问题。

![image-20210324172531576](数据结构与算法（Python语言实现）.assets/image-20210324172531576.png)

> 命题12-1：在大小为n是序列上执行归并算法，与其相关联的归并排序树的高度为$\lceil logn \rceil$

12.2.2 Python实现

- 基于**数组**的归并排序

```python
def merge(S1, S2, S):
  """将两个已排序的序列S1和S2合并，并将输出复制到序列S中."""
  i = j = 0
  while i + j < len(S):
    "每次进入while循环时复制一个元素，有条件决定下一个元素将会取自S1或S2中哪一个"
    if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
      S[i+j] = S1[i]      # copy ith element of S1 as next item of S
      i += 1
    else:
      S[i+j] = S2[j]      # copy jth element of S2 as next item of S
      j += 1
```

- 基于**链表(队列)**的归并排序

  ```python
  from ..ch07.linked_queue import LinkedQueue
  
  def merge(S1, S2, S):
    """Merge two sorted queue instances S1 and S2 into empty queue S."""
    while not S1.is_empty() and not S2.is_empty():
      if S1.first() < S2.first():
        S.enqueue(S1.dequeue())
      else:
        S.enqueue(S2.dequeue())
    while not S1.is_empty():            # move remaining elements of S1 to S
      S.enqueue(S1.dequeue())
    while not S2.is_empty():            # move remaining elements of S2 to S
      S.enqueue(S2.dequeue())
  
  def merge_sort(S):
    """Sort the elements of queue S using the merge-sort algorithm."""
    n = len(S)
    if n < 2:
      return                            # list is already sorted
    # divide
    S1 = LinkedQueue()                  # or any other queue implementation
    S2 = LinkedQueue()
  ##############分解#################
    while len(S1) < n // 2:             # move the first n//2 elements to S1
      S1.enqueue(S.dequeue())
    while not S.is_empty():             # move the rest to S2
      S2.enqueue(S.dequeue())
    # conquer (with recursion)
  #########分解子集，直到不可分##########
    merge_sort(S1)                      # sort first half
    merge_sort(S2)                      # sort second half
    # merge results
  ###############合并#################
    merge(S1, S2, S)                    # merge sorted halves back into S
  ```

- 基于数组的**非递归**的归并排序（执行自底向上的归并排序，即对整个归并排序树自底向上逐层执行合并）

  ```python
  import math
  
  def merge(src, result, start, inc):
    """Merge src[start:start+inc] and src[start+inc:start+2*inc] into result."""
    end1 = start+inc                        # boundary for run 1
    end2 = min(start+2*inc, len(src))       # boundary for run 2
    x, y, z = start, start+inc, start       # index into run 1, run 2, result
    while x < end1 and y < end2:
      if src[x] < src[y]:
        result[z] = src[x]
        x += 1
      else:
        result[z] = src[y]
        y += 1
      z += 1                                # increment z to reflect new result
    if x < end1:
      result[z:end2] = src[x:end1]          # copy remainder of run 1 to output
    elif y < end2:
      result[z:end2] = src[y:end2]          # copy remainder of run 2 to output
  
  def merge_sort(S):
    """Sort the elements of Python list S using the merge-sort algorithm."""
    n = len(S)
    logn = math.ceil(math.log(n,2))
    src, dest = S, [None] * n               # make temporary storage for dest
    for i in (2**k for k in range(logn)):   # pass i creates all runs of length 2i
      for j in range(0, n, 2*i):            # each pass merges two length i runs
        merge(src, dest, j, i)
      src, dest = dest, src                 # reverse roles of lists
    if S is not src:
      S[0:n] = src[0:n]                     # additional copy to get results to S
  ```

- 基于链表的**非递归**的归并排序

  ```python
  练习C-12.29
  链接：https://leetcode-cn.com/problems/sort-list/solution/sort-list-gui-bing-pai-xu-lian-biao-by-jyd/
  ```

12.2.3 归并排序的运行时间—O(nlogn)

<img src="数据结构与算法（Python语言实现）.assets/image-20210324213811421.png" alt="image-20210324213811421" style="zoom:80%;" />

> 命题12-2：一个大小为n的序列S，其两个元素可以在O(1)的时间内完成比较，归并排序时间为O(nlogn)

### 12.3	快速排序——O(nlogn)

> 主要思想：==应用分治法把序列S分解为子序列，递归地排序每个子序列，然后通过简单串联的方式合并这些已排序的子序列。==

快速排序的主要步骤：                                                                快速排序图解：

<img src="数据结构与算法（Python语言实现）.assets/image-20210327153617707.png" alt="image-20210327153617707" style="zoom: 67%;" />                                                           <img src="数据结构与算法（Python语言实现）.assets/image-20210327161541022.png" alt="image-20210327161541022" style="zoom: 80%;" />
1）分解：如果S有至少2个元素（0,1个元素无需排序），从S选择一个特定元素x（一般是S中最后一个元素），称为基准值。从S中移除所有元素，并放入3个序列中：

- L存储S中小于x的元素

- E存储S中等于x的元素

- G存储S中大于x的元素

2）解决子问题：递归地排序序列L和G。
3）合并：把S中的元素按照先插入L中的元素、然后插入E中的元素、最后插入G中的元素的顺序放回。

![image-20210327154935790](数据结构与算法（Python语言实现）.assets/image-20210327154935790.png)

#### 12.3.1	快速排序的Python实现(基于队列)

- 基于队列的快速排序

```python
def quick_sort(S):
  """Sort the elements of queue S using the quick-sort algorithm."""
  n = len(S)
  if n < 2:
    return                            # list is already sorted
  ##############分解#################
  p = S.first()                       # using first as arbitrary pivot
  L = LinkedQueue()
  E = LinkedQueue()
  G = LinkedQueue()
  while not S.is_empty():             # divide S into L, E, and G
    if S.first() < p:
      L.enqueue(S.dequeue())
    elif p < S.first():
      G.enqueue(S.dequeue())
    else:                             # S.first() must equal pivot
      E.enqueue(S.dequeue())
##############递归排序L和G#############
  quick_sort(L)                       # sort elements less than p
  quick_sort(G)                       # sort elements greater than p
##################合并################
  while not L.is_empty():
    S.enqueue(L.dequeue())
  while not E.is_empty():
    S.enqueue(E.dequeue())
  while not G.is_empty():
    S.enqueue(G.dequeue())
```

12.3.2 快速排序的运行时间—O(nlogn)

![image-20210327161241388](数据结构与算法（Python语言实现）.assets/image-20210327161241388.png)

#### 12.3.3	随机快速排序——O(nlogn)

> 选择S中一个随机元素作为基准值代替S的第一个或最后一个元素作为基准值（因为在初始序列S有序的情况下，快速排序是最坏情况，时间复杂度为O($n^2$)），其余部分保持不变。

因为快速排序方法划分步骤的目的是把序列S分解得足够平衡，让基准值尽量接近元素集合的“中间”，会使快速排序的运行时间达到O(nlogn)。

基准值的选择：==常用技巧是取数组的头部、中部和尾部的值的中位数，这样可以避免O($n^2$)的最坏情况。==

#### 12.3.4 快速排序的额外优化（基于数组）

> In-place：对于一个算法，除了原始所需的内存之外，仅仅只使用少量内存，称为就地(In-place)算法。

- 基于数组的快速排序

```python
def inplace_quick_sort(S, a, b):
  """使用快速排序算法对列表从S [a]到S [b]进行排序."""
  if a >= b: return                                      # range is trivially sorted
  pivot = S[b]                                           # last element of range is pivot
  left = a                                               # will scan rightward
  right = b-1                                            # will scan leftward
  while left <= right:
    # 扫描直到达到≥pivot（或right）的值
    while left <= right and S[left] < pivot:
      left += 1
    # 扫描直到达到≤pivot（或left）的值
    while left <= right and pivot < S[right]:
      right -= 1
    if left <= right:                                    # scans did not strictly cross
      S[left], S[right] = S[right], S[left]              # swap values
      left, right = left + 1, right - 1                  # shrink range

  # put pivot into its final place (currently marked by left index)
  S[left], S[b] = S[b], S[left]
  # make recursive calls
  inplace_quick_sort(S, a, left - 1)
  inplace_quick_sort(S, left + 1, b)
```

![image-20210327171528869](数据结构与算法（Python语言实现）.assets/image-20210327171528869.png)

### 12.4	再论排序：算法视角

12.4.1 排序下界

==**任何基于比较的排序算法对有n个元素的序列排序所花费的时间都是Ω(nlogn)的运行时间下界（Ω=不低于）。**==

<img src="数据结构与算法（Python语言实现）.assets/image-20210327180113308.png" alt="image-20210327180113308" style="zoom:80%;" />

12.4.2 线性时间排序：桶排序和基数排序

- **桶排序 (运行时间O(n+N)、运行空间O(n+N))**

  使用键值作为插入桶数组B的索引，数组B具有从0到N-1的索引。具有关键字k的项被放置在桶B[k]中，这个桶本身就是序列（包含键值为k的条目）。在将输入序列S的每个条目插入它的桶中之后，可以通过按序枚举B[0]，B[1]，...，B[N-1]把这些项放回S。

```python
Algorithm bucketSort(S):
Input: 整数键在[0，N−1]范围内的条目的序列S输出：按键的降序排列的序列S
令B为N个序列的数组，每个序列最初都是空的
for each entry e in S do
  k = the key of e
  remove e from S
  insert e at the end of bucket B[k] 
for i = 0 to N−1 do
  for each entry e in B[i] do
      remove e from B[i]
      insert e at the end of S
```

![image-20210327181211039](数据结构与算法（Python语言实现）.assets/image-20210327181211039.png)

**桶排序特性：**即使许多不同的元素有相同的键值，也能得到正确的结果。当N<<n时，高效；当N>>n时，低效。

- **基数排序 (运行时间O(n*N)、运行空间O(n+N))**

  原理是将整数按位数切割成不同的数字，然后按每个位数分别比较。
  
  ```python
  Algorithm binaryRadixSort(S)
  	Input sequence S of b-bit integers
      Output sequence S sorted replace each element x of S with the item (0, x)
  	for i  0 to b - 1
  		replace the key k of each item (k, x) of S	with bit xi of x
  		bucketSort(S, 2)
  ```
  
  

![image-20210330164241296](数据结构与算法（Python语言实现）.assets/image-20210330164241296.png)

基数排序可以应用于任何键都可以被看作以字典序排序得到的小规模排序的情形。例如我们可以将其应用于对长度适中的字符串进行排序，要求字符串中每个单独的字符可以表示为一个整数值（不同长度的字符串可以补0处理）

**12.6	Python内置排序函数**

①list类的sort方法：list.sort()

```python
a=['red','blue','green']
a.sort()
>>>['blue', 'green', 'red']
```

②sorted内置函数

```python
a=['red','blue','green']
sorted(a)
>>>['blue', 'green', 'red']
sorted('green')
>>>['e','e','g','n','r']
```

自由定义键函数排序

```python
a=['green','blue','red']
a.sort(key=len)
>>>['red','blue','green'] #按字符串长度排序
sorted(a,key=len)
>>>['red','blue','green']
sorted(a,key=len,reverse=True)
>>>['green','blue','red'] #反向
```

**12.7 选择**

选择问题：即从未排序的n个可比较元素中选择第k个最小的元素。

### ==12.7 随机快速选择（给定一个无序的数组，寻找第K大的元素）==

类似随机快速排序算法。算法流程：

![image-20210330175751976](数据结构与算法（Python语言实现）.assets/image-20210330175751976.png)



![image-20210330175815749](数据结构与算法（Python语言实现）.assets/image-20210330175815749.png)

![image-20210330175842757](数据结构与算法（Python语言实现）.assets/image-20210330175842757.png)

![image-20210330175856105](数据结构与算法（Python语言实现）.assets/image-20210330175856105.png)

- Python实现

```python
import random
def quick_select(S, k):
  """Return the kth smallest element of list S, for k from 1 to len(S)."""
  if len(S) == 1:
    return S[0]
  pivot = random.choice(S)             # pick random pivot element from S
  L = [x for x in S if x < pivot]      # elements less than pivot
  E = [x for x in S if x == pivot]     # elements equal to pivot
  G = [x for x in S if pivot < x]      # elements greater than pivot
  if k <= len(L):
    return quick_select(L, k)          # kth smallest lies in L
  elif k <= len(L) + len(E):
    return pivot                       # kth smallest equal to pivot
  else:
    j = k - len(L) - len(E)            # new selection parameter
    return quick_select(G, j)          # kth smallest is jth in G
```

- 时间分析

  大小为n的序列S的随机快速选择的预期运行时间是O(n)，假设S的两个元素可以在O(1)的时间内进行比较。

## 第13章  文本处理

### 13.2 模式匹配算法

经典模式匹配问题中，给出长度为n的<u>文本</u>字符串**T**和长度为m的<u>模式</u>字符串**P**，希望明确是否**P**是**T**的一个子串。解决方法一般有：**P** in **T**、**T**.find(**P**)、**T**.index(**P**)、**T**.count(**P**)、**T**.paritition(**P**)、**T**.split(**P**)、**T**.repalce(**P**,**Q**)

|              | 运行时间 | 描述                                                       |
| ------------ | -------- | ---------------------------------------------------------- |
| 朴素暴力算法 | O(nm)    | 一个个从头开始比，比完一次移动一步                         |
| BM算法       | O(nm)    | “坏字符规则”、“好后缀规则”，每次后移两个规则之中的最大值   |
| KMP算法      | O(n+m)   | “前缀表”、“next数组”、利用公共前后缀进行移位匹配的匹配算法 |

#### **13.2.1 朴素暴力算法**

```python
def find_brute(T, P):
  """返回子串P开始的T的最低索引（否则为-1）."""
  n, m = len(T), len(P)                      # introduce convenient notations
  for i in range(n-m+1):                     # 尝试T中的每个潜在起始索引
    k = 0                                    # an index into pattern P
    while k < m and T[i + k] == P[k]:        # kth character of P matches
      k += 1
    if k == m:                               # if we reached the end of pattern,
      return i                               # substring T[i:i+m] matches P
  return -1                                  # failed to find a match starting with any i
```

![image-20210331223538934](数据结构与算法（Python语言实现）.assets/image-20210331223538934.png)

**性能——O(nm)**

**最坏情况下的运行时间是O(nm)。**

穷举模式匹配算法由两个嵌套组成：一个是在文本模式所有可能的**开始**索引进行外部for循环；另一个是在模式的每个字符进行内部while循环索引，并将它和文章中潜在对应的字符进行**比较**。

最坏情况下，对于T中每个索引，无论如何都要对m个字符进行比较，最后可能不匹配。外部循环最多被执行n-m+1次，内部while循环最多执行m次，于是运行时间O(nm)。

#### **13.2.2 Boyer-Moore算法（每次后移两个规则之中的较大值）**

BM算法实际上包含两个并行的算法（也就是两个启发策略）：==**坏字符算法**==（***bad-character shift***）和==**好后缀算法**==（***good-suffix shift***）。**这两种算法的目的就是让模式串每次向右移动尽可能大的距离。**

- ==坏字符规则==（bad-character shift）：当文本串中的某个字符跟模式串的某个字符不匹配时，我们称文本串中的这个失配字符为坏字符，此时模式串需要向右移动，坏字符针对的是文本串T。

  ```
  移动的位数 = 坏字符在模式串P中的索引位置 - 坏字符在模式串P中未匹配的最右出现的索引位置。
  ```

  此外，如果"坏字符"不包含在模式串之中，则最右出现位置为 -1。

![image-20210401162214420](数据结构与算法（Python语言实现）.assets/image-20210401162214420.png)

- ==好后缀规则==（good-suffix shift）：当字符失配时，好后缀针对的是模式串P。

  ```
  后移位数 = 最后一个好后缀字符在模式串P中的索引位置 - 最后一个好后缀在模式串P上一次出现的索引位置
  ```

  如果好后缀在模式串中没有再次出现，则为 -1。

  ![image-20210401165900552](数据结构与算法（Python语言实现）.assets/image-20210401165900552.png)

  ![image-20210401164716611](数据结构与算法（Python语言实现）.assets/image-20210401164716611.png)

- ==如何选择哪种规则==：目的就是让模式串每次向右移动尽可能大的距离。

![image-20210401164842857](数据结构与算法（Python语言实现）.assets/image-20210401164842857.png)

Python实现

```python
def find_boyer_moore(T, P):
  """返回子串P开始的T的最低索引（否则为-1）."""
  n, m = len(T), len(P)                   # introduce convenient notations
  if m == 0: return 0                     # trivial search for empty string
  last = {}                               # 创建 'last' 字典
  for k in range(m):
    last[ P[k] ] = k                      # later occurrence overwrites
  # 将模式的结尾对齐到文本的索引m-1
  i = m-1                                 # an index into T
  k = m-1                                 # an index into P
  while i < n:
    if T[i] == P[k]:                      # a matching character
      if k == 0:
        return i                          # pattern begins at index i of text
      else:
        i -= 1                            # examine previous character
        k -= 1                            # of both T and P
    else:
      j = last.get(T[i], -1)              # last(T[i]) is -1 if not found
      i += m - min(k, j + 1)              # case analysis for jump step
      k = m - 1                           # restart at end of pattern
  return -1
```

**性能**

**最坏情况下的运行时间是O(nm)。**

#### **13.2.3 KMP算法（**利用公共前后缀进行移位匹配的匹配算法。在失配时固定主串指针i (i无需回溯)，依据Next[]将模式串向后移动与匹配指针对齐**）**

算法原理：https://www.bilibili.com/video/BV1Px411z7Yo?from=search&seid=16828101935069283935

算法代码：https://www.bilibili.com/video/BV1hW411a7ys/?spm_id_from=333.788.recommend_more_video.-1

主要思想：预先计算模式部分之间的自重叠，从而当不匹配发生在一个位置时，我们在继续搜寻之前就能立刻知道移动模式的最大数目。

- **失败函数/前缀表prefix**

  失败函数$f$用于表示匹配失败时P对应的位移；失败函数$f(k)$定义为P的最长前缀的长度（<u>"前缀"指除了最后一个字符以外，一个字符串的全部头部组合；"后缀"指除了第一个字符以外，一个字符串的全部尾部组合</u>），直观地说，如果在P[k+1]中找不到匹配，$f(k)$会告诉我们多少紧接着的字符可以用来重启模式。

![image-20210402150150732](数据结构与算法（Python语言实现）.assets/image-20210402150150732.png)

![image-20210402151303762](数据结构与算法（Python语言实现）.assets/image-20210402151303762.png)

- **next数组**

  接下来我们就用这个表来引出next数组，next 数组的值是除当前字符外（注意不包括当前字符）的公共前后缀最长长度，相当于把上表做一个变形，将表中公共前后缀最长长度全部右移一位，第一个值赋为-1。例如c对应next值的意义是，c之前（不包括c）的子串abaab所拥有的公共前后缀最长长度为2，我们称next数组中的值为失效函数值，也就是c的失效函数值为2。

  ![image-20210402152530479](数据结构与算法（Python语言实现）.assets/image-20210402152530479.png)

  当主串S与模式串P失配时，j=next[j]，P向右移动j - next[j]。也就是当模式串P后缀$p_{j-k}p_{j-k+1}…p_{j-1}$与主串S的$s_{i-k}s_{i-k+1}…s_{i-1}$匹配成功，但是$p_j$和$s_i$失配时，因为next[j]=k，相当于在不包含$p_j$的模式串中有最大长度为k的相同前后缀，也就是$p_0p_1…p_{k-1}$ = $p_{j-k}p_{j-k+1}…p_{j-1}$，所以令j = next[j]，让模式串右移j - next[j]位，使模式串$p_0p_1…p_{k-1}$ 与主串$s_{i-k}s_{i-k+1}…s_{i-1}$对齐，让$p_k$和$s_i$继续匹配。如下图所示：

  ![img](数据结构与算法（Python语言实现）.assets/20190424212356251.png)

  KMP的next数组告诉我们：当模式串中的某个字符跟主串中的某个字符失配时，模式串下一步应该跳到哪个位置。如模式串中在j 处的字符跟主串在i 处的字符匹配失配时，下一步用next [j] 处的字符继续跟主串i 处的字符匹配，相当于模式串向右移动 j - next[j] 位。

- **算法流程**

规定i是主串S的下标，j是模式T的下标。现在假设现在主串S匹配到 i 位置，模式串T匹配到 j 位置。

1. 如果j = -1，则i++，j++，继续匹配下一个字符；
2. 如果S[i] = T[j]，则i++，j++，继续匹配下一个字符；
3. 如果j != -1，且S[i] != P[j]，则 i 不变，j = next[j]。此举意味着失配时，接下来模式串T要相对于主串S向右移动j - next [j] 位。

- Python实现

```Python
def find_kmp(T, P):
  """返回子串P开始的T的最低索引（否则为-1）."""
  n, m = len(T), len(P)            # introduce convenient notations
  if m == 0: return 0              # trivial search for empty string
  fail = compute_kmp_fail(P)       # rely on utility to precompute
  j = 0                            # index into text
  k = 0                            # index into pattern
  while j < n:
    if T[j] == P[k]:               # P[0:1+k] matched thus far
      if k == m - 1:               # match is complete
        return j - m + 1           
      j += 1                       # try to extend match
      k += 1
    elif k > 0:                    
      k = fail[k-1]                # reuse suffix of P[0:k]
    else:
      j += 1
  return -1                        # reached end without match

def compute_kmp_fail(P):
  """计算并返回KMP“失败”列表/前缀表的实用程序."""
  m = len(P)
  fail = [0] * m                   # by default, presume overlap of 0 everywhere
  j = 1
  k = 0
  while j < m:                     # compute f(j) during this pass, if nonzero
    if P[j] == P[k]:               # k + 1 characters match thus far
      fail[j] = k + 1
      j += 1
      k += 1
    elif k > 0:                    # k follows a matching prefix
      k = fail[k-1]
    else:                          # no match found starting at j
      j += 1
  return fail
```

- **性能O(n+m)**

  计算主串搜索的时间复杂度是O(n)，计算失败函数/前缀表的时间复杂度为O(m)，总时间复杂度为O(n+m)；空间复杂度为O(m)。
  <u>n代表的是主串T的长度，m代表的是模式串P的长度，空间复杂度O(m)因为搭建了一个长度为m的临时列表。</u>

### 13.3 动态规划

漫画:什么是动态规划?(整合版)：https://www.sohu.com/a/149075950_684445

六大算法之三:动态规划：https://blog.csdn.net/zw6161080123/article/details/80639932

![image-20210402162554928](数据结构与算法（Python语言实现）.assets/image-20210402162554928.png)

- 算法步骤

  1、**创建一个一维数组或者二维数组**，保存每一个子问题的结果，具体创建一维数组还是二维数组看题目而定，基本上如果题目中给出的是一个一维数组进行操作，就可以只创建一个一维数组，如果题目中给出了两个一维数组进行操作或者两种不同类型的变量值，比如背包问题中的不同物体的体积与总体积，找零钱问题中的不同面值零钱与总钱数，这样就需要创建一个二维数组。

  注：需要创建二维数组的解法，都可以**创建一个一维数组运用滚动数组的方式来解决**（results = [[1]* [n]*m），即一位数组中的值不停的变化，后面会详细徐叙述。

  2、**设置数组边界值，一维数组就是设置第一个数字，二维数组就是设置第一行跟第一列的值**，特别的滚动一维数组是要设置整个数组的值，然后根据后面不同的数据加进来变幻成不同的值。

  3、**找出状态转换方程**，也就是说找到每个状态跟他上一个状态的关系，根据状态转化方程写出代码。

  4、**返回需要的值**，一般是数组的最后一个或者二维数组的最右下角。

- 例子

  ![image-20210402174210150](数据结构与算法（Python语言实现）.assets/image-20210402174210150.png)

  <img src="数据结构与算法（Python语言实现）.assets/image-20210402174357533.png" alt="image-20210402174357533"  />

![image-20210402174428774](数据结构与算法（Python语言实现）.assets/image-20210402174428774.png)

![image-20210402174625204](数据结构与算法（Python语言实现）.assets/image-20210402174625204.png)

- 动态规划与分治法区别

  **动态规划算法：**它通常用于求解具有某种最优性质的问题。在这类问题中，可能会有许多可行解。每一个解都对应于一个值，我们希望找到具有最优值的解。动态规划算法与分治法类似，其基本思想也是将待求解问题分解成若干个子问题，先求解子问题，然后从这些子问题的解得到原问题的解。与分治法不同的是，适合于用动态规划求解的问题，经分解得到子问题往往不是互相独立的。

  **分治法：**若用分治法来解这类问题，则分解得到的子问题数目太多，有些子问题被重复计算了很多次。如果我们能够保存已解决的子问题的答案，而在需要时再找出已求得的答案，这样就可以避免大量的重复计算，节省时间。我们可以用一个表来记录所有已解的子问题的答案。

### **13.4 文本压缩（哈夫曼编码、最优搜索树）和贪心算法（局部最优）**

哈夫曼编码：有固定长度的编码情况下，使用短码字符串对高频字符进行编码，并用长码字符串对低频字符进行编码，根据使用频率来最大化节省字符（编码）的存储空间。

哈夫曼树：哈夫曼树又称**最优二叉树**，**是一种带权路径长度最短的二叉树。**所谓树的带权路径长度，就是树中所有的叶结点的权值乘上其到根结点的路径长度（若根结点为0层，叶结点到根结点的路径长度为叶结点的层数）。树的带权路径长度记为WPL=(W1*L1+W2*L2+W3*L3+…+ Wn*Ln)，N个权值Wi(i=1,2,…n)构成一棵有N个叶结点的二叉树，相应的叶结点的路径长度为Li(i=1,2,…n)。可以证明哈夫曼树的WPL是最小的。

- 构造哈夫曼树的算法如下：
  	1）对给定的n个权值{W1,W2,W3,…,Wi,…,Wn}构成n棵二叉树的初始集合F={T1,T2,T3,…,Ti,…, Tn}，其中每棵二叉树Ti中只有一个权值为Wi的根结点，它的左右子树均为空。
  	2）在F中选取两棵根结点权值最小的树作为新构造的二叉树的左右子树，新二叉树的根结点的权值为其左右子树的根结点的权值之和。
  	3）从F中删除这两棵树，并把这棵新的二叉树同样以升序排列加入到集合F中。
  	4）重复2）和3），直到集合F中只有一棵二叉树为止。

```python
Algorithm Huffman(X):
    Input: 长度为n并且有d个不同字符的字符串X
    Output: X的编码树
    """计算X的每个字符c的频率f（c）。"""
    初始化一个优先级队列 Q.
    for each character c in X do
    	Create a single-node binary tree T storing c. :
        Insert T into Q with key f(c).
	while len(Q) > 1 do
    	(f1,T1) = Q.remove_ min()
        (f2,T2) = Q.remove_ min()
        Create a new binary tree T with left subtree T¡ and right subtree T2.
        Insert T into Q with key fi + f2.
	(f,T) = Q.remove. .min()
    return tree T
```

​		简而言之，就是要先知道一系列的权值信息（比如说要编码字符串的每个字符出现频率），然后把它们分别作为哈夫曼树中各个叶子节点的权值，接下来呢就需要由叶子节点来自下往上构造哈夫曼树了。
　　构造的思路是这样的：所有的叶子节点构成了最初的森林（所有树的集合），我们可以使用priority_queue对这些树进行管理，使得集合中的数据始终保持着递增的顺序（从小到大）。然后，每次就让前两个元素出队，再构造一个新的节点（树），其权值为出队的两个元素权值之和，左子树为前面第一个元素，右子树为前面第二个元素，这样集合中元素的个数－１。如此做，直至集合中只剩余一个节点（根节点）为止，此时仅有的这棵树便是哈夫曼树。

![image-20210406161654454](数据结构与算法（Python语言实现）.assets/image-20210406161654454.png)

性能：哈夫曼算法（最优搜索树/哈夫曼树）时间复杂度为$O(n+dlogd)$

可以使用贪心算法解决的问题：全局最优的性质可以通过一系列局部最优选择来实现，即选择是当时可用的可能性之中每一个当前最优的选择。

### **13.5	字典树（前缀树）**

https://desertwatermelon.blog.csdn.net/article/details/81990417

字典树-前缀树和后缀树 ： https://www.pianshen.com/article/844317604/

13.5.1 标准字典树（**空间换时间**，S中没有一个字符串是另一个字符串的前缀！{be,bell}X，多叉树）

令S为一个来自字母表$\sum$的s个字符串的集合，一个存储来自字母表$\sum$的所有字符串的长度总和为n的s个字符串的集合S的标准字典树有以下特性：

- T的高度和S中最长的字符串的长度相等

- T的每个内部节点至多有|$\sum$|的孩子

- T有s个叶子结点

- T的节点的数目至多是n+1（对应最坏情况，没有两个字符串分享一个共同的非空前缀）

![image-20210406172531327](数据结构与算法（Python语言实现）.assets/image-20210406172531327.png)

性能：搜索一个长度为m的字符串的运行时间为O(m)；构建完整字典树运行时间O(n)。

13.5.2 压缩字典树（压缩单个孩子节点）

与标准字典树类似，但确保每个内部节点至少有两个孩子节点。通过压缩单个孩子节点的链为**单条边执行规则**：通俗来说就是某个内部节点（根节点，孩子节点除外）只有一个孩子节点也就是一条边的时候，把该节点和其孩子节点整合为一个节点，达到压缩空间的目的。仅当在已经存储在基本结构中的字符串集合之上作为辅助索引结构，以及不需要世纪存储在集合中的字符串所有字符是才有优势。

![image-20210406193128769](数据结构与算法（Python语言实现）.assets/image-20210406193128769.png)

令S为一个来自字母表$\sum$的s个字符串的集合，存储大小为d的取自字母表的s个字符串的集合S的压缩字典树有以下特性：

- T的每个内部节点至少有2个孩子节点，至多有d个孩子节点。(消灭了单个孩子节点，至多对应一个内部节点)
- T有s个叶子结点（非前缀字符串，每个字符串必以叶子结点结束）
- T的节点的数目是O(s)

13.5.3 后缀字典树

把一串字符的所有后缀保存并且压缩的字典树。相对于字典树来说，后缀树并不是针对大量字符串的，而是针对一个或几个字符串来解决问题。比如字符串的回文子串，两个字符串的最长公共子串等等。

![image-20210406205039525](数据结构与算法（Python语言实现）.assets/image-20210406205039525.png)

性能：长度为n的字符串X的后缀树空间复杂度为O(n)。

## ==第14章  图算法==

**数据结构——图的概述:**https://blog.csdn.net/yjw123456/article/details/90211563
**大话数据结构-图:**https://www.cnblogs.com/w-wanglei/p/figure.html

图是表示对象之间的存在关系的一种方式。图是由顶点的有穷非空集合和顶点之间边的集合组成，通过表示为$G(V,E)$，其中，$G$表示一个图，$V$是图$G$中顶点的集合，$E$是图$G$中边的集合。

### **==基本概念==**

**加权图：**与加权图对应的就是无权图，或叫等权图。如果一张图不含权重信息，我们就认为边与边之间没有差别。不过，具体建模的时候，很多时候都需要有权重，比如对中国重要城市间道路联系的建模，总不能认为从北京去上海和从北京去广州一样远(等权)。

**完全图：**每一对顶点间都存在一条边的图。

无向图中，任意两个顶点间都有边，称为无向完全图。

两个重要关系：

- 邻接(adjacency)：邻接是**两个顶点**之间的一种关系。如果图包含$( u , v )$，则称顶点$v$与顶点$u$邻接。当然，在无向图中，这也意味着顶点$u$与顶点$v$邻接。
- 关联(incidence)：关联是**边和顶点**之间的关系。在有向图中，边$( u , v )$从顶点$u$开始关联到$v$，或者相反，从$v$关联到$u$。
  注意，有向图中，边不一定是对称的，有去无回是完全有可能的。细化这个概念，就有了顶点的**入度(in-degree)**和**出度(out-degree)**。无向图中，顶点的度就是与顶点相关联的边的总数，没有入度和出度。在有向图中，我们以上图为例，顶点10有2个入度，3 → 10 ，11 → 10，但是没有从10指向其它顶点的边，因此顶点10的出度为0。

**路径(path)：**依次遍历顶点序列之间的边所形成的轨迹。注意，依次就意味着有序，先1后2和先2后1不一样。
简单路径：没有重复顶点的路径称为简单路径。说白了，这一趟路里没有出现绕了一圈回到同一点的情况，也就是没有环。

![image-20210407203920638](数据结构与算法（Python语言实现）.assets/image-20210407203920638.png)

**环：**包含相同的顶点两次或者两次以上。上图中的顶点序列&lt; 1 , 2 , 4 , 3 , 1 &gt; &lt;1,2,4,3,1&gt;<1,2,4,3,1>，1出现了两次，当然还有其它的环，比如&lt; 1 , 4 , 3 , 1 &gt; &lt;1,4,3,1&gt;<1,4,3,1>。

**无环图：**没有环的图，其中，有向无环图有特殊的名称，叫做DAG(Directed Acyline Graph)（最好记住，DAG具有一些很好性质，比如很多动态规划的问题都可以转化成DAG中的最长路径、最短路径或者路径计数的问题）。

![image-20210407204316738](数据结构与算法（Python语言实现）.assets/image-20210407204316738.png)

**连通的：**无向图 G 中，若对任意两点，从顶点$V_i$ 到顶点 $V_j$ 有路径，则称 $V_i$ 和 $V_j$ 是连通的。无向图中每一对不同的顶点之间都有路径。如果这个条件在有向图里也成立，那么就是**强连通**的。下图中的图不是连通的，因为看到a和d之间没有通路。

![image-20210407203952214](数据结构与算法（Python语言实现）.assets/image-20210407203952214.png)

**连通分量：**不连通的图是由2个或者2个以上的连通子图组成的。这些不相交的连通子图称为图的连通分量。

任何连通图的连通分量只有一个，即其自身，而非连通的无向图有多个连通分量

![image-20210407210436812](数据结构与算法（Python语言实现）.assets/image-20210407210436812.png)

 以上图为例，总共有四个连通分量，分别是：ABCD、E、FG、HI。

**有向图的连通分量：**如果某个有向图不是强连通的，而将它的方向忽略后，任何两个顶点之间总是存在路径，则该有向图是弱连通的。若有向图的子图是强连通的，且不包含在更大的连通子图中，则可以称为有向图的**强连通**分量。
下图中，$a、e$没有到${ b , c , d }$中的顶点的路径，所以各自是独立的连通分量。因此，图中有三个强连通分量，用集合写出来就是：{{$a$ } { $e$ } , { $b , c , d$ } } 已经用不同颜色标出）。

![image-20210407204114045](数据结构与算法（Python语言实现）.assets/image-20210407204114045.png)

**关节点(割点)：**某些特定的顶点对于保持图或连通分支的连通性有特殊的重要意义。如果移除某个顶点将使图或者分支失去连通性，则称该顶点为关节点。如下图中的$c$。

![image-20210407204132590](数据结构与算法（Python语言实现）.assets/image-20210407204132590.png)

关节点的重要性不言而喻。如果你想要破坏互联网，你就应该找到它的关节点。同样，要防范敌人的攻击，首要保护的也应该是关节点。在资源总量有限的前提下，找出关节点并给予特别保障，是提高系统整体稳定性和鲁棒性的基本策略。
**桥(割边)：**和关节点类似，删除一条边，就产生比原图更多的连通分支的子图，这条边就称为割边或者桥。

**生成树：**无向图中连通且n个顶点n-1条边。
**最小生成树**：在连通网的所有生成树中，所有边的权重和最小的生成树。
**有向树：**有向图中一顶点入度为0，其余顶点入度为1。
**生成森林：**一个图由若干颗树构成

### ==图的抽象数据类型ADT==

​																表14-1	Edge类方法

| Class_Edge方法 | 描述                                                         |
| -------------- | ------------------------------------------------------------ |
| **endpoint()** | 返回元组(u,v)，顶点u是边的起点，顶点v是终点；对于无向图，方向是任意的 |
| **opposite()** | 假设顶点v是边的一个端点(起点或终点)，返回另一个端点          |

​																表14-2	Graph类方法

| Class_graph方法                | 描述                                                         |
| ------------------------------ | ------------------------------------------------------------ |
| **vertex_count()**             | 返回图的顶点的数目。                                         |
| **vertices()**                 | 迭代返回图中所有顶点。                                       |
| **edge_count()**               | 返回图的边的数目。                                           |
| **edges()**                    | 迭代返回图的所有边                                           |
| **get_edge(u,v)**              | 返回从中顶点u到顶点v的边，如果其中一个存在；否则返回None。无向图get_edge(u,v)=get_edge(v,u) |
| **degree(v,out=True)**         | 无向图，返回边入射到顶点V的数目。有向图，返回入射到顶点v的输出（输入）边的数目，由可选参数决定。 |
| **incident_edges(v,out=True)** | 返回所有边入射到顶点v的迭代循环                              |
| **insert_vertex(x=None)**      | 创建和返回一个新的存储元素x的Vertex                          |
| **insert_edge(u,v,x=None)**    | 创建和返回一个新的从顶点u到顶点v的存储元素x的Edge            |
| **remove_vertex(v)**           | 移除顶点v和图中它的所有入射边                                |
| **remove_edge(e)**             | 移除图中的边e                                                |

![image-20210407215710842](数据结构与算法（Python语言实现）.assets/image-20210407215710842.png)

### 14.2	图的数据结构（边列表、邻接列表、邻接图、邻接矩阵）

- **边列表：**对所有边采用无序的列表。
- **邻接列表：**用数组和链表结合的存储方式来标示图的方法称为邻接表。为每个顶点维护一个单独的列表，包括入射到顶点的那些边。通过取较小集合的并集来确定完整的边集合。
- **邻接图：**所有入射到顶点的边的次级容器被组织成一个图，用相邻的顶点作为键。
- **邻接矩阵：**图的邻接矩阵存储方式是用两个数组来标示图。一个一位数组存储图顶点的信息，一个二维数组（称为邻接矩阵）存储图中边或者弧的信息。

![image-20210408170420123](数据结构与算法（Python语言实现）.assets/image-20210408170420123.png)

4种数据结构的性能总结：

​													**表14-3	对Graph ADT方法运行时间的总结。**
​											$n$表示顶点的数目，$m$表示边的数目，$d_v$表示顶点v的度。
​								空间开销：邻接矩阵$O(n^2)$；边列表、邻接图、邻接链表$O(n+m)$

| 操作                   | 边列表 |     邻接列表      |   邻接图   | 邻接矩阵 |
| ---------------------- | :----: | :---------------: | :--------: | :------: |
| **vertex_count()**     | $O(1)$ |      $O(1)$       |   $O(1)$   |  $O(1)$  |
| **edge_count()**       | $O(1)$ |      $O(1)$       |   $O(1)$   |  $O(1)$  |
| **vertices()**         | $O(n)$ |      $O(n)$       |   $O(n)$   |  $O(n)$  |
| **edges()**            | $O(m)$ |      $O(m)$       |   $O(m)$   |  $O(m)$  |
| **get_edge(u,v)**      | $O(m)$ | $O(mid(d_u,d_v))$ | $O(1)exp.$ |  $O(1)$  |
| **degree(v)**          | $O(m)$ |      $O(1)$       |   $O(1)$   |  $O(n)$  |
| **incident_edges(v)**  | $O(m)$ |     $O(d_v)$      |  $O(d_v)$  |  $O(n)$  |
| **insert_vertex(x)**   | $O(1)$ |      $O(1)$       |   $O(1)$   | $O(n^2)$ |
| **remove_vertex(v)**   | $O(m)$ |     $O(d_v)$      |  $O(d_v)$  | $O(n^2)$ |
| **insert_edge(u,v,x)** | $O(1)$ |      $O(1)$       | $O(1)exp.$ |  $O(1)$  |
| **remove_edge(e)**     | $O(1)$ |      $O(1)$       | $O(1)exp.$ |  $O(1)$  |

14.2.1 边列表结构

所有顶点存储在一个无序的列表$V$中，所有边对象存储在一个无序的列表$E$中。集合$V$和$E$用双向链表表示，双向链表使用第七章PositionalList类。

<img src="数据结构与算法（Python语言实现）.assets/image-20210408173423985.png" alt="image-20210408173423985" style="zoom:85%;" />

14.2.2 邻接图结构

让每个入射边的相反的端点作为图的主键，用边结构作为值。

<img src="数据结构与算法（Python语言实现）.assets/image-20210408175501213.png" alt="image-20210408175501213" style="zoom:85%;" />

#### 14.2.3 邻接矩阵结构（空间开销大，添加或移除顶点开销大，便于查找边、计算顶点度）

图G的邻接矩阵结构对边列表结构增加了一个矩阵$A$（二维矩阵$A[i] [j]$），在邻接矩阵表示方法中，我们考虑顶点以集合{$0,1，...，n-1$}中的数字来表示，边以这些数字中的其中一对来表示。单元格$A[i,j]$存储边(u,v)的引用（若边不存在，$A[i,j]$=None）对于无向图，数组A沿主对角线对称。

![image-20210408211202031](数据结构与算法（Python语言实现）.assets/image-20210408211202031.png)

#### 14.2.4 邻接链表结构(计算顶点的度需要遍历一个链表，空间开销小，便于添加和移除顶点)

图中顶点$V$用一个一维数组存储，对于顶点数组中，每个数据元素还需要存储指向第一个邻接点的指针，以便于查找该顶点的边信息。图中每个顶点$V$的所有邻接点构成一个线性表，由于邻接点的个数不定，所以用单链表存储，无向图称为顶点$V_i$的边表，有向图则称为顶点$V$作为弧尾的出边表。

![image-20210408213014813](数据结构与算法（Python语言实现）.assets/image-20210408213014813.png)

![image-20210408223133060](数据结构与算法（Python语言实现）.assets/image-20210408223133060.png)

14.2.5 Python实现

对于每个顶点$v$，我们用Python字典表示次级入射图$l(v)$。数组$V$被顶级字典代替，顶级字典$D$将每个顶点$v$映射到其入射图$l(v)$。我们可以通过生成字典$D$的主键的集合来迭代所有的顶点。

> Python自带networkx库，内嵌networkx.Graph()方法。

- **创建Vertex类和Edge类**（嵌套在Graph类中）

```python
class Vertex:
    """图的轻量级顶点结构."""
    __slots__ = '_element'
  
    def __init__(self, x):
      """Do not call constructor directly. Use Graph's insert_vertex(x)."""
      self._element = x
  
    def element(self):
      """Return element associated with this vertex."""
      return self._element
  
    def __hash__(self):         # will allow vertex to be a map/set key
      return hash(id(self))

    def __str__(self):
      return str(self._element)

 class Edge:
    """图的轻量级边结构."""
    __slots__ = '_origin', '_destination', '_element'
  
    def __init__(self, u, v, x):
      """Do not call constructor directly. Use Graph's insert_edge(u,v,x)."""
      self._origin = u
      self._destination = v
      self._element = x
  
    def endpoints(self):
      """Return (u,v) tuple for vertices u and v."""
      return (self._origin, self._destination)
  
    def opposite(self, v):
      """Return the vertex that is opposite v on this edge."""
      if not isinstance(v, Graph.Vertex):
        raise TypeError('v must be a Vertex')
      return self._destination if v is self._origin else self._origin
      raise ValueError('v not incident to edge')
  
    def element(self):
      """Return element associated with this edge."""
      return self._element
  
    def __hash__(self):         # will allow edge to be a map/set key
      return hash( (self._origin, self._destination) )

    def __str__(self):
      return '({0},{1},{2})'.format(self._origin,self._destination,self._element)
```

- **创建Graph类（基于邻接图结构）**

```python
class Graph:
  """使用邻接图表示简单图."""
  #------------------------- 嵌套顶点类class Vertex -------------------------
  class Vertex:
   ...
  #-------------------------   嵌套边类class Edge  -------------------------
  class Edge:
    ...
  #------------------------- Graph methods -------------------------
  def __init__(self, directed=False):
    """Create an empty graph (undirected, by default).

    Graph is directed if optional paramter is set to True.
    """
    self._outgoing = {}
    # only create second map for directed graph; use alias for undirected
    self._incoming = {} if directed else self._outgoing

  def _validate_vertex(self, v):
    """Verify that v is a Vertex of this graph."""
    if not isinstance(v, self.Vertex):
      raise TypeError('Vertex expected')
    if v not in self._outgoing:
      raise ValueError('Vertex does not belong to this graph.')
    
  def is_directed(self):
    """Return True if this is a directed graph; False if undirected.

    Property is based on the original declaration of the graph, not its contents.
    """
    return self._incoming is not self._outgoing # directed if maps are distinct

  def vertex_count(self):
    """Return the number of vertices in the graph."""
    return len(self._outgoing)

  def vertices(self):
    """Return an iteration of all vertices of the graph."""
    return self._outgoing.keys()

  def edge_count(self):
    """Return the number of edges in the graph."""
    total = sum(len(self._outgoing[v]) for v in self._outgoing)
    # for undirected graphs, make sure not to double-count edges
    return total if self.is_directed() else total // 2

  def edges(self):
    """Return a set of all edges of the graph."""
    result = set()       # avoid double-reporting edges of undirected graph
    for secondary_map in self._outgoing.values():
      result.update(secondary_map.values())    # add edges to resulting set
    return result

  def get_edge(self, u, v):
    """Return the edge from u to v, or None if not adjacent."""
    self._validate_vertex(u)
    self._validate_vertex(v)
    return self._outgoing[u].get(v)        # returns None if v not adjacent

  def degree(self, v, outgoing=True):   
    """Return number of (outgoing) edges incident to vertex v in the graph.

    If graph is directed, optional parameter used to count incoming edges.
    """
    self._validate_vertex(v)
    adj = self._outgoing if outgoing else self._incoming
    return len(adj[v])

  def incident_edges(self, v, outgoing=True):   
    """Return all (outgoing) edges incident to vertex v in the graph.

    If graph is directed, optional parameter used to request incoming edges.
    """
    self._validate_vertex(v)
    adj = self._outgoing if outgoing else self._incoming
    for edge in adj[v].values():
      yield edge

  def insert_vertex(self, x=None):
    """Insert and return a new Vertex with element x."""
    v = self.Vertex(x)
    self._outgoing[v] = {}
    if self.is_directed():
      self._incoming[v] = {}        # need distinct map for incoming edges
    return v
      
  def insert_edge(self, u, v, x=None):
    """Insert and return a new Edge from u to v with auxiliary element x.

    Raise a ValueError if u and v are not vertices of the graph.
    Raise a ValueError if u and v are already adjacent.
    """
    if self.get_edge(u, v) is not None:      # includes error checking
      raise ValueError('u and v are already adjacent')
    e = self.Edge(u, v, x)
    self._outgoing[u][v] = e
    self._incoming[v][u] = e
```

- **创建Graph类（基于邻接矩阵）**

```python
class Graph_Matrix:
    """
    Adjacency Matrix
    """
    def __init__(self, vertices=[], matrix=[]):
        """

        :param vertices:a dict with vertex id and index of matrix , such as {vertex:index}
        :param matrix: a matrix
        """
        self.matrix = matrix
        self.edges_dict = {}  # {(tail, head):weight}
        self.edges_array = []  # (tail, head, weight)
        self.vertices = vertices
        self.num_edges = 0

        # if provide adjacency matrix then create the edges list
        if len(matrix) > 0:
            if len(vertices) != len(matrix):
                raise IndexError
            self.edges = self.getAllEdges()
            self.num_edges = len(self.edges)

        # if do not provide a adjacency matrix, but provide the vertices list, build a matrix with 0
        elif len(vertices) > 0:
            self.matrix = [[0 for col in range(len(vertices))] for row in range(len(vertices))]

        self.num_vertices = len(self.matrix)

    def isOutRange(self, x):
        try:
            if x >= self.num_vertices or x <= 0:
                raise IndexError
        except IndexError:
            print("节点下标出界")

    def isEmpty(self):
        if self.num_vertices == 0:
            self.num_vertices = len(self.matrix)
        return self.num_vertices == 0

    def add_vertex(self, key):
        if key not in self.vertices:
            self.vertices[key] = len(self.vertices) + 1

        # add a vertex mean add a row and a column
        # add a column for every row
        for i in range(self.getVerticesNumbers()):
            self.matrix[i].append(0)

        self.num_vertices += 1

        nRow = [0] * self.num_vertices
        self.matrix.append(nRow)

    def getVertex(self, key):
        pass

    def add_edges_from_list(self, edges_list):  # edges_list : [(tail, head, weight),()]
        for i in range(len(edges_list)):
            self.add_edge(edges_list[i][0], edges_list[i][1], edges_list[i][2], )

    def add_edge(self, tail, head, cost=0):
        # if self.vertices.index(tail) >= 0:
        #   self.addVertex(tail)
        if tail not in self.vertices:
            self.add_vertex(tail)
        # if self.vertices.index(head) >= 0:
        #   self.addVertex(head)
        if head not in self.vertices:
            self.add_vertex(head)

        # for directory matrix
        self.matrix[self.vertices.index(tail)][self.vertices.index(head)] = cost
        # for non-directory matrix
        # self.matrix[self.vertices.index(fromV)][self.vertices.index(toV)] = \
        #   self.matrix[self.vertices.index(toV)][self.vertices.index(fromV)] = cost

        self.edges_dict[(tail, head)] = cost
        self.edges_array.append((tail, head, cost))
        self.num_edges = len(self.edges_dict)

    def getEdges(self, V):
        pass

    def getVerticesNumbers(self):
        if self.num_vertices == 0:
            self.num_vertices = len(self.matrix)
        return self.num_vertices

    def getAllVertices(self):
        return self.vertices

    def getAllEdges(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if 0 < self.matrix[i][j] < float('inf'):
                    self.edges_dict[self.vertices[i], self.vertices[j]] = self.matrix[i][j]
                    self.edges_array.append([self.vertices[i], self.vertices[j], self.matrix[i][j]])

        return self.edges_array

    def __repr__(self):
        return str(''.join(str(i) for i in self.matrix))

    def to_do_vertex(self, i):
        print('vertex: %s' % (self.vertices[i]))

    def to_do_edge(self, w, k):
        print('edge tail: %s, edge head: %s, weight: %s' % (self.vertices[w], self.vertices[k], str(self.matrix[w][k])))
        
#------------------------- 第一种方法，二维数组生成图 -------------------------
def create_undirected_matrix(my_graph):
    nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    matrix = [[0, 1, 1, 1, 1, 1, 0, 0],  # a
              [0, 0, 1, 0, 1, 0, 0, 0],  # b
              [0, 0, 0, 1, 0, 0, 0, 0],  # c
              [0, 0, 0, 0, 1, 0, 0, 0],  # d
              [0, 0, 0, 0, 0, 1, 0, 0],  # e
              [0, 0, 1, 0, 0, 0, 1, 1],  # f
              [0, 0, 0, 0, 0, 1, 0, 1],  # g
              [0, 0, 0, 0, 0, 1, 1, 0]]  # h

    my_graph = Graph_Matrix(nodes, matrix)
    print(my_graph)
    return my_graph
#------------------------- 第二种方法，二维数组生成有向图 -------------------------
def create_directed_matrix(my_graph):
    nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    inf = float('inf')
    matrix = [[0, 2, 1, 3, 9, 4, inf, inf],  # a
              [inf, 0, 4, inf, 3, inf, inf, inf],  # b
              [inf, inf, 0, 8, inf, inf, inf, inf],  # c
              [inf, inf, inf, 0, 7, inf, inf, inf],  # d
              [inf, inf, inf, inf, 0, 5, inf, inf],  # e
              [inf, inf, 2, inf, inf, 0, 2, 2],  # f
              [inf, inf, inf, inf, inf, 1, 0, 6],  # g
              [inf, inf, inf, inf, inf, 9, 8, 0]]  # h

    my_graph = Graph_Matrix(nodes, matrix)
    print(my_graph)
    return my_graph
#------------------------- 第三种方法，用边生成有向图 -------------------------
def create_directed_graph_from_edges(my_graph):
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    edge_list = [('A', 'F', 9), ('A', 'B', 10), ('A', 'G', 15), ('B', 'F', 2),
                 ('G', 'F', 3), ('G', 'E', 12), ('G', 'C', 10), ('C', 'E', 1),
                 ('E', 'D', 7)]

    my_graph = Graph_Matrix(nodes)
    my_graph.add_edges_from_list(edge_list)
    print(my_graph)
    return my_graph
#-------------------------  显示无向图-------------------------
def draw_undircted_graph(my_graph):
    G = nx.Graph()  # 建立一个空的无向图G
    for node in my_graph.vertices:
        G.add_node(str(node))
    for edge in my_graph.edges:
        G.add_edge(str(edge[0]), str(edge[1]))

    print("nodes:", G.nodes())  # 输出全部的节点： [1, 2, 3]
    print("edges:", G.edges())  # 输出全部的边：[(2, 3)]
    print("number of edges:", G.number_of_edges())  # 输出边的数量：1
    nx.draw(G, with_labels=True)
    plt.savefig("undirected_graph.png")
    plt.show()
#-------------------------  显示有向图，带权-------------------------
def draw_directed_graph(my_graph):
    G = nx.DiGraph()  # 建立一个空的无向图G
    for node in my_graph.vertices:
        G.add_node(str(node))
    G.add_weighted_edges_from(my_graph.edges_array)

    print("nodes:", G.nodes())  # 输出全部的节点
    print("edges:", G.edges())  # 输出全部的边
    print("number of edges:", G.number_of_edges())  # 输出边的数量
    nx.draw(G, with_labels=True)
    plt.savefig("directed_graph.png")
    plt.show()
```

- **创建Graph类（基于邻接表）**

```python
class Vertex:
    def __init__(self,key):
        self.id=key
        self.connectedTo={}
    
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr]=weight
    
    def __str__(self):
        return str(self.id)+' connectedTo: '+str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id
    
    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList={}
        self.numVertices=0

    def addVertex(self,key):
        self.numVertices=self.numVertices+1
        newVertex=Vertex(key)
        self.vertList[key]=newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv=self.addVertex(f)
        if t not in self.vertList:
            nv=self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t],cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

if __name__=="__main__":
    g=Graph()
    for i in range(6):
        g.addVertex(i)
    print(g.vertList)
    g.addEdge(0,1,5)
    g.addEdge(0,5,2)
    g.addEdge(1,2,4)
    g.addEdge(2,3,9)
    g.addEdge(3,4,7)
    g.addEdge(3,5,3)
    g.addEdge(4,0,1)
    g.addEdge(5,4,8)
    g.addEdge(5,2,1)
    for v in g:
        for w in v.getConnections():
            print("(%s,%s)"%(v.getId(),w.getId()))
```

### 14.3	图遍历

#### 14.3.1 深度优先遍历（DFS，递归，基于栈）

![image-20210407220149965](数据结构与算法（Python语言实现）.assets/image-20210407220149965.png)

​                                                                     代码段14-4 DFS算法伪代码

```python
Algorithm DFS(G,u):
    Input:A graph G and a vertex u of G
    Output:A collection of vertices reachable from u,with their discovery edges
        for each outgoing edge e=(u,v) fo u do
            if vertex v has not been visited then
                mark vertex v as visited(via edge e)
                recursively call DFS(G,v).
```

- **DFS运行时间O(n+m)**

定义G是一个有n个顶点和m条边的无向图。

| 遍历                              | O(n+m)     |
| --------------------------------- | ---------- |
| **计算G的两个已知顶点之间的路径** | **O(n+m)** |
| **测试G是否是连通的**             | **O(n+m)** |
| **计算G的生成树**                 | **O(n+m)** |
| **计算G的连通分支**               | **O(n+m)** |
| **计算G的循环**                   | **O(n+m)** |

定义G是一个有n个顶点和m条边的有向图。

| 遍历                                     | O(n+m)     |
| ---------------------------------------- | ---------- |
| **计算G的两个已知顶点之间的有向路径**    | **O(n+m)** |
| **测试G是否是强连通的**                  | **O(n+m)** |
| **计算从已知的顶点s可达的G的顶点的集合** | **O(n+m)** |
| **计算G的传递闭包**                      | **O(n+m)** |
| **计算G的有向循环**                      | **O(n+m)** |

- Python实现

  ​                                      代码段14-5	以指定的顶点v开始的图的DFS递归实现

```python
def DFS(g, u, discovered):
  """从顶点u开始对图g的未发现部分执行DFS.

  参数discovered是将每个顶点映射到在DFS期间用于发现它的边的字典。(顶点u被调用之前应该是已标记的.)
  result是新发现的顶点将被添加到字典中。
  """
  for e in g.incident_edges(u):    # for every outgoing edge from u
    v = e.opposite(u)
    if v not in discovered:        # v is an unvisited vertex  若顶点v未被标记
      discovered[v] = e            # e is the tree edge that discovered v  添加标记点v
      DFS(g, v, discovered)        # recursively explore from v  从顶点v出发，递归过程

```

​                                                    代码段14-6	重建u到v的有向路径的函数

```python
def construct_path(u, v, discovered):
  """
  返回包含从u到v的有向路径的顶点列表,
  如果无法从u获得v，则返回一个空列表。

  参数discovered是从u处开始对DFS的先前调用产生的字典。
  """
  path = []                        # empty path by default
  if v in discovered:
    # we build list from v to u and then reverse it at the end
    path.append(v)
    walk = v
    while walk is not u:
      e = discovered[walk]         # find edge leading to walk
      parent = e.opposite(walk)
      path.append(parent)
      walk = parent
    path.reverse()                 # reorient path from u to v
  return path
```

​													代码段14-7	判断图g是否是连通的

```python
无向图：从任意顶点简单地开始DFS，然后判断 if len(discovered) == 顶点数n，相等则说明连通。
有向图：对任意顶点开始DFS，若任何一个顶点都未被访问，且不可达s，则图不是强连通的；若访问了图G的所有顶点，需要检查是否s从其他所有顶点都可达，通过改写DFS将输入边而不是输出边循环到当前顶点，实现这一逆过程。
```

​								 代码段14-8	计算所有的连通分支O(n+m)，返回全部图的DFS森林

```python
def DFS_complete(g):
  """对整个图形执行DFS，然后将森林返回为字典。

  结果将每个顶点v映射到用于发现它的边
  (作为DFS树的根的顶点将映射为“无”)
  连通分支的数目可以通过用None作为发现边（DFS树的根）的discovered字典中顶点的数目来判定
  """
  forest = {}
  for u in g.vertices():
    if u not in forest:
      forest[u] = None             # u will be the root of a tree
      DFS(g, u, forest)
  return forest
```

#### 14.3.2 广度优先遍历（BFS，while循环，基于队列）

![image-20210407220137352](数据结构与算法（Python语言实现）.assets/image-20210407220137352.png)

- Python实现

​								                代码段14-8	以任意顶点s开始的图的BFS实现

```Python
def BFS(g, s, discovered):
  """
  从顶点s开始对图g的未发现部分执行BFS.

  参数discovered是将每个顶点映射到在BFS期间用于发现它的边的字典。(顶点s被调用之前应该是已标记的.)
  结果是新发现的顶点将被添加到字典中.
  """
  level = [s]                        # first level includes only s
  while len(level) > 0:
    next_level = []                  # prepare to gather newly found vertices
    for u in level:
      for e in g.incident_edges(u):  # for every outgoing edge from u
        v = e.opposite(u)
        if v not in discovered:      # v is an unvisited vertex
          discovered[v] = e          # e is the tree edge that discovered v
          next_level.append(v)       # v will be further considered in next pass
    level = next_level               # relabel 'next' level to become current
```

​												代码段14-9	重建u到v的有向路径的函数

```python
同代码段14-6 def construct_path(u, v, discovered)
```

 								代码段14-10	计算所有的连通分支O(n+m)，返回全部图的BFS森林

```python
def BFS_complete(g):
  """对整个图形执行BFS，然后将森林返回为字典。

  结果将每个顶点v映射到用于发现它的边
  (作为DFS树的根的顶点将映射为“无”)
  连通分支的数目可以通过用None作为发现边（DFS树的根）的discovered字典中顶点的数目来判定
  """
  forest = {}
  for u in g.vertices():
    if u not in forest:
      forest[u] = None            # u will be a root of a tree
      BFS(g, u, forest)
  return forest
```

- **BFS遍历的运行时间O(n+m)**

定义G是一个有n个顶点和m条边，用邻接链表结构表示的图，G的BFS遍历需要O(n+m)时间。

**14.4	传递闭包/Floyed_Warshall算法（多源最短路径，动态规划）**

https://blog.csdn.net/yuewenyao/article/details/81021319

有向图G的传递闭包是有向图G*，使得 G *的顶点和G的顶点一样，G *有一条边(u,v)并且无论是否从u到v有一条有向路径（包括(u,v)本身存在于G中的情况）

>Floyd算法适用于邻接矩阵，时间复杂度为O($n^3$)；DFS适用于邻接列表/邻接图，时间复杂度为O(n+m)。

​												代码段14-10	Floyed_Warshall算法

```python
from copy import deepcopy

def floyd_warshall(g):
  """返回一个新图，它是g的传递闭包."""
  closure = deepcopy(g)                      # imported from copy module
  verts = list(closure.vertices())           # make indexable list
  n = len(verts)
  for k in range(n):
    for i in range(n):
      # verify that edge (i,k) exists in the partial closure
      if i != k and closure.get_edge(verts[i],verts[k]) is not None:
        for j in range(n):
          # verify that edge (k,j) exists in the partial closure
          if i != j != k and closure.get_edge(verts[k],verts[j]) is not None:
            # if (i,j) not yet included, add it to the closure
            if closure.get_edge(verts[i],verts[j]) is None:
              closure.insert_edge(verts[i],verts[j])
  return closure
```

- Floyd优缺点分析：


优点：比较容易容易理解，可以算出任意两个节点之间的最短距离，代码编写简单。
缺点：时间复杂度比较高($n^3$)，不适合计算大量数据，当数据稍微大点儿的时候就可以选择其他的算法来解决问题了，不然也会是超时。

- Floyd算法与Dijkstra算法的不同


1.Floyd算法是求任意两点之间的距离，是多源最短路，而Dijkstra(迪杰斯特拉)算法是求一个顶点到其他所有顶点的最短路径，是单源最短路。
2.Floyd算法属于动态规划，我们在写核心代码时候就是相当于推dp状态方程，Dijkstra(迪杰斯特拉)算法属于贪心算法。
3.Dijkstra(迪杰斯特拉)算法时间复杂度一般是o(n^2),Floyd算法时间复杂度是o(n^3),Dijkstra(迪杰斯特拉)算法比Floyd算法块。
4.Floyd算法可以算带负权的，而Dijkstra(迪杰斯特拉)算法是不可以算带负权的。并且Floyd算法不能算负权回路。

**14.5	有向非循环图**

- **拓扑排序**

定义G是有n个顶点的有向图。图G的拓扑排序是对G的每条边$(v_i,v_j)$来说G的顶点的顺序$v_1,...,v_n$，这种情况下$i<j$，<u>也就是说，拓扑排序是一种排序，使得G的任何有向路径以增加的顺序遍历顶点。</u>

> 当且仅当G是非循环的，G有一个拓扑排序。

![image-20210414153154938](数据结构与算法（Python语言实现）.assets/image-20210414153154938.png)

​												      代码段14-11	拓扑排序算法

```python
def topological_sort(g):
  """
  以拓扑顺序返回非循环有向图g的顶点列表。
  如果图g有一个循环，则结果将是不完整的。
  """
  topo = []             # 以拓扑顺序放置的顶点列表
  ready = []            # 没有剩余约束的顶点列表
  incount = {}          # 跟踪每个顶点的度
  for u in g.vertices():
    incount[u] = g.degree(u, False)  # parameter requests incoming degree
    if incount[u] == 0:              # if u has no incoming edges,
      ready.append(u)                # it is free of constraints
  while len(ready) > 0:
    u = ready.pop()                  # u is free of constraints
    topo.append(u)                   # add u to the topological order
    for e in g.incident_edges(u):    # consider all outgoing neighbors of u
      v = e.opposite(u)
      incount[v] -= 1                # v has one less constraint without u
      if incount[v] == 0:
        ready.append(v)
  return topo
```

- 性能

定义G是一个有n个顶点m条边的使用邻接列表结构表示的有向图。拓扑排序算法使用了**O(n)辅助空间，运行时间是O(n+m)**，并且计算G的拓扑顺序或者加入一些顶点失败，表明G中存在有向循环。

### **14.6	最短路径**

**14.6.1	加权图**

加权图是一种有和每条边$e$相关联的数值标签的图，这个数值标签称为$e$的权值。对于$e=(u,v)$，记$w(u,v)=w(e)$。

![image-20210414161736617](数据结构与算法（Python语言实现）.assets/image-20210414161736617.png)

定义G为加权图。路径的长度（权重）是P的边的权值的总和。即$P=((v_0,v_1),(v_1,v_2),...,(v_k-1,v_k))$，那么P的长度（$w(P)$）被定义为

​									                   			$w(P)=\sum_{i=0}^{k-1}(w(v_i,v_i+1))$

在图中顶点u到顶点v之间的距离表示为$d(u,v)$，是从u到v之间最短路径。（G中$u,v$无路径，则$d(u,v)=∞$）

#### **14.6.2	Dijkstra算法（单源最短路径，BFS）**

Dijkstra算法原理：https://blog.csdn.net/yalishadaa/article/details/55827681
通俗解释dijkstra：https://www.zhihu.com/question/20630094/answer/758191548

**基本思想**

1. 通过Dijkstra计算图G中的最短路径时，需要**指定起点s**(即从顶点s开始计算)。
2. 此外，引进**两个集合S和U**。S的作用是记录已求出最短路径的顶点(以及相应的最短路径长度)，而U则是记录还未求出最短路径的顶点(以及该顶点到起点s的距离)。
3. 初始时，S中只有起点s；U中是除s之外的顶点，并且U中顶点的路径是”起点s到该顶点的路径”。然后，**从U中找出路径最短的顶点，并将其加入到S中**；接着，**更新U中的顶点和顶点对应的路径**。 然后，**再从U中找出路径最短的顶点，并将其加入到S中**；接着，更新U中的顶点和顶点对应的路径。 … 重复该操作，直到遍历完所有顶点。

**操作步骤**

1. 初始时，S只包含起点s；U包含除s外的其他顶点，且U中顶点的距离为”起点s到该顶点的距离”[例如，U中顶点v的距离为(s,v)的长度，然后s和v不相邻，则v的距离为∞]。
2. 从U中选出”距离最短的顶点k”，并将顶点k加入到S中；同时，从U中移除顶点k。
3. 更新U中各个顶点到起点s的距离。之所以更新U中顶点的距离，是由于上一步中确定了k是求出最短路径的顶点，从而可以利用k来更新其它顶点的距离；例如，(s,v)的距离可能大于(s,k)+(k,v)的距离。
4. 重复步骤(2)和(3)，直到遍历完所有顶点。

**实例**

<img src="数据结构与算法（Python语言实现）.assets/20191006112455385.jpg" alt="img"  />

**Python实现（邻接表、邻接矩阵）**

```Python
import heapq
import math

def init_distance(graph, s):
    distance = {s: 0}
    for vertex in graph:
        if vertex != s:
            distance[vertex] = math.inf
    return distance


def dijkstra1(graph, s):
    pqueue = []
    heapq.heappush(pqueue, (0, s))
    seen = set()
    parent = {s: None}
    distance = init_distance(graph, s)

    while len(pqueue) > 0:
        pair = heapq.heappop(pqueue)
        dist = pair[0]
        vertex = pair[1]
        seen.add(s)
        nodes = graph[vertex].keys()
        for w in nodes:
            if w not in seen:
                if dist + graph[vertex][w] < distance[w]:
                    heapq.heappush(pqueue, (dist + graph[vertex][w], w))
                    parent[w] = vertex
                    distance[w] = dist + graph[vertex][w]
    # return parent, distance


if __name__ == '__main__':
    graph_dict = {
        "A": {"B": 5, "C": 1},
        "B": {"A": 5, "C": 2, "D": 1},
        "C": {"A": 1, "B": 2, "D": 4, "E": 8},
        "D": {"B": 1, "C": 4, "E": 3, "F": 6},
        "E": {"C": 8, "D": 3},
        "F": {"D": 6},
    }

    parent_dict, distance_dict = dijkstra1(graph_dict, "A")
    print(parent_dict)
    print(distance_dict)
    
def dijkstra(start: int, mgraph: list) -> list:
    passed = [start]
    nopass = [x for x in range(len(mgraph)) if x != start]
    dis = mgraph[start]
    
    while len(nopass):
        idx = nopass[0]
        for i in nopass:
            if dis[i] < dis[idx]: idx = i

        nopass.remove(idx)
        passed.append(idx)

        for i in nopass:
            if dis[idx] + mgraph[idx][i] < dis[i]: dis[i] = dis[idx] + mgraph[idx][i]
    return dis

if __name__ == "__main__":
    inf = 10086
    mgraph = [[0, 1, 12, inf, inf, inf],
              [inf, 0, 9, 3, inf, inf],
              [inf, inf, 0, inf, 5, inf],
              [inf, inf, 4, 0, 13, 15],
              [inf, inf, inf ,inf, 0, 4],
              [inf, inf, inf, inf ,inf, 0]]

    dis = dijkstra(0, mgraph)
    print(dis)
```

**Python实现（优先级队列）**

```python
from ..ch09.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue

def shortest_path_lengths(g, src):
  """
  计算从源s到g的可达顶点的最短路径距离。

  图g可以是无向的或有向的，但必须加权以使边e.element（）返回每个边缘e的数字权重。

  返回字典，映射每一个从源可达的顶点v到它的最短路径距离d(s,v)。
  """
  d = {}                                        # d[v]是从s到v的上限
  cloud = {}                                    # 将可达的顶点v映射为其d[v]值
  pq = AdaptableHeapPriorityQueue()             # vertex v will have key d[v]
  pqlocator = {}                                # map from vertex to its pq locator

  #对于图的每个顶点v，将一个条目添加到优先级队列中，其中源的距离为0，所有其他源的距离为无限
  for v in g.vertices():
    if v is src:
      d[v] = 0
    else:
      d[v] = float('inf')                       # syntax for positive infinity
    pqlocator[v] = pq.add(d[v], v)              # save locator for future updates

  while not pq.is_empty():
    key, u = pq.remove_min()
    cloud[u] = key                              # its correct d[u] value
    del pqlocator[u]                            # u is no longer in pq
    for e in g.incident_edges(u):               # outgoing edges (u,v)
      v = e.opposite(u)
      if v not in cloud:
        # perform relaxation step on edge (u,v)
        wgt = e.element()
        if d[u] + wgt < d[v]:                   # better path to v?
          d[v] = d[u] + wgt                     # update the distance
          pq.update(pqlocator[v], d[v], v)      # update the pq entry

  return cloud    
```

- 性能

在Dijsktra算法中，我们有两种选择去实现有位置感知项的适应性强的优先队列：①堆实现$O((n+m)logn)$②未排序的序列实现$O(n^2)$。当边的数量m很小的时候($m<n^2/logn$)，选择堆实现，边的数量m很大的时候($m>n^2/logn$)选择序列实现。

> 已知有n个顶点m条边的有权图，每条边权值非负，Dijkstra算法计算从顶点s到所有其他顶点的距离时最好的情况是$O(n^2)$或者$O((n+m)logn)$。

#### 14.6.3	最短路径树O(n+m)

从源顶点s产生的所有最短路径的集合可以表示为最短路径树。这个路径形成了一个有根的树，因为如果从s到v的最短路径经过中间顶点u，它必须以从s到u的最短路径开始。

​																		$d[u]+w(u,v)=d[v]$

​                                                                 代码段14-14	重建最短路径

```python
def shortest_path_tree(g, s, d):
  """
  给定距离映射d，重建以顶点s为根的最短路径树。

  将树作为从每个可达顶点v（而不是s）到边e =（u，v）的映射图返回，该边e =（u，v）从树中其父u到达v。
  """
  tree = {}
  for v in d:
    if v is not s:
      for e in g.incident_edges(v, False):       # consider INCOMING edges
        u = e.opposite(v)
        wgt = e.element()
        if d[v] == d[u] + wgt:
          tree[v] = e                            # edge e is used to reach v
  return tree
```

### 14.7	最小生成树MST

最小生成树的两种方法（Kruskal和Prim算法）：https://blog.csdn.net/a2392008643/article/details/81781766
数据结构--最小生成树详解：https://blog.csdn.net/qq_35644234/article/details/59106779
最小生成树：https://www.jianshu.com/p/a5f0f46be8e2
prim&krus算法代码：https://www.jb51.net/article/154826.htm

​	已知一个无向的、有权重的图G，我们找到一棵树T，它包含G中所有顶点，并最小化总和

​																$w(T)=\sum\limits_{(u,v)inT}w(u,v)$

这样的包括连通图G的每个顶点的树被称为<u>生成树</u>，有最小总权重的生成树T被称为<u>最小生成树</u>。

> 构造最小生成树有很多算法，但是他们都是利用了最小生成树的同一种性质：MST性质（假设N=(V,{E})是一个连通网，U是顶点集V的一个非空子集，如果（u，v）是一条具有最小权值的边，其中u属于U，v属于V-U，则必定存在一颗包含边（u，v）的最小生成树）。

解决MST问题的两种经典算法：**Prim-Jarnik算法**和**Kruskal算法**。第一种算法从单个根节点生成MST，和Dijkstra算法的最短路径有很多相似的地方；第二种算法按照边的权重的非递减顺序考虑边来成群地“生成”MST。思路类似于DFS和BFS。

#### 14.7.1	Prim-jarnik算法(适用于边稠密的网，类似Dijkstra)

此算法可以称为==“加点法”==，**<u>每次迭代选择代价最小的边对应的点，加入到最小生成树中。算法从某一个顶点s开始，逐渐长大覆盖整个连通网的所有顶点。</u>**通过生成单个树直到跨越整个图来生成MST。

1. 图的所有顶点集合为$V$；令初始集合$U$={$s$},$v$=$V−U$={$a,b,c,...$};
2. 在两个集合$U$和$V-U$能够组成的边中，选择一条代价最小的边$(u_0,v_0)$，加入到最小生成树中，并把$v_0$并入到集合$U$中。
3. 重复上述步骤，直到最小生成树有n-1条边或者n个顶点为止。

![image-20210415174255902](数据结构与算法（Python语言实现）.assets/image-20210415174255902.png)

![img](数据结构与算法（Python语言实现）.assets/20160714161107576)

​															图14.7	Prim-jarnik算法步骤

- Python实现

```Python
import sys
    
def prim(primgraph,chararray):
    charlist = []
    charlist.append(chararray[0])
    mid = []    #mid[i]表示生成树集合中与点i最近的点的编号
    lowcost = []  #lowcost[i]表示生成树集合中与点i最近的点构成的边最小权值 ，-1表示i已经在生成树集合中
    lowcost.append(-1)
    mid.append(0)
    n = len(chararray)
    for i in range(1,n): #初始化mid数组和lowcost数组
        lowcost.append(primgraph[0][i])
        mid.append(0)
    sum = 0
    for _ in range(1,n): #插入n-1个结点
        minid = 0
        min = MAX
        for j in range(1,n):  #寻找每次插入生成树的权值最小的结点
            if(lowcost[j]!=-1 and lowcost[j]<min):
                minid = j
                min = lowcost[j]
        charlist.append(chararray[minid])
        print(chararray[mid[minid]]+'——'+chararray[minid]+'权值：'+str(lowcost[minid]))
        sum+=min
        lowcost[minid] = -1
        for j in range(1,n):  #更新插入结点后lowcost数组和mid数组值
            if(lowcost[j]!=-1 and lowcost[j]>primgraph[minid][j]):
                lowcost[j] = primgraph[minid][j]
                mid[j] = minid
                
    return  sum , charlist

if __name__=='__main__':
    MAX = sys.maxsize
    primgraph = [[MAX,  10, MAX, MAX, MAX,  11, MAX, MAX, MAX],
                 [10,  MAX,  18, MAX, MAX, MAX,  16, MAX,  12],
                 [MAX,  18, MAX,  22, MAX, MAX, MAX, MAX,   8],
                 [MAX, MAX,  22, MAX,  20, MAX, MAX,  16,  21],
                 [MAX, MAX, MAX,  20, MAX,  26,   7,  19, MAX],
                 [11,  MAX, MAX, MAX,  26, MAX,  17, MAX, MAX],
                 [MAX,  16, MAX, MAX,   7,  17, MAX,  19, MAX],
                 [MAX, MAX, MAX,  16,  19, MAX,  19, MAX, MAX],
                 [MAX,  12,   8,  21, MAX, MAX, MAX, MAX, MAX]]
    chararray = ['A','B','C','D','E','F','G','H','I']
    sum,charlist = prim(primgraph,chararray)
    print("sum="+str(sum))
    print("插入结点顺序："+str(charlist))
##################################写法二#############################    
def primToMST(adj,startPoint="A"):
    indexdict = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G"}
    citydict = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7}
    vnew=[startPoint]
    edge=[]
    sum=0
    #vnew
    edg=[] #element is cell, eg. (u,v)
    while len(vnew)<len(citydict):
        imin = (-1,float('Inf'))
        centerCity=""
        for city in vnew:
            cur = citydict[city]-1
            ws = adj[cur]
            for (i,w) in enumerate(ws):
                if indexdict[i+1] not in vnew and 0 < w and  w < imin[1]:
                    imin = (i+1,w)
                    centerCity=city
        vnew.append(indexdict[imin[0]]) #add the city with minimum weight
        edge.append((centerCity,indexdict[imin[0]]))
        sum+=imin[1]
    return sum,vnew,edge



sum,vnew,edges =primToMST([ [0,7,0,5,0,0,0],
                           [7,0,8,9,7,0,0],
                           [0,8,0,0,5,0,0],
                           [5,9,0,0,15,6,0],
                           [0,7,5,15,0,8,9],
                           [0,0,0,6,8,0,11],
                           [0,0,0,0,9,11,0]],startPoint="D")

print("weight sum: "+str(sum))
print("vertex:")
[print(city) for city in vnew]
print("edge: ")
[print("("+str(v)+","+str(u)+")")for (v,u) in edges]
```

​                                         代码段14-16	最小生成树问题的Prim算法的Python实现

```python
from ..ch09.pq import HeapPriorityQueue,AdaptableHeapPriorityQueue
from .partition import Partition

def MST_PrimJarnik(g):
  """
  计算加权图g的最小生成树。

  返回组成MST的边的无序列表。
  """
  d = {}                               # d[v] is bound on distance to tree
  tree = []                            # list of edges in spanning tree
  pq = AdaptableHeapPriorityQueue()   # d[v] maps to value (v, e=(u,v))
  pqlocator = {}                       # map from vertex to its pq locator

  # 对于图的每个顶点v，将一个条目添加到优先级队列中，其中源的距离为0，所有其他源的距离为无限
    if len(d) == 0:                                 # this is the first node
      d[v] = 0                                      # make it the root
    else:
      d[v] = float('inf')                           # positive infinity
    pqlocator[v] = pq.add(d[v], (v,None))

  while not pq.is_empty():
    key,value = pq.remove_min()
    u,edge = value                                  # unpack tuple from pq
    del pqlocator[u]                                # u is no longer in pq
    if edge is not None:
      tree.append(edge)                             # add edge to tree
    for link in g.incident_edges(u):
      v = link.opposite(u)
      if v in pqlocator:                            # thus v not yet in tree
        # see if edge (u,v) better connects v to the growing tree
        wgt = link.element()
        if wgt < d[v]:                              # better edge to v?
          d[v] = wgt                                # update the distance
          pq.update(pqlocator[v], d[v], (v, link))  # update the pq entry

  return tree
```

- 性能

基于堆的优先队列：$O((n+m)logn)$；基于连通图：$O(mlogn)$；基于未排序的列表作为优先队列：$O(n^2)$。

#### 14.7.2	Kruskal算法(O(mlogn)，适用于边稀疏的网，BFS)

此算法可以称为==“加边法”==，**<u>初始最小生成树边数为0，每迭代一次就选择一条满足条件的最小代价边，加入到最小生成树的边集合里。</u>** 维持集群森林，重复地合并集群对直到单个集群跨越整个图。

1. 把图中的所有边按代价从小到大排序； 
2. 把图中的n个顶点看成独立的n棵树组成的森林； 
3.  按权值从小到大选择边，所选的边连接的两个顶点$(u_i,v_i)$,应属于两颗不同的树，则成为最小生成树的一条边，并将这两颗树合并作为一颗树。 
4. 重复(3),直到所有顶点都在一颗树内或者有n-1条边为止。

![image-20210415220148939](数据结构与算法（Python语言实现）.assets/image-20210415220148939.png)

![img](数据结构与算法（Python语言实现）.assets/20160714144315409)

​															图14.8	Kruskal算法步骤

- Python实现

```Python
class Graph(object):
  def __init__(self, maps):
    self.maps = maps
    self.nodenum = self.get_nodenum()
    self.edgenum = self.get_edgenum()
  
  def get_nodenum(self):
    return len(self.maps)
  
  def get_edgenum(self):
    count = 0
    for i in range(self.nodenum):
      for j in range(i):
        if self.maps[i][j] > 0 and self.maps[i][j] < 9999:
          count += 1
    return count
  
  def kruskal(self):
    res = []
    if self.nodenum <= 0 or self.edgenum < self.nodenum-1:
      return res
    edge_list = []
    for i in range(self.nodenum):
      for j in range(i,self.nodenum):
        if self.maps[i][j] < 9999:
          edge_list.append([i, j, self.maps[i][j]])#按[begin, end, weight]形式加入
    edge_list.sort(key=lambda a:a[2])#已经排好序的边集合
     
    group = [[i] for i in range(self.nodenum)]
    for edge in edge_list:
      for i in range(len(group)):
        if edge[0] in group[i]:
          m = i
        if edge[1] in group[i]:
          n = i
      if m != n:
        res.append(edge)
        group[m] = group[m] + group[n]
        group[n] = []
    return res
```

 									代码段14-18	最小生成树问题的Kruskal算法的Python实现

```python
from ..ch09.pq import HeapPriorityQueue,AdaptableHeapPriorityQueue
from .partition import Partition #管理集群分区的Partition类

def MST_Kruskal(g):
  """
  使用Kruskal算法计算图的最小生成树。

   返回组成MST的边的列表。

   图的边的元素为权重，e.elemnet()。
  """
  tree = []                   # list of edges in spanning tree
  pq = HeapPriorityQueue()    # edges in G, with weights as key -->(e.element(),e)
  forest = Partition()        # keeps track of forest clusters
  position = {}               # map each node to its Partition entry

  for v in g.vertices():
    position[v] = forest.make_group(v) #每个顶点建集群。make_group()：创建一个包含新元素x的不相交的组并且返回存储x的位置。

  for e in g.edges():
    pq.add(e.element(), e)    # edge's element is assumed to be its weight

  size = g.vertex_count()
  while len(tree) != size - 1 and not pq.is_empty():
    # tree not spanning and unprocessed edges remain
    weight,edge = pq.remove_min()
    u,v = edge.endpoints()
    a = forest.find(position[u]) #返回包含位置u的组的领导的位置
    b = forest.find(position[v]) #返回包含位置v的组的领导的位置
    if a != b:
      tree.append(edge)
      forest.union(a,b) #合并包含位置a和b的组

  return tree
```

**14.7.3	查并集**

```
看书14.7.3节
```

 									代码段14-19	查并集Partition类的Python实现

```python
class Partition:
  """Union-find structure for maintaining disjoint sets."""
  
  #------------------------- nested Position class -------------------------
  class Position:
    __slots__ = '_container', '_element', '_size', '_parent'

    def __init__(self, container, e):
      """Create a new position that is the leader of its own group."""
      self._container = container         # reference to Partition instance
      self._element = e
      self._size = 1
      self._parent = self                 # convention for a group leader

    def element(self):
      """Return element stored at this position."""
      return self._element

  #------------------------- nonpublic utility -------------------------
  def _validate(self, p):
    if not isinstance(p, self.Position):
      raise TypeError('p must be proper Position type')
    if p._container is not self:
      raise ValueError('p does not belong to this container')
    
  #------------------------- public Partition methods -------------------------
  def make_group(self, e):
    """Makes a new group containing element e, and returns its Position."""
    return self.Position(self, e)

  def find(self, p):
    """Finds the group containging p and return the position of its leader."""
    self._validate(p)
    if p._parent != p:
      p._parent = self.find(p._parent)    # overwrite p._parent after recursion
    return p._parent
    
  def union(self, p, q):
    """Merges the groups containg elements p and q (if distinct)."""
    a = self.find(p)
    b = self.find(q)
    if a is not b:                        # only merge if different groups
      if a._size > b._size:
        b._parent = a
        a._size += b._size
      else:
        a._parent = b
        b._size += a._size
```

## 附录A 字符串

**搜索子串**

| 调用语法          | 描述                                      |
| ----------------- | ----------------------------------------- |
| s.count(pattern)  | 返回与pattern不重叠的匹配项数目           |
| s.find(pattern)   | 返回最左边以pattern开始的索引，否则返回-1 |
| s.index(pattern)  | 同上                                      |
| s.rfind(pattern)  | 返回最右边以pattern开始的索引，否则返回-1 |
| s.rindex(pattern) | 同上                                      |

**构建相关字符串**

| 调用语法           | 描述                                             |
| ------------------ | ------------------------------------------------ |
| s.replace(old,new) | 返回一用新匹配项替代所有旧匹配项的s的备份        |
| s.capitalize()     | 返回s一个拷贝，字符串s中首字符大写               |
| s.upper()          | 返回s一个拷贝，字符串s所有字符大写               |
| s.lower()          | 返回s一个拷贝，字符串s所有字符小写               |
| s.center(width)    | 返回s一个拷贝，中间用空格填充相应的宽度（width） |
| s.ljust(width)     | 返回s一个拷贝，结尾用空格填充相应的宽度（width） |
| s.rjust(width)     | 返回s一个拷贝，开头用空格填充相应的宽度（width） |
| s.zfill(width)     | 返回s一个拷贝，开头用0填充相应的宽度（width）    |
| s.strip()          | 返回s一个拷贝，删除开头和结尾无用的空白          |
| s.lstrip()         | 返回s一个拷贝，删除开头无用的空白                |
| s.rstrip()         | 返回s一个拷贝，删除结尾无用的空白                |

**测试布尔条件**

| 调用语法             | 描述                                                         |
| -------------------- | ------------------------------------------------------------ |
| s.startwith(pattern) | 如果pattern是字符串s的前缀，返回True                         |
| s.endswith(pattern)  | 如果pattern是字符串s的后缀，返回True                         |
| s.isspace()          | 如果非空字符串的所有字符是空白，返回True                     |
| s.isalpha()          | 如果非空字符串的所有字符是字母，返回True                     |
| s.islower()          | 如果所有字母都是小写的，返回True                             |
| s.isupper()          | 如果所有字母都是大写的，返回True                             |
| s.isdigit()          | 如果非空字符串的所有字符都是在0~9之间，返回True              |
| s.isdecimal()        | 如果非空字符串的所有字符代表是数字0~9包括Unicode字符，返回True |
| s.isnumeric()        | 如果非空字符串的所有字符代表是数字包括Unicode字符(0~9、等价物、分数字符)，返回True |
| s.isalnum()          | 如果非空字符串的所有字符都是字母或数字，返回True             |

**拆分和连接字符串**

| 调用语法            | 描述                                                         |
| ------------------- | ------------------------------------------------------------ |
| sep.join(strings)   | 返回给定字符串组成的序列，将sep(‘ ’)作为分隔符插入每对序列之间。 |
| s.splitlines()      | 返回字符串s的子串列表，以换行符分割。                        |
| s.split(sep,count)  | 返回字符串s的子串列表，以sep（默认空格）作为分隔符分隔count（默认所有）次。 |
| s.rsplit(sep,count) | 类似split(),使用最右边出现的sep                              |
| s.partition(sep)    | 使用最左边出现的sep让s=head+sep+tail,返回（head,sep,tail）,否则返回（s,”,”） |
| s.rpartition(sep)   | 使用最右边出现的sep让s=head+sep+tail,返回（head,sep,tail）,否则返回（s,”,”） |

