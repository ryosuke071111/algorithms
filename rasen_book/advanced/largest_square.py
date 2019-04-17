from sys import stdin
readline = stdin.readline

h, w = map(int, input().split())
dp = [list(map(int,input().split())) for _ in range(h)]

for i in range(h):
  for j in range(w):
    dp[i][j] ^= 1
  print(dp)

for i in range(1, h):
  for j in range(1, w):
    if dp[i][j]:
      dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
      print(dp[i][j])

print(max(y for x in dp for y in x) ** 2)
