memo = {} #メモ化されないと時間がかかる
def fib(n):
  if n == 0 or n == 1:
    return 1
  # else:
  #   return fib(n-1) + fib(n-2)
  else:
    if n-1 not in memo:
      memo[n-1] =fib(n-1)
    if n-2 not in memo:
      memo[n-2] = fib(n-2)
    return memo[n-1]+memo[n-2]
print(fib(int(input())))
