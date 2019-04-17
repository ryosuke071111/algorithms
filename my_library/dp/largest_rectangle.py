def rectangle(n, hs):
  stack = [] #高さと位置を格納
  ans = 0
  for i, h in enumerate(hs):
    j = i
    while stack and stack[-1][0] > h:
      pre_h, j = stack.pop()
      ans = max(ans, (i - j) * pre_h)

    if not stack or stack[-1][0] < h:
      stack.append((h, j))

  ans = max(ans, max((n-j) * h2 for h2, j in stack))

  return ans

H, W = map(int, input().split())

#ここでリストを固定化しておかないと値を受け付けてくれない
hist = [0] * W
result = 0
for _ in range(H):
  ht = list(map(int, input().split()))
  hist = list(map(lambda pre, cur: (pre+1) * (cur ^ 1), hist, ht))
  result = max(result, rectangle(W, hist))
print(result)
