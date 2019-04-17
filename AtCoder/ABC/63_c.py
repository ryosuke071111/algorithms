#10:59-
# n=int(input())
# S=sorted([int(input()) for i in range(n)])
# not_10=[i for i in S if i%10!=0]
# sums=sum(S)
# if sums%10!=0:
#   print(sums)
# else:
#   print(sums-not_10[0] if not_10 else 0)


"""
2^100値の最大値を取る問題（sum%10!=0）
①合計がすでに%10!=0ならそのまま出力
②そうでないなら%!10=0でないもののうち最小を取り出す
　→35 25 15 5 の場合、それぞれペアが作られて部分的に10の倍数が作られて合計が10の倍数になるので一つを崩す。
"""

#dp
N = int(input())
s = []
for i in range(N):
    s.append(int(input()))
stot = sum(s)
#i個のうちいくつか使ってjにできるか
dp = [[False for i in range(stot+101)] for j in range(N+1)]
dp[0][0] = True
for i in range(N):
    for j in range(stot):
        dp[i+1][j+s[i]] = dp[i][j] or dp[i+1][j+s[i]]
        dp[i+1][j] = dp[i][j] or dp[i+1][j]

ans = 0
for i in range(stot+1):
    if dp[N][i] and i % 10 != 0:
        ans = i
for i in dp:
  print(i)
print(ans)















