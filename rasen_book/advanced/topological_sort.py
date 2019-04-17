V, E = map(int, input().split())
L = []
visited = [0 for i in range(V)]
edges = [[] for i in range(V)]
flag = 0

def visit(x):
  if visited[x] ==1:
    flag = 1
  elif not visited[x]:
    visited[x] =1
    for e in edges[x]:
      visit(e)
    visited[x] = 2
    L.insert(0, x)


for i in range(E):
  s,t,=map(int,input().split())
  edges[s].append(t)

for i in range(V):
  if not visited[i]:
    visit(i)
for i in L:
  print(i)
