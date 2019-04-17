"""1. 最大和問題
N要素を持つ数列 a[0],a[1],⋯,a[N−1] から任意の個数の項を選んで和を取った時の最大値
"""

def max_sum(N,a):
  dp=[0]*(N+1)
  for i in range(N):
    dp[i+1]=max(dp[i],dp[i]+a[i])
  return dp[N]
"""
2. ナップサック問題
重さと価値の情報を持つ N 個の荷物を重さが W 以下になるように詰め込むとき価値の和を最大化
"""
def knapsack(N,W,weight,value):
  #初期化
  inf=float("inf")
  dp=[[-inf for i in range(W+1)] for j in range(N+1)]
  for i in range(W+1): dp[0][i]=0

  #DP
  for i in range(N):
    for w in range(W+1):
      if weight[i]<=w: #dp[i][w-weight[i]の状態にi番目の荷物が入る可能性がある
        dp[i+1][w]=max(dp[i][w-weight[i]]+value[i], dp[i][w])
      else: #入る可能性はない
        dp[i+1][w]=dp[i][w]
  return dp[N][W]
  """
3. 部分和問題
正の数列 a[0],a[1],⋯,a[N−1] の部分和で A になるものはある？
dp[i][j]は 0 から i−1 項目までの成分で和が j になるものがあるか？を表すboolean
i 項目までの和が jになるには, i−1 項目までの和が j か j−a[i] であればよい
"""

def part_sum0(a,A):
  #初期化
  N=len(a)
  dp=[[0 for i in range(A+1)] for j in range(N+1)]
  dp[0][0]=1

  #DP
  for i in range(N):
    for j in range(A+1):
      if a[i]<=j: #i+1番目の数字a[i]を足せるかも
        dp[i+1][j]=dp[i][j-a[i]] or dp[i][j]
      else: #入る可能性はない
        dp[i+1][j]=dp[i][j]
  return dp[N][A]

"""
4. 部分和数え上げ問題
正の数列 a[0],a[1],⋯,a[N−1] の部分和で A になるものは何通りある？109+7 で割った余りを出力
dp[i][j]は 0 から i−1 項目までの成分で和が j になるものが何通りあるか？を表す
i 項目までの和が j になるには, i−1 項目までの和が j か j−a[i] であればよい
"""

def part_sum(a,A):
  p=10**9+7
  #初期化
  N=len(a)
  dp=[[0 for i in range(A+1)] for j in range(N+1)]
  dp[0][0]=1

  #DP
  for i in range(N):
    for j in range(A+1):
      if a[i]<=j: #i+1番目の数字a[i]を足せるかも
        dp[i+1][j]=dp[i][j-a[i]]+ dp[i][j]% p
      else: #入る可能性はない
        dp[i+1][j]=dp[i][j]%p
  return dp[N][A]

"""
5. 最小個数部分和問題
正の数列 a[0],a[1],⋯,a[N−1] の部分和が A になるもののうち, 必要な項は最小で何個あるかを返す. できない場合はinftyを返す.
dp[i][j]は 0 から i−1 項目までの成分で和が j になるために必要な項は最小で何個かを表す
i 項目までの和が j になるには, i−1 項目までの和が j か j−a[i] であればよい
"""

def min_num_part_sum(a,A):
  #初期化
  N=len(a)
  inf=float("inf")
  dp=[[inf for i in range(A+1)] for j in range(N+1)]
  dp[0][0]=0

  #DP
  for i in range(N):
    for j in range(A+1):
      if a[i]<=j: #i+1番目の数字a[i]を足せるかも
        dp[i+1][j]=min(dp[i][j-a[i]]+1, dp[i][j])
      else: #入る可能性はない
        dp[i+1][j]=dp[i][j]
  return dp[N][A]

"""
6. K個以内部分和問題も上のコードで対応可能.
7. 個数制限付き部分和問題正の数
正の数列 a[0],a[1],⋯,a[N−1] の各項 a[i] が m[i] 個あるとき, 部分和で A は作れるか. ただし m[i] は正の整数.
dp[i+1][j] は第 i 項目を何個残して達成できるかを表す.
iを固定して, j を小さいものから dp[i+1][j] を定めていく.
dp[i][j] が非負なら第 i 項目を使わずに達成できる.
dp[i+1][j−a[i]] が 0 以下なら達成できない, a[i]が j より大きい場合も達成できない
dp[i+1][j−a[i]] が 1 以上なら a[i] を1つ使って達成できる.
以上から,
"""

def restricted_part_sum(a,m,A):
  #初期化
  N=len(a)
  dp=[[-1 for i in range(A+1)] for j in range(N+1)]
  dp[0][0]=0

  #DP
  for i in range(N):
    for j in range(A+1):
      if dp[i][j]>=0: dp[i+1][j]=m[i]
      elif j<a[i] or dp[i+1][j-a[i]]<=0: dp[i+1][j]=-1
      else: dp[i+1][j]=dp[i+1][j-a[i]]-1
  return dp[N][A]>=0

"""
dp[i+1][j] の更新の仕方を見ると, dp[i][j] が非負のときは m[i] が表れるだけですし, それ以外の状況では dp[i+1][k],k=0,1,⋯j−1 の情報しか使っていません. なのでメモはもっと小さくてもよさそうです.
"""

def restricted_part_sum(a,m,A):
  #初期化
  N=len(a)
  dp=[-1 for i in range(A+1)]
  dp[0]=0

  #DP
  for i in range(N):
    for j in range(A+1):
      if dp[j]>=0: dp[j]=m[i]
      elif j<a[i] or dp[j-a[i]]<=0: dp[j]=-1
      else: dp[j]=dp[j-a[i]]-1
  return dp[A]>=0

"""
8. 最長共通部分列 (LCS) 問題
文字列 S, T の最長共通部分列の長さを返します.
dp[i][j] は S の i−1 文字目までと T の j−1 文字目まででの最長共通部分列(Longest Common Subsequence)の長さを表します.
"""

def LCS(S,T):
  #初期化
  dp=[[0 for i in range(len(T)+1)] for j in range(len(S)+1)]

  #DP
  for i in range(len(S)):
    for j in range(len(T)):
      dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
      if S[i]==T[j]:
        dp[i+1][j+1]=max(dp[i+1][j+1],dp[i][j]+1)
  return dp[len(S)][len(T)]

"""
元記事では DP 初期条件として dp[0][0] のみですが, dp[1][0], dp[0][1] も初期化が必要ではないでしょうか.
9. 最小コスト弾性マッチング問題
列 A=(a0,a1,⋯,am−1), B=(b0,b1,⋯,bn−1)が与えられています. i=0,1,⋯,m−1,j=0,1,⋯,n−1 に対してコスト c(i,j) が与えられたとき, 最小コスト弾性マッチング問題を考えます.
dp[i][j] は A の i−1 までと B の j−1 までの最小コストを表します.
"""

def DP_match(A,B,cost):
  m=len(A)
  n=len(B)
  dp=[[0 for i in range(n+1)] for j in range(m+1)]
  for i in range(len(S)):
    for j in range(len(T)):
      dp[i+1][j+1]=max(dp[i][j],dp[i+1][j],dp[i][j+1])+cost[i,j]
  return dp[m][n]

"""
10. レーベンシュタイン距離 (diffコマンド)
文字列 S, T の編集距離を返します. 編集距離とは, 文字列 S に対して, 1 文字変更, 1 文字削除, 1 文字挿入の操作を最小で何回施せば文字列 T に書き換えることが出来るかを表します.
dp[i][j] は S の i−1 までと B の j−1 までの編集距離を表します.
"""

def Levenshtein_dist(S,T):
  m=len(S)
  n=len(T)
  inf=float("inf")
  dp=[[inf for i in range(n+1)] for j in range(m+1)]
  dp[0][0]=0

  for i in range(-1,m):
    for j in range(-1,n):
      if i==-1 and j==-1:
        continue
      elif i>=0 and j>=0:
        if S[i]==T[j]:
          dp[i+1][j+1]=min(dp[i][j],dp[i][j+1]+1, dp[i+1][j]+1)
        else:
          dp[i+1][j+1]=min(dp[i][j]+1,dp[i][j+1]+1, dp[i+1][j]+1)
      elif i>=0:
        dp[i+1][j+1] = dp[i][j+1]+1
      elif j>=0:
        dp[i+1][j+1] = dp[i+1][j]+1
  return dp[m][n]

"""
元記事では DP 漸化式には min を用いるべきではないでしょうか.
11. 発電計画問題
区間 (0,T] をどのように区切れば利益が最大になるかという問題です.
dp[t] は”時刻 (t−1,t] ではオフにしていたときの発電計画のうちの最大利益”を表します.
時刻 T で発電をやめることを考えるればよいので, dp[T+1] が求める値となります.
また, dp[t] は1つ手前の項だけでは定まらないことに注意しますが, 以下のように考えるとよいです.

まず, ”時間 (t−1,t] ではオフにしていた”発電計画を以下の要素に分解します:
(1) 時間 (t−2,t−1] でもオフにしていた
このような発電計画のうち最大利益を達成するものは, 前項の dp[t−1] です.
(2) 時間 (t−2,t−1] ではオンにしていた
ここで, 最後のオンにしていた時間について場合わけをします. つまり, ”時刻i=0,1,⋯t−2 から時刻 t−1 の時間でオンにしたもの”を考えれば十分です. それぞれのケースにおける最大利益は
dp[i]+g[i][t−1]
となります.
(1), (2)をまとめると, 漸化式は
dp[t]=max{dp[t−1],max0≤i<t−1{dp[i]+g[i][t−1]}}
によって与えられます.
"""

def hastudenkeikaku(T,g):
  #初期化
  dp=[0]*(N+2)

  #DP
  for t in range(2,T+2):
    dp[t]=dp[t-1]
    for i in range(t-1):
      dp[t]=max(dp[t],dp[i]+g[i][t-1])
  return dp[T+1]

"""
元記事とは漸化式が異なりますが, こちらのほうが計算量が少ないのでは.
12. 分かち書き
パターン認識でよくあるらしいです. 文字数 n の入力 A が与えられたとき, 単語 w[j][i]=A[j:i+1], つまり A のj−1 文字目から i−1 文字目までを表したものについて, それぞれの出現しにくさ c[w]や単語同士のつながりにくさ d[w1][w2] が与えられています.
0≤j<i≤n に対して, dp[i][j] は文字列 A を i 文字目まで読み込んだとき, 最後の単語が j から始まるとしたときの最小コストとしています.
"""

def wakachikaki(A,c,d):
  n=len(A)
  w=[["" for i in range(n)] for j in range(n)]
  for i in range(n):
    for j in range(i):
      w[j][i]=A[j+1:i]
  inf=float("inf")
  dp=[[inf for i in range(n+1)] for j in range(n+1)]
  dp[0][0]=0
  for i in range(n+1):
    for j in range(n+1):
      for k in range(j):
        dp[i][j]=min(dp[i][j],dp[j][k]+c[w[j][i]]+d[w[k][j]][w[j][i])

  ans=inf
  for j in range(n):
    ans=min(ans,dp[n][j])
  return ans
