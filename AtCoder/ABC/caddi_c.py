from collections import deque,Counter
n,p=map(int,input().split())

if p==1:
  print(1)
  exit()
if p==1:
  print(p)
  exit()

#素因数分解
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:  #√xの範囲まで検証
        if n % i:      #iで割り切れないならiを増やす
            i += 1
        else:
            n //= i   #割り切れるならiでnを割る
            factors.append(i)
    if n > 1:         #残った数が1以上ならそれも張る
        factors.append(n)
    print(factors)
    return factors


for i,v in factors.items():
  ans*=i**(v//n)


factors=Counter(prime_factors(p))
ans=1
for i,v in factors.items():
  ans*=i**(v//n)
  print("ans",ans)
print(ans)




