f=open('graph1.txt')
f=f.read().strip('\n').split()
f=list(map(lambda x:x.split('->'),f))
indegs=[[]for i in range(10000)]
outdegs=[[]for i in range(10000)]
vs=set([])
t0=0
flag0=False
t1=0
flag1=False
flag2=False

def dfs(u):
  global flag2
  visited[u]=1
  for v in outdegs[u]:
    if v==0 and flag2==False:
      print("v0がサイクルの一部となる時刻:",t1)
      flag2=True
    if visited[v]==0:
      dfs(v)
  return sum(visited)

for i in f:
  visited=[0]*10000
  u,v=int(i[0]),int(i[1])
  outdegs[u].append(v)
  indegs[v].append(u)
  if len(vs)>=1000 and flag0==False:
    print('|V(t)|>=1000となった時刻:',t0)
    flag0=True
  if flag1==False or flag2==False:
    ans=dfs(0)
    if ans>=1000 and flag1==False:
      print('|R(t)|>=1000となった時刻:',t1)
      flag1=True
  t0+=1
  t1+=1


cnt_out=0
max_out=0
for i in range(len(outdegs)):
  if len(outdegs[i])>cnt_out:
    cnt_out=len(outdegs[i])
    max_out=i
cnt_in=0
max_in=0
for i in range(len(indegs)):
  if len(indegs[i])>cnt_in:
    cnt_in=len(indegs[i])
    max_in=i
print("最大の出次数の頂点番号:",max_out,"出次数:",cnt_out)
print("最大の入次数の頂点番号:",max_in,"入次数:",cnt_in)
print("頂点の個数:",len(vs))
