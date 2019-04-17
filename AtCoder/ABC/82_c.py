#10:05-
from collections import Counter
n=int(input())
A=Counter(list(map(int,input().split())))
ans=0
for i,j in A.items():
  if j-i<0:
    ans+=j
  else:
    ans+=min((j-i),j)
print(ans)

