n,a=map(int,input().split())
X=list(map(int,input().split()))

dp=[[[0]*(sum(X)+1) for _ in range(n+1)] for _ in range(n+1)]

dp[0][0][0]=1

for i in range(1,n+1): #x_1,x_2...x_n
  for k in range(i):   #k枚数選ぶ
    for s in range(sum(X)+1): #合計
      if dp[i-1][k][s]:
        print(i,k,s,"|",i,k+1,s+X[i-1],X[i-1],"を加えた")
        dp[i][k+1][s+X[i-1]]+=dp[i-1][k][s] #1枚選択肢が増えた時の、そのカードを加えた結果を加算
        dp[i][k][s]+=dp[i-1][k][s]

ans=0
for i in range(1,n+1):
  for j in range(1,sum(X)+1):
    if j == i*a: #合計が平均のi倍の時に加える
      ans+=dp[n][i][j]

print(ans)

