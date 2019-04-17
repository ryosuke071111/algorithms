H, W = map(int, input().split())
S = [list(map(int, input().split())) for i in range(H)]
dp = [[0]*(W) for i in range(H)]

for i in range(H):
  for j in range(W):
    if S[i][j] == 0:
      dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1 #こういうもんだ。

print(max([max([max(a) for a in dp])**2]))

#一言：DPで最大正方形問責を求める
#流れ：2次元配列で漸化式の値を代入する（入力された値が0の場所でのみ）→その長さの2乗で面積算出
#計算量：O(HW * min(H,W)^3)
