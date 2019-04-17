n,m,c=map(int,input().split())
B=list(map(int,input().split()))
ans=0
for i in range(n):
  A=list(map(int,input().split()))
  tmp=0
  for j in range(m):
    tmp+=A[j]*B[j]
  if tmp+c>0:
    ans+=1
print(ans)
