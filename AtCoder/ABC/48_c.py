# 18:35-
n,x=map(int,input().split())
A=list(map(int,input().split()))+[0]
ans=0
for i in range(n):
  diff=max(0,A[i]+A[i-1]-x)
  ans+=diff
  A[i]-=diff
print(ans)

