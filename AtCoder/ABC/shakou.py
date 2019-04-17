def dfs(u):
  global graph
  global zahyou

  #調べ始める地点の距離をグローバルの自分の座標にする
  start=zahyou[u]
  #次のノードまでの距離を調査
  for next,d in graph[u]:
    #まだ次のノードまでの距離が調査されてないなら次ノードまでの距離を調べる
    if zahyou[next]==None:
      zahyou[next] = start + d
      if not dfs(next):
        return False
    #調査されているなら矛盾がないかを調べる
    else:
      if start + d != zahyou[next]:
        return False
  return False
n,m=map(int,input().split())
graph=[[] for _ in range(n)]

def dfs(u):
  global graph
  global zahyou
  start = zahyou[u]
  for w,d in graph[u]:
    if zahyou[w] == None:
      zahyou[w] == start + d
      if not dfs(w):
        return False
    else:
      if zahyou[w] != start + d:
        return False
  return False


zahyou = [None]*n
for i in range(m):
  l,r,d=map(int,input().split())
  graph[l-1].append((r-1,d))
  graph[r-1].append((l-1,-1*d))

flag=True
#基本フラグをnoにしていく姿勢
#構築したグラフのそれぞれのノードを視点に矛盾していないか調査
for i in range(n):
  #まだ調べていないならdfs始める
  if zahyou[i]==None:
    zahyou[i]==0
    flag &=dfs(i)
    if not flag:
      break
if flag:
  print('yes')
else:
  print('no')
