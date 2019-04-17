# n,m=map(int,input().split())
# edges=[[]for i in range(n)]
# visited=[0]*(n)
# for i in range(n+m-1):
#   a,b=map(int,input().split())
#   edges[a-1].append(b-1)
# print(edges)
# ans=visited
# def dfs(visited,i):
#   global ans
#   visited=visited[:]
#   visited[i]=1
#   for v in edges[i]:
#     if visited[v]==0:
#       dfs(visited,v)
#   if sum(visited)>sum(ans):
#     ans=visited
#   return visited

# tmp=0
# for i in range(len(edges)):
#   dfs(visited,i)
# for i in range(len(ans)):
#   if ans[i]==1:
#     print(i)

n,m=map(int,input().split())
src = [tuple(map(lambda x:int(x)-1,input().split())) for i in range(n-1+m)]
indeg_n=[0]*n
indeg=[[]for i in range(n)]
outdeg=[[]for i in range(n)]
for a,b in src:
  indeg_n[b]+=1
  indeg[b].append(a)
  outdeg[a].append(b)
root=indeg_n.index(0)
print('indeg_n',indeg_n)
toposo=[]
stack=[root]

while stack:
  v=stack.pop()
  toposo.append(v)
  for to in outdeg[v]:
    indeg_n[to]-=1
    if indeg_n[to]==0:
      stack.append(to)
order=[-1]*n
print(toposo)
for i,v in enumerate(toposo):
  order[v]=i
ans=[-1]*n
ans[root]=0
for ti in range(1,n):
  v=toposo[ti]
  maxo=max(order[p] for p in indeg[v])
  ans[v]=toposo[maxo]+1
print(*ans,sep='\n')
