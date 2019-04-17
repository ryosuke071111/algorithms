n,m = map(int, input().split())
mo = list(map(int, input().split()))
dp = [float("inf") for i in range(n+2)]
dp[0] = 0

#円の総合計
for i in range(n+1):
  #額面のコインの種類
  for j in mo:
    if i + j <= n:
      dp[i+j] = min(dp[i+j], dp[i]+1)
      print(dp[i+j], dp[i]+1)
print(dp[n])

#2
n, m = map(int, input().split()) #n：金額　m：コインの枚数
coins = list(map(int,input().split()))
T = [0] + [float('inf')]*n


for i in range(m):                  #コインの枚数
  for j in range(coins[i], n+1):              #支払う金額
    T[j] = min(T[j], T[j - coins[i]] + 1)

print(T[j])
