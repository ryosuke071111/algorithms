f=open('data1.txt')
f=f.readlines()
f=list(map(lambda x:x.strip('\n').strip('(').strip(')'),f))
f=list(map(lambda x:x.split(','),f))
max_y=0
ans=[]
xs=[]
ys=[]
for i,v in f:
  if int(v)>max_y:
    max_y=int(v)
    ans=[i,v]
print(ans)
