n = int(input())
edges = [[] for i in range(n)]

for i in range(n-1):
  s, t, w = map(int, input().split())
  edges[s].append((t, w)) #(目的の頂点、コスト)
  edges[t].append((s, w)) #(目的の頂点、コスト)

from collections import deque
def bfs(s):
  dist = [None]*n
  que = deque([s])
  dist[s] = 0 #自分への距離は0にする
  while que:
    v = que.popleft()
    d = dist[v]
    for w, c in edges[v]: #自分の隣接頂点までのコストを調べる
      if dist[w] is not None: #すでに調査済みの場合は逆ダイクストラ現象になるのでスキップ
        continue
      dist[w] = d + c     #調査済みでな頂点があれば自分までのコスト+目的地面までのコスト
      que.append(w)       #目的地の先も調べてみる

  d = max(dist)
  return dist.index(d), d

u, _ = bfs(0)
v, d = bfs(u)

print(d)

#continueを使うとそれ以降の処理が実行されずに飛ばす
