n,m=map(int,input().split())
edges=[[0]*n for i in range(n)]
for i in range(m):
  a,b=map(int,input().split())
  edges[a-1].append(b-1)
  edges[b-1].append(a-1)

visited=[False]*n
cnt=0

def dfs(u,visited):
  global cnt
  visited=visited[:]
  visited[u]=True
  if all(visited):
    cnt+=1
    return
  for v in edges[u]:
    if not visited[v]:
      dfs(v,visited)
  return False

dfs(0,visited)
print(cnt)
