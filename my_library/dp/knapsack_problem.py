N, W = map(int, input().split())
items = [[0,0]] + [[0,0] for i in range(1,N+1)]

for i in range(1, N+1):
  v,w = map(int,input().split())
  items[i][0] = v
  items[i][1] = w


C = [[0 for i in range(W+1)] for i in range(N+1)]

for i in range(1, N+1):
  for j in range(1, W+1):
    if items[i][1] <= j:
      C[i][j] = max(C[i-1][j], C[i-1][j - (items[i][1])] + items[i][0])
    else:
      C[i][j] = C[i-1][j]

print(C[i][j])
#こんな問題も解けない機械学習の世界に行こうとしているのか？？？
#数学の世界に入る混むならやってみろ
