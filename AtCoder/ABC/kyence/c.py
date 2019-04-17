n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
D=[]
for i,j in zip(A,B):
  D.append(i-j)
ls=list(map(lambda x:x>=0,D))
if all(ls):
  print(0)
  exit()

if sum(D)<0:
  print(-1)
  exit()

en=sum(D)
for i in sorted(D,reverse=True):
  if i> 0:
    while i > 0:
      i-=1
      en-=1


