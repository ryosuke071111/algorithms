n,w = map(int,input().split())

ab=[[0,0]]+[list(map(int,input().split())) for i in range(1,n+1)]
dp = [[0 for i in range(w+1)] for i in range(n+1)]

for i in range(1,n+1):
  for j in range(1,w+1):
    if ab[i][1] <= j:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-(ab[i][1])]+ab[i][0])
    else:
      dp[i][j] = dp[i-1][j]

print(dp)
print(ab)
