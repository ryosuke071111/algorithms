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
    ls=[]
    for i in range(len(self.par)):
      ls.append(self.find(i))
    return ls

n,m=map(int,input().split())
edges=[[0]*n for i in range(n)]
AB=[]
ans=UnionFind(n)
for i in range(m):
  a,b=map(int,input().split())
  AB.append([a-1,b-1])
  edges[a-1].append(b-1)
  edges[b-1].append(a-1)
  ans.union(a-1,b-1)
cnt=0
for i in range(m):
  uf=UnionFind(n)
  for j in range(m):
    if i==j:
      continue
    a,b=AB[j]
    uf.union(a,b)
  if len(set(uf.all_find()))>1:
    cnt+=1
print(cnt)



