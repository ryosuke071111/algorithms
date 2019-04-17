f=open('graph2.txt')
f=f.read().strip('\n').split()
f=list(map(lambda x:x.split('->'),f))
indegs=[[]for i in range(10000)]
outdegs=[[]for i in range(10000)]
t1=0
cnt_edges=0
vs=set([])

def dfs(u):
  global flag2
  visited[u]=1
  for v in outdegs[u]:
    if visited[v]==0:
      dfs(v)
  return visited

#グラフの作成
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
    routes=[]
    vs.add(u)
    vs.add(v)
  #ルート集合のindexを作成
  for i,v in enumerate(ans):
    if v==1:
      routes.append(i)
  for i in vs.copy():
    if i not in routes:
      vs.remove(i)
  for i in range(len(outdegs)):
    if i not in routes:
      outdegs[i]=[]
  for i in range(len(indegs)):
    if i not in routes:
      indegs[i]=[]

  t1+=1


#有効辺の数数える
for i in outdegs:
  cnt_edges+=len(i)
print('有向辺の数:',cnt_edges)

#頂点の数を数える
print("頂点の数:",len(vs))

