import itertools
a,b,c,d,e=map(int,input().split())
ls=[]
for i in itertools.combinations((a,b,c,d,e),3):
  ls.append(sum(i))
ls.sort()
print(ls[-3])
