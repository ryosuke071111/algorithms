w,a,b=map(int,input().split())

if a!=b:
  if w>abs(a-b):
    print(0)
  else:
    edge=min(a,b)
    print(max(a,b)-(edge+w))
else:
  print(0)
