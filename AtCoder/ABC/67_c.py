n=int(input())
A=list(map(int,input().split()))
X=sum(A)
ans=10**100
x=0
for i in range(n-1):
  x+=A[i]
  ans=min(ans,abs(X-2*x))
print(ans)
