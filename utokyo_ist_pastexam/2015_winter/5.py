mod=2**26
memo={}
def g(n):
  if n < 1:
    return 1
  if n not in memo:
    memo[n]=(1103515245*g(n-1)+12345)%mod
  return memo[n]
print(g(2))
print(g(3))
