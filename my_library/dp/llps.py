
str=input()
n=len(str)

dp=[[0 for i in range(n)]for i in range(n)]
for i in range(n):
  dp[i][i]=1
  if i+1<n:
    if str[i]==str[i+1]:
      dp[i][i+1]=1
for k in range(3,n):
  for i in range(n-k+1):
    j=i+k-1
    if dp[i+1][j-1] and str[i]==str[j]:
      dp[i][j]=1

for i in dp:
  print(i)

