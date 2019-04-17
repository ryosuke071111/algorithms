A=[int(input()) for i in range(5)]
A.sort(key=lambda x:10-(x%10) if x%10!=0 else 0,reverse=True)
ans=0
for i in A[1:]:
  ans+=i+(10-i%10 if i%10!=0 else 0)
print(ans+A[0])
