import sys
input=sys.stdin.readline

class UnionFind:
  def __init__(self, num):
    self.rank = [0]*num
    self.par = [i for i in range(num)] #基準(par = parentのpar)
    self.n   = num

  def find(self, x):
    if self.par[x] == x:
      return x
    else:
      self.par[x] = self.find(self.par[x]) #自分じゃなきゃ親を探す
      return self.par[x]

  def union(self, x, y):
    x = self.find(x)
    y = self.find(y)
    if x == y:
      return
    if self.rank[x] > self.rank[y]: #ランクの高い方に基準を合わせる
      self.par[y] = x
    else:
      self.par[x] = y
      if self.rank[x] == self.rank[y]:
        self.rank[y] += 1

  def same(self, x, y):
    return self.find(x) == self.find(y)

n,q=map(int,input().split())
uf=UnionFind(n)
for i in range(q):
  p,a,b=map(int,input().split())
  if p==0:
    uf.union(a,b)
  else:
    print("Yes" if uf.same(a,b) else "No")
