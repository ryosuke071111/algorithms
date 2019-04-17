n,a,b=map(int,input().split())
cur=0
for i in range(n):
  s,d=input().split()
  d=int(d)
  if a<=d<=b:
    if s =="West":
      cur-=d
    else:
      cur+=d
  elif d<a:
    if s =="West":
      cur-=a
    else:
      cur+=a
  else:
    if s =="West":
      cur-=b
    else:
      cur+=b
if cur <0:
  print("West",abs(cur))
elif cur==0:
  print(0)
else:
  print('East',abs(cur))
