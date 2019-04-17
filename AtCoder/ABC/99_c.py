# 11:02-
n=int(input())
ls=[1]

for i in range(1,7):
  ls.append(6**i)
  ls.append(9**i)
dp = [float('inf') for i in range(n+2)]
dp[0] = 0

#円の総合計
for i in range(1,n+1):
  for j in ls:
    if i-j>=0:
      dp[i] = min(dp[i-1]+1, dp[i-j]+1,dp[i])
    else:
      dp[i] = min(dp[i-1]+1,dp[i])
print(dp[n])

