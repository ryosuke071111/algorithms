import queue

class UnionFind:
  def __init__(self, N):
    self.sizes = [1 for _ in range(N)]
    self.par = [i for i in range(N)]

  def find(self, x):
    if x == self.par[x]:
      return x
    self.par[x] = self.find(self.par[x])
    return self.par[x]

  def unite(self, x, y):
    x = self.find(x)
    y = self.find(y)

    if x == y:
      return
    if self.sizes[x] < self.sizes[y]:
      x, y, = y, x
    self.par[y] = x
    self.sizes[x] += self.sizes[y]

  def same(self, x, y):
    return self.find(x) == self.find(y)

  def size(self, x):
    return self.sizes[self.find(x)]

def main():
  N, Q = map(int, input().split())
  uf = UnionFind(N)

  for _ in range(Q):
    com, x, y = map(int, input().split())
    if com == 0:
      uf.unite(x, y)
    else:
      print(int(uf.same(x,y)))
  return

if __name__ == '__main__':
  main()
