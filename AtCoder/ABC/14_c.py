#10:52-
from itertools import accumulate
import sys
input=sys.stdin.readline
n=int(input())
imos=[0]*(10**6+2)
for i in range(n):
  a,b=map(int,input().split())
  imos[a]+=1
  imos[b+1]-=1
print(max(accumulate(imos)))

