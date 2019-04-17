n = int(input())
m = [[-1 for i in range(n)] for j in range(n)] #お隣さんへのコストを保存（この中から最小を探す）

v = set()
v.add(0)

for i in range(n): #隣接の辺のコストを入力
  nums = list(map(int, input().split()))
  for j in range(n):
    m[i][j] = nums[j]


def prim_mst(n):
  isVisited = [False] * n
  d = [0] + [2001] * (n-1)      #TとV-Tのを繋ぐ最小辺の重みを格納する

  while  True:
    mincost = 2001
    for i in range(n):
      if not (isVisited[i]) and d[i] < mincost:
        mincost = d[i]
        u = i
    isVisited[u] = True


    if mincost == 2001:        #mincostが2001になったら繰り返し作業終了
      break

    for v in range (n):
      if (not isVisited[v]) and (m[u][v] != -1):
        if m[u][v] < d[v]:
          d[v] = m[u][v]
  print(sum(d))

prim_mst(n)


