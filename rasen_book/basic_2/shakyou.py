

class UnionFind:
  def __init__(self, num):
    self.rank = [0]*num
    self.par = [i for i in range(num)]
    self.num = num

    def find(self, x):
      if self.par[x] == x:
        return x
      else:
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def merge(self, x, y):
      x = self.find(x)
      y = self.find(y)
      if x == y:
        return
      if self.rank[x] < self.rank[y]:
        self.par[x] = y
      else:
        self.par[y] = x
        if self.rank[x] == self.rank[y]:
          self.rank[y] += 1

    def same(self, x, y):
      return self.find(x) == self.find(y)




N, Q = map(int, input().split())
uf = UnionFind(N)

for i in range(Q):
  C, X, Y = map(int,input().split())

  if C == 0:
    uf.merge(X, Y)
  else:
    print(1 if uf.same(X, Y) else 0)




def Dijkestra(G, n):
  d = [2000]* n
  d[0] = 0
  isVisited = [False]*n
  C = []

  for i in range(n):
    C.append(i)

  while len(C) != 0:
    u = C[0]
    for i in range(1, len(C)):
      if d[u] > d[C[i]]:
        u = C[i]
    C.remove(u)
  for i in range(len(G[u])):
    if G[u][i] == -1:
      continue
    elif d[i] > d[u] + G[u][i]:
      d[i] = d[u]+G[u][i]
      isVisited[i] = u

  for i in range(n):
    print(i, d[o])

n = int(input())
G =[]

for i in range(n):
  a = []
  ele = list(map(int, input().split()))
  k = ele[1]
  t = ele[2:]
  v = c = []
  for j in range(k):
    v = v+[t[2*j]]
    c = c+[t[2*j+1]]

  for j in range(n):
    if j in v:
      a.append(c[v.index(j)])
    else:
      a.append(-1)
  G.append(a)
Dijkstra(G,n)












#最小全域木（グラフの全域木のなかで編の重みの総和が最小のもの）
#最短経路（重み付きグラフにおいてある点の組の経路の中で編の総和が最小のパス）

n = int(input())
m = [[-1 for i in range(n)] for j in range(n)] #お隣さんへのコストを保存

v = set()
v.add(0)

for i in range(n):
  nums = list(map(int, input().split()))
  for j in range(n):
    m[i][j] = nums[j]


def prim_mst(n):
  isVisited = [False] * n
  d = [0] + [2001] * (n-1)      #TとV-Tのを繋ぐ最小辺の重み

  while  True:
    mincost = 2001

    #0から順に訪問する
    for i in range(n):
      if (not isVisited[i]) and(d[i] < mincost):
        mincost = d[i]
        u = i

    if mincost == 2001:        #mincostが2001になったら繰り返し作業終了
      break

    isVisited[u] = True        #すでに訪れた場合にはTrueを代入する（コスト更新を終了）

    #u（現時点での頂点）のお隣さんに対しての辺のコストを求める（uが今の頂点の値）
    for v in range(n):
      if(not isVisited[v]) and (m[u][v] != -1): #-1でなく何かしらの辺の重みがあるなら
        if m[u][v] < d[v]:
          d[v] = m[u][v]                        #その重みを最小辺リストに追加しよう
          print("d is", d, "\n", "u is", u , "d[v] is" ,d[v])

  print(sum(d))

prim_mst(n)






def dfs(v, cnt):
  D[v] = cnt
  cnt += 1            #初期状態の-1から訪問中の1に変更
  for c in edge[v]:   #隣接行列の中のfor での昇順番目の値
    if D[c] == -1:
      cnt = dfs(c, cnt)
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









def max_heapify(A, i):
  l = 2 * i
  r = 2 * i + 1
  largest = i
  if l < len(A) and A[l] > A[i]:
    largest = l
  else:
    largest = i
  if r < len(A) and A[r] > A[largest]:
    largest = r
  if largest != i:
    tmp = A[i]
    A[i] = A[largest]
    A[largest] = tmp
    max_heapify(A, largest)

def build_maxheap(A):
  i = len(A) // 2
  while i >= 1:
    max_heapify(A, i)
    i -= 1

if __name__ == '__main__':
  num_of_data = int(input())
  A = [int(x) for x in input().split()]
  A.insert(0, 0)

  build_maxheap(A)
  A = A[1:]
  print(' {0}'.format(' '.join(map(str, A))))




















NIL = -1
class Node:
  def __init__(self):
    self.parent = NIL
    self.left = NIL
    self.right = NIL

def getDepth(u):
  d = 0
  while T[u].parent != NIL:
    u = T[u].parent
    d += 1
  return d

def getChildren(u):
  c = T[u].left
  result = []
  while c != NIL:
    result.append(c)
    c = T[c].right
  return result

n = int(input())
T = [0] * n
for i in range(n):
  T[i] = Node()

for i in range(n):
  tmp = list(map(int, imput().split()))
  id = tmp.pop()
  k = tmp.pop()
  c =  tmp
  if k != 0
  for j in range(len(c)):
    T[c[j]].parent = id
    T[id].left = c[0]
    for j in range(len(c)-1):
      T[c[j]].right = c[j+1]

for i in range(n):
  d = getDepth(i)
  c = getChildren(i)
  if d == 0:
    t = 'root'
  elif c == []
    t == 'leaf'
  else:
    t = 'internal node'
  print('node ',i,': ','parent = ',T[i].parent,', depth = ',d,', ',t,', ',c,sep = '')
