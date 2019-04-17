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
    if self.rank[x] > self.rank[y]: #ランクの高い方に基準を合わせる
      self.par[y] = x
      self.size[x]+=self.size[y]
      self.size[y] = 0
    else:
      self.par[x] = y
      self.size[y] += self.size[x]
      self.size[x] = 0
      if self.rank[x] == self.rank[y]:
        self.rank[y] += 1

  def same(self, x, y):
    return self.find(x) == self.find(y)

  def all_find(self):
    for n in range(len(self.par)):
      self.find(n)

n,m=map(int,input().split())
edges=[]
for i in range(m):
  a,b=map(int,input().split())
  edges.append([a-1,b-1])


uf=UnionFind(n)
point=n*(n-1)//2
ans=[]
while edges:
  ans.append(point)
  a,b=edges.pop()
  pa=uf.find(a)
  pb=uf.find(b)
  if not uf.same(pa,pb):
    point-=(uf.size[pa]*uf.size[pb])
  uf.union(a,b)

print(*ans[::-1],sep="\n")



