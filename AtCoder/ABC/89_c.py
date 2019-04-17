# from collections import Counter
import itertools
ans=0
n=int(input())
ls=["M","A","R","C","H"]
S = [input() for _ in range(n)]

march={i:0 for i in ls}
for s in S:
  if s[0] in ls:
    march[s[0]]+=1
for i,j,k in itertools.combinations(ls,3):
  ans+=march[i]*march[j]*march[k]
print(ans)
