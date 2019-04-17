#12:07-
n=int(input())
A=list(map(int,input().split()))
ans=len(A)
i=0
while i+1 < len(A):
  if A[i]< A[i+1]:
    ans+=1
    tmp=1
    j=i+1
    while j+1<len(A) and A[j]<A[j+1]:
      tmp+=1
      ans+=tmp
      j+=1
    i=j
  i+=1
print(ans)

