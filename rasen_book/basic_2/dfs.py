def dfs(v, cnt):
  D[v] = cnt          #訪問中リストに訪問中の印をつける
  cnt += 1            #初期状態の-1から訪問中の1に変更
  for c in edge[v]:   #対象ノードの隣接ノードについて
    if D[c] == -1:    #訪問中のノードに対する辺がまだ未訪問なら
      cnt = dfs(c, cnt)#訪問を開始
  F[v] = cnt
  cnt += 1
  return cnt

N = int(input())
edge = [[] for _ in range(N)] #隣接行列
for _ in range(N):
  u, _, *v = map(lambda x:int(x)-1, input().split()) #*vはリストではなくタプルで受け取る。複数標準入力に対して複数変数を設定した場合には左から一つずつ受け取ることになる。
  edge[u] = sorted(v)

D, F = [-1] * N, [-1] * N #D：訪問中のリスト、#訪問済みのリスト
c = 1
for i in range(N):
  if D[i] == -1: #初期状態の印
    c = dfs(i, c)
for i, (d, f) in enumerate(zip(D, F)):
  print(i + 1, d, f)

