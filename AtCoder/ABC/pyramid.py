n = int(input())

xs = []
ys = []
hs = []
for i in range(n):
  x,y,h = map(int,input().split())
  xs.append(x)
  ys.append(y)
  hs.append(h)

for x in range(101):
  for y in range(101):
    for i in range(n):
      if hs[i] >0:
        H = hs[i] + abs(xs[i]-x)+abs(ys[i]-y)
    for i in range(n):
      if hs[i] != max(0, H-abs(xs[i]-x)-abs(ys[i]-y)):
        break
    else:
      print(x,y,H)
      exit()

