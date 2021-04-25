# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from ..ch09.pq import HeapPriorityQueue,AdaptableHeapPriorityQueue
from .partition import Partition  #管理集群分区的Partition类

def MST_PrimJarnik(g):
  """
  计算加权图g的最小生成树。

  返回组成MST的边的列表（以任意顺序）。
  """
  d = {}                               # d[v] is bound on distance to tree
  tree = []                            # list of edges in spanning tree
  pq = AdaptableHeapPriorityQueue()   # d[v] maps to value (v, e=(u,v))
  pqlocator = {}                       # map from vertex to its pq locator

  # 对于图的每个顶点v，将一个条目添加到优先级队列中，其中源的距离为0，所有其他源的距离为无限
  for v in g.vertices():
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

def MST_Kruskal(g):
  """
  使用Kruskal算法计算图的最小生成树。

   返回组成MST的边的列表。

   图的边的元素为权重，e.elemnet()。
  """
  tree = []                   # list of edges in spanning tree
  pq = HeapPriorityQueue()    # entries are edges in G, with weights as key
  forest = Partition()        # keeps track of forest clusters
  position = {}               # map each node to its Partition entry

  for v in g.vertices():
    position[v] = forest.make_group(v) #创建一个包含新元素x的不相交的组并且返回存储x的位置

  for e in g.edges():
    pq.add(e.element(), e)    # edge's element is assumed to be its weight

  size = g.vertex_count()
  while len(tree) != size - 1 and not pq.is_empty():
    # tree not spanning and unprocessed edges remain
    weight,edge = pq.remove_min()
    u,v = edge.endpoints()
    a = forest.find(position[u])  #返回包含位置u的组的领导的位置
    b = forest.find(position[v])  #返回包含位置v的组的领导的位置
    if a != b:
      tree.append(edge)
      forest.union(a,b)           #合并包含位置a和b的组

  return tree
