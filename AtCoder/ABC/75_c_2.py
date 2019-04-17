  #17:51-

#1~mでunionfindを作って頂点の全パターンで親を探索
import sys
input=sys.stdin.readline
class UnionFind:
  def __init__(self, num):
    self.rank = [0]*num
    self.par = [i for i in range(num)] #基準(par = parentのpar)
    self.n   = num
    self.size = [1]*num

#親を探す
  def find(self, x):
    if self.par[x] == x:
      return x
    else:
      self.par[x] = self.find(self.par[x]) #自分じゃなきゃ親を探す
      return self.par[x]

#集合を結合する(結合する前に親のポインタを取得する)
  def union(self, x, y):
    x = self.find(x)
    y = self.find(y)
    if x == y:
      return
    if self.rank[x] < self.rank[y]: #ランクの高い方に基準を合わせる
      x,y=y,x
    if self.rank[x] == self.rank[y]:
      self.rank[x] += 1
    self.par[y] = x
    self.size[x] += self.size[y]
    self.size[y] = 0

  def same(self, x, y):
    return self.find(x) == self.find(y)

  def all_find(self):
    ls=[]
    for n in range(len(self.par)):
      ls.append(self.find(n))
    return ls


n,m=map(int,input().split())
uf=UnionFind(n)
ans=0
ab=[]
for i in range(m):
  a,b=map(int,input().split())
  ab.append([a,b])
for i in range(m):
  uf=UnionFind(n)
  flag=False
  for j in range(m):
    a,b=ab[j]
    if i==j:
      continue
    uf.union(a-1,b-1)
  if len(set(uf.all_find()))>1:
    # print(set(uf.par),uf.par)
    ans+=1
    # print(uf.par,uf.all_find())
print(ans)


# 1-3-4-5-6 7-2

