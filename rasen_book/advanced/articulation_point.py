from sys import setrecursionlimit
setrecursionlimit(100000)

def inpl():
  return tuple(map(int, input().split()))
V, E = inpl()
graph = [[] for i in range(V)]


for _ in range(E):
  s, t = inpl()
  graph[s].append(t)
  graph[t].append(s)


prenum = [-1] * V
lowest = [float("inf")]*V
found = [False] * V
parent = [-1] *V

result = set()
root = 0

def DFS(i, c, prev):
  global root
  prenum[i] = c
  lowest[i] = c
  found[i] = True

  for p in graph[i]:
    if found[p]:
      if p != prev:
        lowest[i] = min(lowest[i], prenum[p])
    else:
      c = DFS(p, c+1, i)
      lowest[i] = min(lowest[i], lowest[p])

  if prenum[prev] <= lowest[i]:
    result.add(prev)
  parent[i] = prev

  return c

DFS(0, 1, 0)

if parent.count(0) <= 2:
  result = result.difference([0])

for r in sorted(result):
  print(r)

