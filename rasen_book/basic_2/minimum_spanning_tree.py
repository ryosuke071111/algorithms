#最小全域木（グラフの全域木のなかで編の重みの総和が最小のもの）

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

    #0から順に訪問する
    for i in range(n):
      if (not isVisited[i]) and(d[i] < mincost):
        mincost = d[i]
        print('mincostが変更された！！', mincost)
        u = i
    print('for i in range(n)のループが終わった\n')

    if mincost == 2001:        #mincostが2001になったら繰り返し作業終了
      break

    isVisited[u] = True        #すでに訪れた場合にはTrueを代入する（コスト更新を終了）
    print("isVisited is", isVisited)

    #u（現時点での頂点）のお隣さんに対しての辺のコストを求める（uが今の頂点の値）
    for v in range(n):
      if(not isVisited[v]) and (m[u][v] != -1): #-1でなく何かしらの辺の重みがあり
        if m[u][v] < d[v]:                      #隣接リストによるとその辺のコストのが小さかったら
          d[v] = m[u][v]                        #その重みを最小辺リストに追加しよう
          print("i", i, " u:", u, " v:", v)
          print("d is",d)
          print( "d[v] is",d[v])
    print('for v in range(n)のループが終わった\n')

  print(sum(d))

prim_mst(n)


#計算量O(V^2)：V'へのコストが最小の辺の探索をV個分行うので。
















