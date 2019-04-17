#一つの点から全ての経路までの最短の距離≒
#ある単一点までの最短経路ではない（その中で任意の距離を求めるから結局そうなる）
#有向辺だから単に二次元配列にコスト格納するとprim的になる

#dijkstra（通常版）
V,e,r=map(int,input().split())
d=[float('inf')]*V
d[r]=0
edges=[[] for i in range(V)]
visited=[False]*V

for i in range(e):
  s,t,c=map(int,input().split())
  edges[s].append([t,c])

#未探索ノードのうち距離が最小のものを探す（ターゲット）
while not all (visited):
  dmin=float('inf')
  for i in range(V):
    #未訪問の中で最小のコストの頂点を探索
    if dmin >= d[i] and not visited[i]:
      dmin=d[i]
      u=i
  visited[u]=True
  #ターゲットから伸びる辺を探索
  for v,c in edges[u]:
    if d[v] > d[u]+c:
      d[v]=d[u]+c

for i in d:
  if i == float('inf'):
    print('INF')
  else:
    print(i)




# #dijkstra(ヒープ版)
from heapq import heappush, heappop
v,e,r = map(int,input().split())
edges=[[] for i in range(v)]
d = [float('INF')]*v

for i in range(e):
  s,t,c = map(int,input().split())
  edges[s].append([t,c])

que = []
heappush(que,(r,0))
d[r] = 0

while que: #O(V)
  u, du = heappop(que) #O(logV)
  for v, c in edges[u]:
    if d[v] > du+c:
      d[v] = du+c
      heappush(que,(v,d[v]))#O(logV)
for i in d:
  if i == float('inf'):
    print('INF')
  else:
    print(i)
