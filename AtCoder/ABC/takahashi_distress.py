
w = int(input())
n,k = map(int,input().split())

A = []
B = []
dp=[[[0 for i in range(w)] for i in range(n)] for i in range(k)]

for i in range(n):
  a,b = map(int,input().split())
  A.append(a)
  B.append(b)

for i in range(n):
  for j in range(w):
    for k in range(k):
      if A[i] <= j:
        dp[i][j][k] = max(dp[i][j][k-1], dp[i-1][j-A[k-1]][k-1]+ B[k-1])
      else:
        dp[i][j][k] = dp[i][j][k-1]



print(dp)

