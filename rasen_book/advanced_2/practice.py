#dijkstra

def Dijkstra(G,n):
  d = [2000]*n
  d[0] = 0
  visited = [False]*n
  C = []
  for i in range(n):
    C.append(i)

  while len(C) != 0:
    u = C[0]
    for i in range(1,len(C)):
      if d[u] > d[C[i]]:
        u = C[i]
    C.remove(u)

    for i in range(len(G[u])):
      if G[u][i] == -1:
        continue
      elif d[i] > d[u]+G[u][i]:
        d[i] = d[u]+G[u][i]
        visited[i] = u
  for i in range(n):
    print(i,d[i])

n = int(input())
G=[]
for i in range(n):
  a = []
  ele = list(map,int(input().split()))
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

#prim
n = int(input())
m = [[-1 for i in range(n)] for j in range(n)]
d = [0]+[2000]*(n-1)
visited = [False]*n

for i in range(n):
  nums = list(map(int,input().split()))
  for j in range(n):
    m[i][j] = nums[j]

def prim_ms(n):
  while True:
    mincost = 2000
    for i in range(n):
      if not visited[i] and d[i] < mincost:
        mincost = d[i]
        u = i
    visited = True
    if mincost ==2000:
      break

    for v in range(n):
      if not visited[v] and m[u][v] != -1:
        if m[u][v] < d[v]:
          d[v] = m[u][v]
    print(d)


#priority_que
n,p = map(int,input().split())
ps=[]


#BST
class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

class BST:
  def __init__(self,number_list):
    self.root = None
    for node in number_list:
      self.insert(node)

  def insert(self, data):
    n = self.root
    if n == None:
      self.root = Node(data)

class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

class BST:
  def __init__(self, number_list):
    self.root = None
    for node in number_list:
      self.insert(node)

  def insert(self,data):
    n = self.root
    if n is None:
      self.root = Node(data)
    else:
      while True:
        entry = n.data
        if data < entry:
          if n.left is None:
            n.left = Node(data)
          n = n.left
        elif data > entry:
          if n.right is None:
            n.right = Node(data)
          n = n.right
        else:
          n.data = data



#max_heap
def max_heapify(A,i):
  l = 2*i
  r = 2*i+1
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
    max_heapify(A,largest)

def build_maxheap(A):
  i = len(A)//2
  while i >= 1:
    max_heapify(A,i)
    i -= 1


#union-find
class UnionFind:
  def __init__(self,num):
    self.rank = [0]*num
    self.par = [i for i in range(num)]
    self.n = num

  def find(self,x):
    if self.par[x] == x:
      return x
    else:
      self.par[x] == self.find(self.par[x])
      return self.par[x]

  def merge(self,x,y):
    x = self.find(x)
    y = self.find(y)
    if x == y:
      return
    if self.rank[x]>self.rank[y]:
      self.par[y] = x
    else:
      self.par[x] = y
      if self.rank[x] == self.rank[y]:
        self.rank[y] += 1

  def same(self,x,y):
    return self.find(x) == self.find(y)

N, Q = map(int, input().split())
uf = UnionFind(N)

for i in range(Q):
  C, X, Y = map(int, input().split())

  if C ==0:
    uf.merge(X,Y)
  elif C == 1:
    print(1 if uf.same(X,y) else 0)
  else:
    print(uf.find(X))

