#通常版

#グラフの構築
n=int(input())
m = [[-1 for i in range(n)] for j in range(n)]
for i in range(n): #隣接の辺のコストを入力
  nums = list(map(int, input().split()))
  for j in range(n):
    m[i][j] = nums[j]

#距離と訪問リスト
d=[0]+[10**9]*(n-1)
visited=[0]*n

#繰り返し
while 1:
  u=-1
  for i in range(n):
    if not visited[i] and (u<0 or d[i]<d[u]): #全ての頂点についてその隣接辺を探索→①へ
      u = i
  if u < 0:
    break
  visited[u]=1
  for v in range(n):
    if not visited[v] and m[u][v]!=-1:#①ここでさっき選んだ頂点の全ての隣接辺を探索
      if m[u][v]<d[v]:
        d[v]=m[u][v]

print(sum(d))


#二分ヒープ
from heapq import heappush, heappop, heapify

N = int(input())
edges = [[] for i in range(N)]
for v in range(N):
    for w, c in enumerate(map(int, input().split())):
        if c != -1:
            edges[v].append((w, c))

visited = [0]*N
que = [(c, w) for w, c in edges[0]]
visited[0] = 1
heapify(que)

d=[0]+[10**9]*(N-1)

#左がコスト
ans = 0
while que:
    c, u = heappop(que)
    if visited[u]:
        continue
    visited[u] = 1
    d[u]=c
    for v, c in edges[u]:
        if visited[v]:
          continue
        heappush(que, (c, v))
print(sum(d))


