# 11:29-
import math
n=int(input())
ceil=math.ceil(math.sqrt(n))
def f(a,b):
  return max(len(str(a)),len(str(b)))
tmp=10**9
for a in range(1,ceil+1):
  if n%a==0:
    b=n//a
    tmp=min(tmp,f(a,b))
print(tmp)
