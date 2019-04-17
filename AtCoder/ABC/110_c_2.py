# 9:18-
from collections import Counter

s=input()
t=input()

if len(Counter(t))==len(Counter(s)) and len(s)==len(t):
  ls1=sorted([i for i in Counter(t).values()])
  ls2=sorted([i for i in Counter(s).values()])
  for i in range(len(ls1)):
    if ls1[i]!= ls2[i]:
      print('No')
      exit()
  print('Yes')
else:
  print("No")

