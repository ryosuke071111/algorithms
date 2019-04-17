n,q=map(int,input().split())
pro=[0 for i in range(n)]
for i in range(q):
  l,r,t=map(int,input().split())
  pro[l-1:r]=[t]*(r-l+1)

for i in pro:
  print(i)
