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

def topological_sort(g):
  """
  以拓扑顺序返回有向无环图g的顶点列表。

  如果图g有一个循环，则结果将是不完整的。
  """
  topo = []             # a list of vertices placed in topological order
  ready = []            # list of vertices that have no remaining constraints
  incount = {}          # keep track of in-degree for each vertex
  
  ###############计算所有顶点入度，将起始顶点加入ready列表###############
  for u in g.vertices():
    incount[u] = g.degree(u, False)  # parameter requests incoming degree
    if incount[u] == 0:              # if u has no incoming edges,
      ready.append(u)                # it is free of constraints
  ###############弹出起始顶点，加入起始顶点###############
  while len(ready) > 0:
    u = ready.pop()                  # u is free of constraints
    topo.append(u)                   # add u to the topological order
    ###############用顶点u找顶点v###############
    for e in g.incident_edges(u):    # consider all outgoing neighbors of u
      v = e.opposite(u)
      ###############顶点v入度-1###############
      incount[v] -= 1                # v has one less constraint without u
      if incount[v] == 0:
        ready.append(v)
  return topo

if __name__ == '__main__':
  from graph_examples import figure_14_12 as example
  g = example()
  print("Number of vertices is", g.vertex_count())
  print("Number of edges is", g.edge_count())
  topo = topological_sort(g)
  print("Topo order", [str(v) for v in topo])
