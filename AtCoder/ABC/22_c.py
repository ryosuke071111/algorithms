# #18:16-
from itertools import combinations
from scipy.sparse.csgraph import floyd_warshall as wf

n,m=map(int,input().split())
inf=float('inf')
edges=[[inf]*n for j in range(n)]
for i in range(n):
  edges[i][i]=0
s=[]
for i in range(m):
  u,v,l=map(int,input().split())
  if u==1:
    s.append((v-1,l))
  elif v==1:
    s.append((u-1,l))
  else:
    edges[u-1][v-1]=l
    edges[v-1][u-1]=l

#全点対最短経路を求める
dist=wf(edges,directed=False)
ans=inf

#0を始点とした時の入次/出次頂点を選択
for u,v in combinations(s,2):
  d=dist[u[0]][v[0]] #選んだ2つの間を移動するコスト
  if d!= inf:
    ans=min(ans,u[1]+v[1]+int(d)) #0から選んだ二つへ移動するコスト
if ans==inf:
  print(-1)
else:
  print(ans)

