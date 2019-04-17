#10:42-
from bisect import bisect_left
n,m=map(int,input().split())
ls=[[] for i in range(n)]
py=[]
for i in range(m):
  p,y=map(int,input().split())
  ls[p-1].append(y)
  py.append([p,y])
ls=list(map(lambda x:sorted(x),ls))
for i in range(m):
  p,y=py[i]
  index= bisect_left(ls[p-1],y)
  print(str(p).zfill(6)+str(index+1).zfill(6))
