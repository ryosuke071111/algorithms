n, p = map(int, input().split())
ps = []
for i in range(n):
  ps.append(input().split())
  ps[i][1] = int(ps[i][1])
t = 0

while len(ps) > 0:
  if ps[0][1] > p:
    ps.append([ps[0][0], ps[0][1]-p])
    t += p
    ps.pop(0)
  else:
    t += ps[0][1]
    print('{0} {1}'.format(ps[0][0], t))
    ps.pop(0)
