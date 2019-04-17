import sys
count = 0


memo ={}
def f(n):
  if n <1:
    return 1
  elif n-1 not in memo:
    memo[n-1] = (161*f(n-1)+2457) % (2**24)
    return memo[n-1]
  else:
    return (161*memo[n-1]+2457) % (2**24)

for i in range(500,1000500,500):
  f(i)

print(f(1000000))
# print((161*memo[999999]+2457) % (2**24))

# memo ={}
# def g(n):
#   if n <1:
#     return 1
#   elif n-1 not in memo:
#     memo[n-1] = (1103515245*g(n-1)+12345) % (2**26)
#     return memo[n-1]
#   else:
#     return (1103515245*memo[n-1]+12345) % (2**26)

# for i in range(2,100000):
#   for j in range(2,100000):
#     if g(i+j) == g(i):
#       print(g(i+j),g(i))
#       # print(j)
