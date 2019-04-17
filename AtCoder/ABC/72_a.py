# n,k=map(int,input().split())
# A=sorted(list(map(int,input().split())))
# tmp=0
# for i in range(1,k):
#   tmp+=i
# print(sum(A[:k])+tmp)

n=int(input())
A=list(map(int,input().split()))
ans=0
for i in range(n):
  if i+1==A[A[i]-1]:
    ans+=1
print(ans//2)
