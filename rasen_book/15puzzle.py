board = [int(s) for _ in range(4) for s in input().split()]
move_piece = [None]* 46
GOAL = list(range(1,16)) + [0]

def create_adjacent(h, w): #番目状のリストの絶対隣接ポジションを言及
  adjacent = [[] for _ in range(h*w)]
  for i in range(h * w):
    if i % w != w-1: #リストのindxeを4で割ったときに3以上になるのは一番右にあるときのみなので
      adjacent[i].append(i+1) #同じ行の右隣
    if i % w != 0:   #横の長さで割り切れるときは一番左にあるときのみなので
      adjacent[i].append(i-1) #同じ行の左隣
    if i // h < h-1: #リストのindexを4で割ったときに3以上になるのは一番下にあるときなので
      adjacent[i].append(i+w) #次の行の同じ列（直下）
    if i // h > 0: #リストのindexが4以上であるならば2行目以降にあるので
      adjacent[i].append(i-w) #前の行の同じ列（直上）
  # print('adjacent is', adjacent)
  return adjacent

def id_search(limit, move, space, lower):
  if move == limit: #動かす合計が上限に達したら
    if board == GOAL:
      global count
      count += 1
      print(move)
      exit()
  else:             #動かす合計が上限以内の場合
    for x in adjacent[space]: #スペースのあるパズルの隣接パズルについて
      p = board[x]            #その隣接パズルをpに代入する
      if move_piece[move] == p: #動かす対象がそのpならば止める
        continue
      board[space], board[x] = p, 0 #ボードのスペース、スペースの隣接を入れ替え
      move_piece[move + 1] = p      #動かしたピースの値をmove_pieceリストに入れる

      new_lower = lower - distance[p][x] + distance[p][space] #残りの手数を更新
      if new_lower + move <= limit:  #残りの手数+現在動かした数が、下限値以下なら
        id_search(limit, move+1, x, new_lower) #パズルを継続して動かす
      board[space], board[x] = 0, p #現在のボードのspaceは0に、隣接パズルの値はpに

def create_distance(h, w):
  distance = [[0] * h * w for _ in range(h *w)] #マンハッタン距離を格納するリスト
  for i in range(h*w):
    if i == 0:
      continue
    ye, xe = divmod(i-1, w)
    for j in range(h *w):
      y, x = divmod(j,w)
      distance[i][j] = abs(ye-y) + abs(xe-x)    # 二次元配列で[i]が[j]までに移動するコスト
  # print('distance is', distance)
  return distance

def get_distance(board): #ゴールまでの手数を格納する
  v = 0
  for x in range(len(board)):
    p = board[x]
    if p == 0:
      continue
    v += distance[p][x]
  return v

adjacent = create_adjacent(4, 4)
distance = create_distance(4,4)
n = get_distance(board)
count = 0
for x in range(n,46):
  id_search(x, 0, board.index(0), n)
  if count > 0:
    break

