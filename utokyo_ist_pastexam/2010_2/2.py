f=open('graph2.txt')
f=f.read().strip('\n').split()
f=list(map(lambda x:x.split('->'),f))
indegs=[[]for i in range(10000)]
outdegs=[[]for i in range(10000)]
t1=0
cnt_edges=0

def dfs(u):
  global flag2
  visited[u]=1
  for v in outdegs[u]:
    if visited[v]==0:
      dfs(v)
  return sum(visited)

for i in f:
  visited=[0]*10000
  u,v=i[0],int(i[1])
  if u[0]=="!":
    try:
      u=int(u[1:])
      outdegs[u].remove(v)
      indegs[v].remove(u)
    except ValueError:
      pass
  else:
    u=int(u)
    outdegs[u].append(v)
    indegs[v].append(u)
    ans=dfs(0)
    if ans>=1000 :
      print('|R(t)|>=1000となった時刻:',t1)
  t1+=1


#有効辺の数数える
for i in outdegs:
  cnt_edges+=len(i)
print('有向辺の数:',cnt_edges)

#ルート集合の大きさ
visited=[0]*10000
ans=dfs(0)
print('ルート集合の大きさ:',ans)

