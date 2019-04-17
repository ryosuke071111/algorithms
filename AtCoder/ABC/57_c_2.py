#9:42-
n=int(input())
def f(a,b):
  a=len(str(a))
  b=len(str(b))
  return max(a,b)

ans=10**9
for i in range(1,int(n**0.5)+1):
  if n%i==0:
    ans=min(ans,f(i,n//i))
print(ans)

