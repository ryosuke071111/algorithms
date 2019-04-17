k,a,b=map(int,input().split())
ans=0
if a+1<=k and b>a+2:
  k=k-(a+1)
  ans+=b
  mul,mod=divmod(k,2)
  ans+=(mul)*(b-a)
  ans+=mod
  print(ans)
else:
  print(1+k)
