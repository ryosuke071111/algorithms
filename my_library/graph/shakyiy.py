
  def kruskal(self, v, e):
    edges = []
    for v1 in range(v):
      for v2, cost in e[v1]:
        if v1 < v2:
          edges.append((cost, v1, v2))
    edges.sort(reverse=True)
    self.mincost = 0
    self.minSpanningTree = []
    uf = UnionFindTree(v)
    while len(self.minSpanningTree) < v - 1:
      cost, v1, v2 = edges.pop()
      if uf.same(v1, v2) == False:
        self.mincost += cost
        uf.unite(v1, v2)
        self.minSpanningTree.append((v1, v2, cost))

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
