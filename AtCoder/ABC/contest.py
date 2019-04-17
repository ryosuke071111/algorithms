n = int(input())
nums = list(map(int,input().split()))
P = sum(nums)

dp = [[0 for i in range(P+1)] for i in range(n+1)]
dp[0][0] = 1
for i in range(n):
  for j in range(P+1):
    if dp[i][j] == 1:
      dp[i+1][j] = 1
      if j+nums[i] <= P:
        dp[i+1][j+nums[i]]=1
print(sum(dp[n]))
print(dp)

#別解
N = int(input())
P = list(map(int, input().split()))
s = {0}
for i in range(N):
    sub_s = set()
    for n in s:
        sub_s.add(n)
        sub_s.add(n+P[i])
    s = sub_s
print(len(s))
