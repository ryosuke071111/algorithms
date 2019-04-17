from collections import deque

n = int(input())                #エッジの個数
edge = [[] for _ in range(n)]   #エッジの隣接リスト（お隣さんを格納する）

for _ in range(n):
  u, _, *v = map(lambda x: int(x)-1, input().split())
  edge[u] = sorted(v)           #入力された隣接頂点をお隣さんリストに格納

dist = [-1] * n                #始点から各頂点iまでの距離を測るリスト
dist[0] = 0                    #0番目のエッジの距離
Q = deque([0])                 #次に訪問すべきエッジを記録するキュー

while len(Q):
  v = Q.popleft()             #vに次に訪問するエッジを代入（v=自分）
  for c in edge[v]:           #v(自分)のお隣さんの数の値を辿っていき（幅探索の実行（本質））
    if dist[c] == -1:         #もしお隣さんの距離が-1になっていたら
      dist[c] = dist[v] + 1   #お隣さんの距離=自分の距離+1にする
      Q.append(c)             #次に訪問すべきキューにお隣さんを代入

for i, d in enumerate(dist):
  print(i+1, d)














