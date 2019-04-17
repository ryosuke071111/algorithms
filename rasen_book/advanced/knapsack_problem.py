n, w = map(int, input().split())

value = []
weight = []

for _ in range(n):
  vi , wi = map(int,input().split())
  value.append(vi)
  weight.append(wi)

dp = [0 for _ in range(w+1)]

for i in range(n):
  for j in range(w, weight[i] - 1, -1):
    #前者は品物を選択しない、　後者は品物を選択する
    dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

#最大値を出力
# print(dp[w])
print(dp)
