from collections import deque

H, W = map(int, input().split())
max_rect = 0 #最大長方形の面積
prev = [0]*(W+1)

for i in range(H):
  current = [p + 1 if f else 0 for f, p in zip(map(lambda x:int(x) ^ 1, input().split()), prev)] + [0]#高さを取得できる
  stack = [(0, 0)]
  for j in range(W + 1):
    c_j = current[j]
    print('i is', i, " j is", j)
    print('c_j is', c_j)
    print('stack[-1] is', stack[-1])
    print('max_rect is', max_rect,"\n")
    if stack[-1][0] < c_j: #current_jがスタックの後ろの値より大きければ
      stack.append((c_j, j))     #スタックにその値、jの値を入れる
      continue
    if stack[-1][0] > c_j:       #小さければ
      since = 0                  #左端の数値を0にする
      while stack[-1][0] > c_j:  #後ろの数値がスタックの頂点よりも小さい間
        height, since = stack.pop() #高さと左端の数値を取得をスタックから
        max_rect = max(max_rect, height*(j-since)) #面積を更新していく
        print('面積が更新された！',max_rect, "\n")
      if c_j:
        stack.append((c_j, since)) #高さと左端の数値を入れる
  prev = current
print(max_rect)




#一言：最大長方形の面積を求める
#
