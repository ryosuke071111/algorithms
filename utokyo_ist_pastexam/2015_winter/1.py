mod=2**24
memo={}
def f(n):
  if n <  1:
    return 1
  if n not in memo:
    memo[n]=(161*f(n-1)+2457) %mod
  return memo[n]

print(f(100))
