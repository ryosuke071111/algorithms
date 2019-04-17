mod=2**26
memo={}
memo1={}
def g(n):
  if n < 1:
    memo[n]=1
    return 1
  if n not in memo:
    memo[n]=(1103515245*g(n-1)+12345)%mod
    a=memo[n]
    if a not in memo1:
      memo1[a]=1
    else:
      memo1[a]+=1
  return memo[n]

n=int(input())
flag=True
k=1
while flag:
  if g(n+k)==g(n):
    flag=False
    print(k)
    print("g(n+k)は",g(n+k),"g(n)は",g(n))
    exit()
  k+=1


#n+k=n mod a になる求め方：k==modの時っぽい（modの世界でループするから）
#余剰定理

