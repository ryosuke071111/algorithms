#9:47-

#dp ver
# n,a=map(int,input().split())
# X=sorted(list(map(int,input().split())))
# #x1...xjからk枚選んでxiの合計をsにするような選び方の総数
# m=max(a,X[-1])
# dp=[[[0 for j in range(m*n+1)] for k in range(n+1)]for s in range(n+1)]

# dp[0][0][0]=1
# for j in range(n+1):
#   for k in range(n+1):
#     for s in range(m*n+1):
#       if j >=1 and s<X[j-1]:
#         dp[j][k][s]=dp[j-1][k][s]
#       elif j>=1 and k>=1 and s>=X[j-1]:
#         dp[j][k][s]=dp[j-1][k][s]+dp[j-1][k-1][s-X[j-1]]
# ans = 0
# for k in range(1, n+1):
#   ans += dp[n][k][k*a]
# print(ans)

#counter ver
#新しいカードの種類xjが出た段階での新しい組み合わせを全て試してその値を合算
from collections import Counter
n,a=map(int,input().split())
X=sorted(list(map(lambda x:int(x)-a,input().split())))
ans=Counter([0])
for x in X:
  tmp=Counter()
  print("x:",x)
  for k,v in ans.items(): #現在のansカウンターに上乗せする形でxjの値を合算することで今までの組み合わせに新たにxjが出たパターンの組み合わせを試行することと同義
    tmp[k+x]+=v
  print(" tmp:",tmp)
  ans+=tmp
  print(" ans:",ans)
print(ans[0]-1)
