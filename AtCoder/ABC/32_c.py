#12:09-
import sys
input=sys.stdin.readline
n,k=map(int,input().split())
S=[int(input()) for i in range(n)]
tmp=1
cnt=0
ans=0
l,r=0,0

if 0 in S:
  print(n)
  exit()
for r in range(n):
  tmp*=S[r]
  if k < tmp:
    tmp//=S[l]
    l+=1
  ans=max(ans,r-l+1)
print(ans)

