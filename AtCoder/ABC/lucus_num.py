n = int(input())
memo={}

def ryuka(n):
  if n ==0:
    return 2
  if n == 1:
    return 1
  elif n not in memo:
    memo[n] = ryuka(n-1)+ryuka(n-2)
  return memo[n]

print(ryuka(n))
