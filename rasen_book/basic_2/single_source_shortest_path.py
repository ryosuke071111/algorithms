#最短経路（重み付きグラフにおいてある点の組の経路の中で編の総和が最小のパス）

def Dijkestra(G, n):
  d = [200000000]*n
  d[0] = 0               #0からの移動コスト
  isVisited = [False]*n
  C = []

  for i in range(n):
    C.append(i)           #とりあえずCにnの値を入れていく[0,1,2,...n]（=頂点番号）

  while len(C) != 0:
    u = C[0]              #uに頂点番号を代入して今回の主人公にしていく
    for i in range(1, len(C)):
      if d[u] > d[C[i]]:  #0から主人公へのコストが、1~頂点数のコストより高ければ
        u = C[i]          #主人公をその低いコストのものへ変更する
    C.remove(u)           #Cから主人公を排除する（処理中だから処理候補のまちから削除）
    for i in range(len(G[u])):  #主人公の隣接する辺の数の分
      if G[u][i] == -1:         #コストの値が-1だったら続ける
        continue
      elif d[i] > d[u] + G[u][i]: #デフォルト値より、入力されたコストのが低かったら（前の回で更新されたコストよりもさらに低い場合も含む）
        d[i] = d[u]+G[u][i]       #そのコストを代入する
        isVisited[i] = u

  for i in range(n):
    print(i, d[i])               #頂点番号と、0からの辺のコストを出力


n = int(input())
G = [] #全頂点における隣接する頂点の辺のコストの入ったリスト
for i in range(n):
  a = [] #隣接する頂点の辺のコスト
  ele = list(map(int, input().split()))
  k = ele[1]         #出次数
  t = ele[2:]
  v = c = []
  for j in range(k):  #出次数の数だけ下記内容を更新
    v = v+[t[2*j]]    #隣接する頂点の値を入れるリスト
    c = c+[t[2*j+1]]  #隣接する頂点との辺のコストを入れるリスト

  for j in range(n):
    if j in v:                #隣接する頂点の値があったら
      a.append(c[v.index(j)]) #その頂点の値のリストインデックスのcリストの中の値（=辺のコスト）
    else:
      a.append(-1)            #辺が隣接していない時もあるからそんな時は-1を入れておく
  G.append(a) #全頂点における隣接する頂点の辺のコストの入ったリスト
Dijkestra(G, n)


#計算量O(V^2)：頂点に対して隣接頂点を調べるのでV^2
