def queenprint():
  global x
  global col
  global row
  global k
  global maxx

  for i in range(maxx):
    for j in range(maxx):
      if x[i][j] and row[i] != j:
        return

  for i in range(maxx):
    for j in range(maxx):
      if row[i] == j:
        print('Q', end = '')
      else:
        print('.', end = '')
    print()

def recursive(i):
  global x
  global col
  global row
  global k
  global maxx

  if (i == maxx): #クイーンの配置に成功
    queenprint()
    return

#ここで再帰的に呼び出しを行なっているけど今は完全には理解できない
  for j in range(maxx):

    #他のクイーンに襲撃されている場合は無視
    if(col[j] or dpos[i+j] or dneg[i - j + maxx - 1]):
      continue

    row[i] = j

    #(i, j) にクイーンを配置
    col[j] = dpos[i + j] = dneg[i - j + maxx - 1 ] =1

    #次の行を試す
    recursive(i + 1)
    #（i, j）に配置されているクイーンをとり覗く
    row[i] = col[j] = dpos[i + j] = dneg[i - j + maxx - 1] = 0

#マス目の数
maxx = 8
k = int(input())
x = [[0 for i in range(maxx)] for j in range(maxx)]
col = [0 for i in range(maxx)]
row = [0 for i in range(maxx)]
dpos = [0 for i in range(maxx * 2 - 1)]
dneg = [0 for i in range(maxx * 2 - 1)]

for i in range(k):
  r,c = [int(x) for x in input().split()]
  x[r][c] = 1

recursive(0)



