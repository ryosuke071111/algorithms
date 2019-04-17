from functools import lru_cache

mod=2**26
mod2=2**10
memo={}

@lru_cache(maxsize=None)
def g(n):
  if n < 1:
    return 1
  if n not in memo:
    memo[n]=(1103515245*g(n-1)+12345)%mod
  return memo[n]

@lru_cache(maxsize=None)
def h(n):
  if n > 100:
    warukazu=0
    if 900 > n:
      for i in range(n-1,-1,-1):
        if n % i ==0:
          warukazu=i
          break
    else:
      for i in range(900,-1,-1):
        if n % i ==0:
          warukazu=i
          break
    tmp=0
    for i in range(0,n+warukazu-1,warukazu):
      g(i)%mod2
      if i == n:
        # print('nに到達した',n)
        return g(n)%mod2
  else:
    return g(n)%mod2


n=int(input())
flag=True
k=1
while flag:
  if h(n+k)==h(n):
    flag=False
    print('h(n+k)',h(n+k),'h(n)',h(n))
    print("答えは",k)
    exit()
  k+=1


