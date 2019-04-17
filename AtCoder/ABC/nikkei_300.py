#9:03-
import math
h,w,k=map(int,input().split())
H=[w]*h
W=[h]*w

half=math.ceil((h*w-k)/2)
ans=0

for i in range(k):
  r,c=map(int,input().split())
  W[c-1]-=1
  H[r-1]-=1

aa=0
for i in range(h):
  aa+=H[i]
  if aa>=half:
    chuo_w=i
    break

bb=0
for i in range(w):
  bb+=W[i]
  if bb>=half:
    chuo_h=i
    break

for i in range(h):
  ans+=abs(chuo_w-i)*H[i]
for i in range(w):
  ans+=abs(chuo_h-i)*W[i]

print(ans)

