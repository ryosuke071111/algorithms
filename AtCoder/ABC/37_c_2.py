n,k=map(int,input().split())
A=list(map(int,input().split()))
for i in range(n-1):
  A[i+1]=A[i]+A[i+1]
ans=0
A=[0]+A
for i in range(n-k+1):
  ans+=A[i+k]-A[i]
print(ans)
