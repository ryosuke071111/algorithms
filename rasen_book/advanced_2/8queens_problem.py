board = [["." for i in range(8)] for i in range(8)]
N = int(input())
row = [1] * 8
col = [1] * 8
dpos = [1] * 15
dneg = [1] * 15


for i in range(N):
  x, y = map(int, input().split())
  row[x] = col[y] = dpos[x+y] =dneg[x-y+7] = 0
  board[x][y] = "Q"

def solve(i):
  while i < 8 and not row[i]: #iが1、かつ、row[i]の値でなければiを増やしていく
    i += 1
    print('i is ',i)
  if i == 8:                  #iが8になったら（クイーンの配置に成功したら）
    for i in range(8):        #リストの中身を全部結合する
      print(''.join(board[i]))
  for j in range(8):          #jの値を増やしていく
    if not col[j] or not dpos[i+j] or not dneg[i-j+7]: #これらのリストが0なら（クイーンが置けたら止める。）
      continue
    row[i] = col[j] = dpos[i+j] = dneg[i-j+7] = 0 #全部に当てはまるところを0に
    board[i][j] ='Q'
    solve(i+1)                                    #次の行へ行く
    row[i] = col[j] = dpos[i+j] =dneg[i-j+7] = 1
    board[i][j] = '.'

solve(0)

#一言：斜めに被らないようにクイーンを配置する
#処理のプロセス：クイーンの動きを模す漸化式を作ってアルゴリズムを作成→ループで最適値
#計算量：
