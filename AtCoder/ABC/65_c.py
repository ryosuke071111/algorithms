#9:35-
from math import factorial
n,m=map(int,input().split())
mod= 10**9+7

if n-m==1 or m-n==1:
  print(factorial(n)*factorial(m)%mod)
elif n==m:
  print(2*factorial(n)*factorial(m)%mod)
else:
  print(0)

"""
順列の問題（並べ方の問題）
https://atcoder.jp/contests/abc065/tasks/arc076_a
①n==mの時下記のように並べ方が二種類ある
●○●○●○
○●○●○●

②n=m+1 or m=n+1の時、下記のように一意に確定
●○●
○●○

③それ以外は条件に合わない（=つまり0で良い）
0とすることもある。文章の条件に合わないことは0にすることもあるよ。
"""
