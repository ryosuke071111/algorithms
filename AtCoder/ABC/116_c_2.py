# 11:50-

#①
n=int(input())
H=[0]+list(map(int,input().split()))+[0]
s=[H[i+1]-H[i] for i in range(n+1)]

ans=0
for i in s:
  if i>0:
    ans+=i
print(ans)

#②
n=int(input())
H=list(map(int,input().split()))
ans=0
i=0
while sum(H)>0:
  ans+=1
  flag=False
  for i in range(n):
    if H[i]>0:
      H[i]-=1
      flag=True
    elif H[i]==0 and flag==True:
      break
print(ans)

75 96 27 50
