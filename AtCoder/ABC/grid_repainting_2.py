h,w = map(int,input().split())
area =[input() for i in range(h)]

xy=[(1,0),(-1,0),(0,1),(0,-1)]


for i in range(h):
  for j in range(w):
    if area[i][j] == '#':
      f = 0
      for x, y in xy:
        if 0 <= i + y < h and 0 <= j + x < w and area[i+y][j+x]=="#":
          f=1
      if f == 0:
        print('No')
        exit()

print('Yes')
