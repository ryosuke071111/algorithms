import math
from collections import Counter

#ある数を素因数分解する
def prime_factors(n):
  i = 2
  factors = []
  while i * i <= n:
    if n % i==0:
      n //= i
      factors.append(i)
    else:
      i += 1
  if n > 1:
    factors.append(n)
  return factors

mod=10**9+7
n=int(input())
#階乗を求める
num=math.factorial(n)
#階乗を素因数分解する
factors=prime_factors(num)
#素因数分解の指数をまとめ上げる
indices=Counter(factors)

ans=1
#まとめ上げた指数の個数+1の掛け算
for i in indices.values():
  ans*=i+1
print(ans%mod)

