#11:21-11:29
n,m=map(int,input().split())
ans=0
if m<2:
  print(0)
  exit()
if n<m:
  m-=2*n
  ans+=n
  ans+=m//4
else:
  ans+=m//2
print(ans)
