#お手本

from scipy.sparse.csgraph import dijkstra

n=int(input())
a,b=map(int,input().split())
m=int(input())

mod=10**9+7
edges=[[]for i in range(n+1)]
for i in range(m):
  x,y=map(int,input().split())
  edges[x].append(y)
  edges[y].append(x)

cost=mod
count=0
visited=[0]*(n+1)

def dfs(u,visited,tmp):
  global cost
  global count
  tmp=tmp
  visited=visited[:]
  if tmp>cost:
    return
  if u!=a:
    visited[u] = 1
    tmp+=1
  if visited[b]==1:
    if tmp < cost:
      cost = tmp
      count=1
    elif tmp == cost:
      count+=1
    return count
  for  v in edges[u]:
    if visited[v]!=1:
      dfs(v,visited,tmp)

dfs(a,visited,0)
print(count%mod)


