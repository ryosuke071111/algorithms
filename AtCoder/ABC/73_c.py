#10:28-
from collections import Counter
n=int(input())
A=Counter([int(input()) for i in range(n)])
ans=sum([1 if i%2==1 else 0 for i in A.values()])
print(ans)

#偶奇判定
