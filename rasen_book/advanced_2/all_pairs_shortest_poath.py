from math import isinf

V, E = map(int,input().split())

d = [[float('inf') for i in range(V)] for j in range(V)]

for i in range(V):
  d[i][i] = 0

for i in range(E):
  s, t, w = map(int, input().split())
  d[s][t] = w

for k in range(V):
  for i in range(V):
    for j in range(V):
      if d[i][j] > d[i][k] + d[k][j]:
        d[i][j] = d[i][k] + d[k][j]

for i in range(V):
  if d[i][i] < 0:
    print('NEGATIVE CYCLE')
    exit()

for di in d:
  print(' '.join (('INF' if isinf(dij) else str(dij) for dij in di)))
