##ネットワーク構築
vs,e = map(int,input().split())
edges = [[0]*vs for j in range(vs)] #隣接行列

for i in range(e):
  u,v,c = map(int,input().split())
  edges[u][v] = c                   #隣接行列に容量を追加していく
print(edges)

##増加可能経路を探す（sから経路をたどってtまで行く）
def bfs(s,t,edges):
  vs = len(edges) #隣接行列の縦の長さ
  visited = [False]*vs #頂点はvs個
  visited[s] = True    #bfsの始点をtrueに
  que = [s]
  parents = [-1]*vs
  while que:
    u = que.pop(0)   #queの先頭から主人公を取り出す
    if u == t:       #主人公が終点なら親を返す sからtまで増加可能経路をたどっていければ
      return parents
    for v in range(vs): #頂点v分forを回す
      if not visited[v] and edges[u][v] >0: #未訪問かつ容量があれば**（ここで経路が唯一になる）***
        parents[v] = u  #vの親に始主人公sを入れる
        visited[v] = True
        que.append(v)
  return None


inf = float('inf')
ans = 0
cnt=0
##残余ネットワークにsからtへの道pが存在する間
while True:
  parents = bfs(0,vs-1,edges) #bfsでsからtに向かう増加可能経路を探す
  print('parents',parents)
  if parents is None:
    break
  v = vs-1 #tの場所
  f = inf
  while parents[v] != -1: #tからsに戻る道がある間
    u = parents[v]        #vへ向かう頂点をuとする
    f = min(f,edges[u][v]) #フローの量（残余余量の最小値を更新して行く）
    v = u #tからsまで戻るようにuをvに代入（残余余量の最小値を更新して行く）
  ans += f
  v = vs - 1

 #残余ネットワークで通る分容量から差し引く
  while parents[v] != -1:
    u = parents[v]
    edges[u][v] -=f     #逆辺分を押し戻す
    edges[v][u] +=f     #逆辺分を追加
    print("updated_edges",edges)
    v = u
print(ans)
print('実行回数',cnt)









