
n,m=map(int,input().split())

edges=[[] for i in range(n)]

for i in range(m):
  s,t = map(int,input().split())
  edges[s-1].append(t-1)
  edges[t-1].append(s-1)

cnt =[0]

def dfs(V,s):
  V[s]=1
  if sum(V)==n:
    cnt[0]+=1
  else:
    for adj in edges[s]:
      if V[adj] == 0:
        dfs(V[:adj] + [1] + V[adj + 1:], adj)
  print(V)
dfs([0] * n, 0)
print(cnt[0])
# ---------------------------------------------------

#これでもいける（自分で考えたやつ）
n,m=map(int,input().split())

edges=[[] for i in range(n)]

for i in range(m):
  s,t = map(int,input().split())
  edges[s-1].append(t-1)
  edges[t-1].append(s-1)

cnt =0

V=[0]*n

def dfs(V,s):
  global cnt
  V=V[:]
  V[s]=1
  if sum(V)==n:
    cnt+=1
  else:
    for v in edges[s]:
      if V[v]==0:
        dfs(V,v)
dfs(V,0)
print(cnt)


