
class UnionFind:
  def  __init__(self,num):
    self.rank=[0]*num
    self.par=[i for i in range(num)]
    self.n=num

  def find_set(x):
    if self.par[x]==x:
      return x
    else:
      self.par[x]=self.find_set(self.par[x])
      return self.par[x]

  def union(self, x,y):
    x = self.find_set(x)
    y = self.find_set(y)
    if x==y:
      return
    if self.rank[x]>self.rank[y]:
      self.par[y]=x
    else:
      self.par[x]=y
      if self.rank[x]==self.rank[y]:
        self.rank[y]+=1
  def same(self,x,y):
    return self.find_set(x)==self.find_set(y)


n,q=map(int,input().split())
uf=UnionFind(n)
for i in range(q):
  c,x,y=map(int,input().split())
  if c==0:
    uf.union(x,y)
  if c==1:
    print(1 if uf.same(x,y) else 0)
  else:
    print(uf.find_set(x))
