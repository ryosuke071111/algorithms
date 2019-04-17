#10:26-
from collections import Counter
n,k=map(int,input().split())
A=Counter(list(map(int,input().split()))).most_common()
diff=len(A)-k
A=A[::-1]
if diff==0:
  print(0)
else:
  print(sum(list(map(lambda x:x[1],A[:diff]))))
