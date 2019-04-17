# 間違えた答え
n = int(input())
a = list(map(int,input().split()))

cost = 0
i = 0

for i in range(0,n-1,3):
  if i + 3 <= n-1:
    cost += min(abs(a[i+1]-a[i])+ abs(a[i+3]-a[i+1]), abs(a[i+2]-a[i])+ abs(a[i+3]-a[i+2]))
  elif i + 2 <= n-1:
    cost += min(abs(a[i+1]-a[i]), abs((a[i+2]-a[i])))
  else:
    cost += abs(a[i+1]-a[i])


print(cost)

#正解
n = int(input())
a = list(map(int,input().split()))
dp=[0]*n
dp[1] = abs(a[1]-a[0])

for i in range(2,n):
  dp[i]=min(dp[i-1]+abs(a[i-1]-a[i]),dp[i-2]+abs(a[i-2]-a[i]))

print(dp[-1])

