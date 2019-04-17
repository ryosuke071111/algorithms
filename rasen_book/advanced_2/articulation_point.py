from sys import setrecursionlimit
setrecursionlimit(100000)

def inp():
  return tuple(map(int, input().split()))
v, e = inp()
edges = [[] for i in range(v)]

for _ in range(e):
  s, t = inp()
  edges[s].append(t)
  edges[t].append(s)

prenum = [-1]*v
lowest = [float('inf')]*v
isVisited = [False]*v
parent = [-1]*v

result = set()  #articulation pointを入れるリスト
root = 0

def dfs(u, c, prev):#(自分番号、何か、親番号)
  global root
  prenum[u] = c
  lowest[u] = c
  isVisited[u] = True

  for p in edges[u]:
    if isVisited[p]:
      if p != prev:
        lowest[u] = min(lowest[u], prenum[p])
    else:
      c = dfs(p, c+1, u)
      lowest[u] = min(lowest[u], lowest[p])

  if prenum[prev] <= lowest[u]:
    result.add(prev)
  parent[u] = prev

  return c

dfs(0, 1, 0)

if parent.count(0) <= 2:
  result = result.difference([0])

for r in sorted(result):
  print(r)


#一言で言うと：エッジを外した時に非連結になるノードを探す
#処理の流れ：dfsで進み①子を二つ以上持つp || prenum[p] <= lowest[u]の場合、pが関節点になる
#計算量：通常でやるとO(V^2)の計算量（全てに対してdfsをする必要性）
