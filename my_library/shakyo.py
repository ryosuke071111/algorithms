vs,e=map(int,input().split())
edges=[[0]*vs for j in range(vs)]

for i in range(e):
  u,v,c=map(int,input().split())
  edges[u][v]=c

def bfs(s,t,edges):
  vs=len(edges)
  visited=[False]*vs
  visited[s]=True
  que=[s]
  parents=[-1]*vs
  while que:
    u = que.pop(0)
    if u == t:
      return parents
    for v in range(vs):
      if not visited[v] and edges[u][v]>0:
        parents[v]=u
        visited[v]=True
        que.append(v)
  return None


#残余ネットワークがある間
while True:
  parents=bfs(0,vs-1,edges)
  if parents is None:
    break
  v=vs-1
  f=inf
  while parents[v]!=-1:
    u=parents[v]
    f=min(f,edges[u][v])
    v=u
  ans+=f
  v=vs-1





#増加可能経路を探す
#残余ネットワークが残っている間
#増加可能経路分残余ネットワークを変更
