h,w = map(int,input().split())
area =[input() for i in range(h)]

xy=[(1,0),(-1,0),(0,1),(0,-1)]

for i in range(h):
  for j in range(w):
    if area[i][j] == '#':
      flag=0
      for x, y in xy:
        #斜めに黒が存在しないか確認（存在してしまったらそれは塗ることができないのでfalse）
        if 0 <= i + y < h and 0 <= j + x < w and area[i+y][j+x]=="#":
          flag=1
      if not flag:
        print('No')
        exit()
print('Yes')

