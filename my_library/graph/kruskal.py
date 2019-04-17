
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

    def kruskal(self,v,e):
        edges=[]
        for v1 in range(v):
            for v2, cost in e[v1]:
                if v1<v2:
                    edges.append((cost,v1,v2))
        edges.sort(reverse=True)
        self.mincost=0
        self.minSpanningTree=[]
        uf=UnionFind(v)
        while len(self.minSpanningTree)<v-1:
            cost,v1,v2=edges.pop()
            if uf,same(v1,v2)==False:
                self.mincost+=cost
                uf.unite(v1,v2)
                self.minSpanningTree.append((v1,v2,cost))
    def minCost(self):
        return self.mincost

    def getMinSpanningTree(self):
        return sorted(self.minSpanningTree)

v,e = map(int, input().split())
edges = [[] for _ in range(v)]
for _ in range(e):
  s, t, w = map(int, input().split())
  edges[s].append((t, w))
  edges[t].append((s, w))

msp = Kruskal(v, edges)
print(msp.minCost())


# def main():
#   N, Q = map(int, input().split())
#   uf = UnionFind(N)

#   for _ in range(Q):
#     com, x, y = map(int, input().split())
#     if com == 0:
#       uf.unite(x, y)
#     else:
#       print(int(uf.same(x,y)))
#   return
