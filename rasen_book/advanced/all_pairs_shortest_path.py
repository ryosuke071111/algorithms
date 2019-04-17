import sys

def floyd(v_count, matrix):
  for i in range(v_count):
    for j, c2 in enumerate(matrix[j][i] for j in range(v_count)):
      for k, (c1, c3) in enumerate(zip(matrix[j], matrix[i])):
        if c1 > c2+c3:
          matrix[j][k] = c2+c3
  return matrix

def has_negative_cycle(a):
  return any(row[i] < 0 for i, row in enumerate(a))

V, E = map(int,input().split())
inf = float("inf")
matrix = [[inf]*V for _ in [0]*V]
for i in range(V):
  matrix[i][i] =0
for s,t,d in (map(int, l.split()) for l in sys.stdin):
  matrix[s][t] = d
floyd(V, matrix)
if has_negative_cycle(matrix):
  print('NEGATIVE CYCLE')
else:
  for row in matrix:
    print(' '.join(map(lambda n:str(n) if n!=inf else "INF", row)))
