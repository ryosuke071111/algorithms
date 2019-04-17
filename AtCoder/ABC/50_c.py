from collections import Counter
n=int(input())
A=list(map(int,input().split()))
mod=10**9+7
countA= Counter(A)
if n%2==1:
  for k,v in countA.items():
    if k==0:
      if v!=1:
        print(0)
        exit()
    else:
      if v!=2:
        print(0)
        exit()
  print(2**((n-1)//2)%mod)
else:
  for k,v in countA.items():
    if v!=2:
      print(0)
      exit()
  print(2**(n//2)%mod)
