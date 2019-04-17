board = [int(s) for _ in range(4) for s in input().split()] #ボードを作る
move_piece = [None] * 46
GOAL = list(range(1, 16)) + [0] #理想形を作る

def create_adjacent(h, w):
  adjacent = [[] for _ in range(h*w)] #状態の配列？
  for i in range(h * w):
    if i % w != w-1 :
      adjacent[i].append(i + 1)
    if i % w != 0:
      adjacent[i].append(i - 1)
    if i // h < h - 1:
      adjacent[i].append(i + w)
    if i // h > 0:
      adjacent[i].append(i - w)
    print(adjacent)
  return adjacent

def id_search(limit, move, space, lower):
  if move == limit:
    if board == GOAL:
      global count
      count += 1
      print(move)
      exit()
  else:
    for x in adjacent[space]: #状態の配列の中でイテレーション
      p = board[x]            #ボードの任意の数値をpへ
      if move_piece[move] == p: #pの値を動かす対象とする
        continue
      board[space], board[x] = p, 0 #新しいボードの空部分をp、ボードの任意の値を0とする
      move_piece[move + 1] = p      #動かす対象の次の数値をpにする
      new_lower = lower - distance[p][x] + distance[p][space] #

      #下限値枝刈法
      if new_lower + move <= limit:
        id_search(limit, move + 1, x, new_lower)
      #元に戻す
      board[space], board[x] = 0, p

def create_distance(h, w): #ゴールまでの推定値を算出
  distance = [[0] * h * w for _ in range(h *w)] #ボードの目分0を作る
  for i in range(h * w):
    if i == 0:
      continue
    ye, xe = divmod(i - 1, w) #i-1/w の商とあまりをそれぞれ　ye, xeに代入
    for j in range(h * w):
      y, x = divmod(j, w)     #j/w の商とあまりをそれぞれ y、xに代入する
      distance[i][j] = abs(ye - y) + abs(xe - x)
    print("distance is", distance)
  return distance

def get_distance(board): #ゴールまでの推定値を取得
  v = 0
  for x in range(len(board)):
    p = board[x]
    if p == 0:
      continue
    v += distance[p][x]
  return v

adjacent = create_adjacent(4, 4)
distance = create_distance(4, 4)
n = get_distance(board)
count = 0
for x in range(n, 46):
  id_search(x, 0, board.index(0),n)
  if count > 0 :
    break
