H, W = map(int, input().split())
S = [list(map(int, input().split())) for i in range(H)]
dp = [[0]*(W) for i in range(H)]

for i in range(H):
  for j in range(W):
    if S[i][j] == 0:
      dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
print(max([max(a) for a in dp])**2)
