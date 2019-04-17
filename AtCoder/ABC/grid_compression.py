h,w = map(int,input().split())
area = [input() for i in range(h)]

row=[False]*h
col=[False]*w

for i in range(h):
  for j in range(w):
    if area[i][j] == '#':
      row[i] = True
      col[j] = True

for i in range(h):
  if row[i]:
    for j in range(w):
      if col[j]:
        print(area[i][j], end='')

    print()

#列と行に#があるところはTrueをつける
#Trueがあった行列の一ますは出力する
#縦横で攻めてどちらかでFalseになったところは出力しない
