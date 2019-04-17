#11:47-
n,k=map(int,input().split())
ls={}
for i in range(n):
  a,b=map(int,input().split())
  if a not in ls:
    ls[a]=b
  else:
    ls[a]+=b
ls=sorted(ls.items())
tmp=0
for i,j in ls:
  tmp+=j
  if k <= tmp:
    print(i)
    exit()

