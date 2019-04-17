n,m,x=map(int,input().split())
A=[0 for i in range(n+1)]
ls=list(map(int,input().split()))
for i in ls:
  A[i]=1
print(min(sum(A[:x+1]),sum(A[x:])))
