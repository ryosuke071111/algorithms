mod=2**24
from sys import setrecursionlimit

memo={}
def f(n):
  if n < 1:
    return 1
  if n not in memo:
    memo[n]=(161*f(n-1)+2457) %mod
  return memo[n]

for i in range(100,1000100,100):
  f(i)

print(memo[1000000])
