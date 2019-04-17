#通常

def dijkstra(n):
  inf = 10**7+7
  dist = [0]+[inf]*(n-1)
  visited = [False]*n
  while not all (visited):
    dmin = inf
    for i, (d,v) in enumerate(zip(dist,visited)):
      if dmin > d and not v:
        dmin, u = d, i
    visited[u] = True
    for(v,c) in edge[u]:
      if dist[v] > dist[u]+ c:
        dist[v] = dist[u]+c
  return dist

n = int(input())
edge =[[]]*n
for _ in range(n):
  l = list(map(int, input().split()))
  edge[l[0]]=(e for e in zip(l[2::2], l[3::2]))
for i,c in enumerate(dijkstra(n)):
  print(i,c)




#heap
import heapq

n = int(input())
d = [0]+[inf]*(n-1)
g = []
q = []

for i in range(n):
  heapq.heappush(q,(d[i],i))
  inp = list(map(int,input().split()))
  tmp = []
  for j in range(inp[1]):

while q:
  q_pop = heapq.heappop(q)
  i = q_pop[1]
  if q_pop[0] > 100*0100000:
    continue
  for node in g[i]:
    d_tmp = d[i]+node[1]
    if d_tmp < d[node[0]]
    d[node[0]] = d_tmp
    heapq.heappush(q,(d_tmp,node[0]))
for i in range(n):
  print(i,d[oi])
