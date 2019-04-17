wt,ht,n=map(int,input().split())
# XYA=[list(map(int,input().split())) for i in range(n)]

w=[1]*wt
h=[1]*ht
for i in range(n):
  W,Y,A=map(int,input().split())
  if A==1:
    w=[0]*(W)+w[W:]
  elif A==2:
    w=w[:W]+[0]*(wt-W)
  elif A==3:
    h=h[:ht-(Y+1)+1]+[0]*(Y)
  elif A==4:
    h=[0]*(ht-Y)+h[ht-Y:]

print(sum(w)*sum(h))

