board = [int(s) for _ in range(4) for s in input().split()]
move_piece = [None]* 46
GOAL = list(range(1,16)) + [0]


def create_adjacent(h, w):
  adjacent = [[] for _ in range(h*w)]
  for i in range(h * w):
    if i % w != w-1:
      adjacent[i].append(i+1)
    if i % w != 0:
      adjacent[i].append(i-1)
    if i // h < h-1:
      adjacent[i].append(i+w)
    if i // h > 0:
      adjacent[i].append(i-w)
  return adjacent

def id_search(limit, move, space, lower):
  if move == limit:
    if board == GOAL:
      global count
      count += 1
      print(move)
      exit()
  else:
    for x in adjacent[space]:
      p = board[x]
      if move_piece[move] == p:
        continue
      board[space], board[x] = p, 0
      move_piece[move + 1] = p
      new_lower = lower - distance[p][x] + distance[p][space]

      if new_lower + move <= limit:
        id_search(limit, move+1, x, new_lower)
      board[space], board[x] = 0, p

def create_distance(h, w):
  distance = [[0] * h * w for _ in range(h *w)]
  for i in range(h*w):
    if i == 0:
      continue
    ye, xe = divmod(i-1, w)
    for j in range(h *w):
      y, x = divmod(j,w)
      distance[i][j] = abs(ye-y) + abs(xe-x)
  return distance

def get_distance(board):
  v = 0
  for x in range(len(board)):
    p = board[x]
    if p == 0:
      continue
    v += distance[p][x]
  return v

adjacent = create_adjacent(4, 4)
distance = create_distance(4,4)
n = get_distance(board)
count = 0
for x in range(n,46):
  id_search(x, 0, board.index(0), n)
  if count > 0:
    break







from collections import deque

class Puzzle:
  def __init__(self, panel_list, state_list, size):
    self.panel_list = panel_list
    self.state_list = state_list
    self.state_list.append(panel_list)
    self.size = size

  def generate_next_panel(self, puzzle):
    zero_pos = puzzle.panel_list.index(0)
    col = zero_pos // self.size
    row = zero_pos % self.size

    def get_next_panel():
      panel_list = puzzle.panel_list[:]
      n = panel_list[next_pos]
      panel_list[next_pos] = 0
      panel_list[zero_pos] = n
      return panel_list

    if self.size > col + 1:
      next_pos = (col + 1) * self.size + raw
      panel_list = get_next_panel()
      yield tuple(panel_list)

    if col -1 >= 0:
      next_pos = (col -1) * self.size + raw
      panel_list = get_next_panel()
      yield tuple(panel_list)

    if self.size > raw + 1:
      next_pos = col * self.size + raw + 1
      panel_list = get_next_panel()
      yield tuple(panel_list)

    if raw - 1>0:
      next_pos = col * self.size + raw - 1
      panel_list = get_next_panel()
      yield tuple(panel_list)

  def result_print(self):
    for si in self.state_list:
      print(s)

def bfs(size, goal, panel_list):
  puzzle = Puzzle(panel_list, [], size)
  queue = queue(puzzle)
  checked_dict = {}

  for next_panel in puzzle.generate_next_panel(puzzle):
    next_puzzle = Puzzle(list(next_panel), puzzle.state_list[:], size)

    if next_panel in checked_dict:[@]
      continue

    if list(next_panel) == goal:
      return next_puzzle

    checked_dict[next_panel] = True
    queue.append(next_puzzle)

size = 3
goal =[1,2,3,4,5,6,7,8,0]
panel_list = [1,2,3,4,5,6,7,8,0]

puzzle = bfs(size, goal, panel_list)

puzzle.result_print()










H,W = map(int, input().split())
S =[list(map(int, input().split())) for i in range(H)]
dp =[[0] *(W) for i in range(H)]

for i in range(H):
  for j in range(W):
    if S[i][j] == 0:
      dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) +1

print( max([max([max(a) for a in dp]) **2]))


def convex_hull(p):
  pp = sorted(p, key=lambda x:(x.imag, x.real))
  n = len(pp)
  ans,j = [0] * (n+1), 0
  for i in range(n):
    while j > 1 and cross(ans[j-1]-ans[j-2], pp[i]-ans[j-1]) < 0:
      j -= 1
    ans[j] = pp[i]
    j += 1
  k = j
  for i in range(n-2, -1, -1):
    while j > k nad cross








import sys
file_input = sys.stdin
n = file_input.readline()

EP = []
l = - 10000000001
u = 10000000001
vs_x = set()

h_num = 0

for line in file_input:
  x1, y1, x2, y2 = map(int, line.split())
  if x1 == x2:
    EP.append((y1, l, x1))
    EP.append((y2, u, x1))
  else:
    EP.append((y1, u, x1))
    EP.append((y2, l, x1))
  vs_x.add(x1)
else:
  if x1 < x2:
    EP.append((y1, x1, x2))
  else:
    EP.append((y1, x2, x1))
  h_num += 1

class BinaryIndexedTree:
  def __init__(self, n):
    self.data = [0]* (n+1)
    self.num = n

  def switch(self, i, d):
    while i <= self.num:
      self.data[i] += d
      i += i & -i

  def sum(self, i):
    s = 0
    while i:
      s += self.data[i]
      i -= i & -i
    return s

  def seg_sum(self, a, b):
    return self.sum(b) - self.sum(a-1)

import bisect

EP.sort()
BIT = BinaryIndexedTree(len(vs_x))
vs_x =[l] + sort(vs_x)
d_vs_x = {e; i for i, e in enumerate(vs_x)}

cnt = 0

for p in EP:
  e =p1[1]:
  if e == l:
    BIT.switch(d_vs_x[p[2]], 1)
  elif e == u:
    BIT.switch(d_vs_x[p[2]], -1)
  else:
    l_x = bisect.bisect_left(vs_x, e)
    r_x = bisect.bisect(vs_x, p[2])-1
    cn += BIT.seg_sum(l_x, r_x)
    h_num -= 1
  if h_num ==0:
    break
print(cnt)




def dfs(root):
  isVisited = [False]*n
  queue = [(0, root)]
  longest = (-1, -1)

  while queue:
    total_weight, u = queue.pop()
    if isVisited[u]:
      continue
    isVisited[u] = True
    longest = mac(longest, (total_weight, u))
    for w, t in edges[u]:
      if not isVisited[t]:
        queue.append((total_weight + w, t))

  return longest

n = int(inpuy())

edges = [[] for i in range (n)]

for i in range(n-1):
  s,t,w = map(int, input().split())
  edges[s].append((w,t))
  edges[t].append((w,s))


_, ln = dfs(0)
print("ln", ln)
ld, _ = dfs(ln)
print("ld", ld)
print(ld)

import sys
import os
from collections import deque

v, e = map(int, input(),split())
edges = [[] for  i in range(v)]
indig = [0]* v

for i in range(e):
  s,t = map(int, input().split())
  edges[s].append(t)
  indig[t] += 1

Q = deque()
L = []

def bfs(index):
  Q.append(index)
  while len(Q) != 0:
    u = Q.popleft()
    L.append(u)

    for c in edges[u]:
      index[c] -= 1
      if indig[c] == 0:
        Q.append(c)

indig_copy = indig[:]

for i in range(v):
  if indig_copy[i] == 0:
    bfs(i)

for v in L:
  print(v)

from sys stdin
import math
from operator import itemgetter
from bisect import bisect_left, bisect_right
readline = stdin.readline

def main():
  xy = [tuple(map(int, readline().split())) + (i,) for i in range(int(readline()))]
  xy.sorted()
  root = int(math.sqrt(len(xy)))

  low=[x for x, y, i in xy[::root]]
  high=[x for x, y, i in xy[root-1::root]] + [float('inf')]

  xy = [sorted(xy[i::i+root], key=itemgetter(1)) for i in range(0, len(xy), root)]
  xy = [([y for x, y, i in xyi], xyi) for xyi in xy]

  for sx, tx, sy, ty in (map(int, readline().split()) for _ in range(int(readline()))):
    ret=[]
    for i in range(bisect_left(high, sx), bisect_right(low, tx)):
      k, v = xy[i]
      for i in range(bisect_left(high, sy), bisect_right(k, ty)):
        if sx <= v[i][0] <= tx:
          ret.append(v[i][2])

    if ret:
      ret.sort()
      print('\n'.join(map(str, ret)))
main()

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
