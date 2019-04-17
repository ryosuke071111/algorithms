import math

def koch(d, p1, p2):
  if d == 0:
    return
  v = [p2[0]- p1[0], p2[1] - p1[1]]
  s = [p1[0] + v[0] / 3, p1[1] + v[1] / 3]
  t = [p1[0] + 2 * v [0] / 3, p1[1] + 2 * v[1] / 3]
  u = [p1[0] + v[0] / 2 - v[1] * math.sqrt(3) / 6, p1[1] + v[1] / 2 + v[0]* math.sqrt(3) / 6]

  koch(d-1, p1, s)
  print(' '.join(map(str, s)))
  koch(d-1, s, u)
  print(' '.join(map(str, u)))
  koch(d-1, u, t)
  print(' '.join(map(str, t)))
  koch(d-1, t, p2)

n = int(input())
print('0 0')
koch(n, [0, 0], [100, 0])
print('100 0')
