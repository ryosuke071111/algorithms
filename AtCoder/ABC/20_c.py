from collections import _heapq
h,w,t=map(int,input().split())
area=[[] for i in range(h)]
for i in range(h):
  area[i].append(input())

heap=heap()
edges=[[] for i in range()]
d=[]

u = heappop()
for e in edges[u]:
  if d[v] > d[u] + edges[u][v]
  d[v]=d[u] + edges[u][v]
  heappush(heap,u)

