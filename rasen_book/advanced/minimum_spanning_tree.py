def root(x):
  if par[x] == x:
    return x
  par[x] = root(par[x])
  return par[x]

def same(x, y):
  return root(x) == root(y)

def unite(x, y):
  x = root(x)
  y = root(y)
  par[x] = y

v, e = map(int,input().split())
adj = [list(map(int, input().split())) for i in range(e)]
adj.sort(key = lambda x:x[2])
par = [i for i in range(v)]
sum = 0

for i, j, k in adj:
  if not same(i, j):
    sum += k
    unite(i, j)
print(sum)
