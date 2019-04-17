memo={}
def f(x):
  if x<=2:
    return 1
  else:
    if x not in memo:
      memo[x]=f(x-1)+f(x-2)
    return memo[x]
print(f(10))
print(memo)
