x,a,b = map(int,input().split())

if b-a <= 0:
  print("delicious")
elif b-a <= x:
  print("safe")
if b-a > x:
  print("dangerous")
