mod = 10**9+7

h,w,k = map(int,input().split())
fibonacchi =[1, 1, 2, 3, 5, 8, 13, 21, 34]
dp = [[0] * (w + 1) for _ in range(h + 1)]
dp[0][1] = 1
for i in range(h):
  for j in range(w+1):
    #dp[i][j]からdp[i+1][j-1]に遷移する条件
    #jとj-1の間に横棒がある&j-1とj-2の間、j+1とjの間に横棒がない
    #この置き方は
    #（縦棒1から縦棒j-2までの横棒の置き方）* （縦棒j+1から縦棒wまでの横棒の置き方置き方）
    if j >= 2:
      dp[i+1][j-1] += (fibonacchi[j-2]*fibonacchi[w-j])*dp[i][j]
      dp[i+1][j-1]%=mod

    #dp[i][j]からdp[i+1][j+1]への遷移が起こる条件は
    #j+1とjの間に横棒がある&jとj-1の間、j+2とj+1の間に横棒がない
    #この置き方は
    #(縦棒1から縦棒j-1の置き方)*(縦棒j+2*wまでの横棒の置き方)
    if j <= w-1:
      dp[i+1][j+1] += (fibonacchi[j-1]*fibonacchi[w-j-1])*dp[i][j]
      dp[i+1][j+1]%=mod

    #dp[i][j]からdp[i+1][j]への遷移が起こる条件は
    #j-1とjの間、jとj+1の間に横棒がない
    #このような横棒の置き方は
    #（縦棒1から縦棒j-1の置き方）*（縦棒j+1からwまでの棒の置き方）
    dp[i+1][j] += (fibonacchi[j-1]*fibonacchi[w-j])*dp[i][j]
    dp[i+1][j] %=mod

print(dp[h][k])

