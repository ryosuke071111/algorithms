from bisect import bisect_left
from collections import Counter

#人の答え
n = int(input())
A = list(map(int,input().split()))
A = Counter(A).most_common()
ans = 0

for i,j in sorted(A,reverse=True):
  if j >=4 and ans ==0:
    ans = i*i
    break
  elif j >= 2 and ans == 0:
    ans = i
  elif j >= 2:
    ans *= i
    break
print(ans)

from random import random

# #自分の答え
# n = int(input())
# A = list(map(int,input().split()))

# A = [i for i in A if A.count(i) >= 2]

# num = max(A)

# if len(A) == 0:
#   print(0)
#   exit()

# if A.count(num) >= 4:
#   print(num**2)
#   exit()
# elif 2<= A.count(num) < 4:
#   print(num*A[bisect_left(A,num)-1])

