mod=2**24
memo={}
def f(n):
  if n < 1:
    return 1
  if n not in memo:
    memo[n]=(161*f(n-1)+2457) %mod
  return memo[n]

count=0
for i in range(100):
  if f(i)%2==0:
    count+=1
print(count)




