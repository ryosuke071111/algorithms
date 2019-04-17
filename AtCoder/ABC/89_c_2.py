import itertools
from collections import Counter
n=int(input())
S=[input()[0] for i in range(n)]
ls=["M","A","R","C","H"]
S=Counter([i for i in S if i in ls])
ans=0
for i,j,k in itertools.combinations(ls,3):
  ans+=S[i]*S[j]*S[k]
print(ans)
