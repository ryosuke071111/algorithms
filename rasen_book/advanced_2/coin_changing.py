n, m = map(int, input().split()) #n：金額　m：コインの枚数
coins = list(map(int,input().split()))
T = [0] + [float('inf')]*n


for i in range(m):                  #コインの枚数
  for j in range(coins[i], n+1):              #支払う金額
    T[j] = min(T[j], T[j - coins[i]] + 1)

print(T[j])

# #一言：n円の金額をm種類のコインで支払う際の最小枚数
# #処理の流れ：動的計画を用いて、min(T[i][j], T[i][j-C[i]]+1)
# #計算量：O(mn)二重ループなので。
