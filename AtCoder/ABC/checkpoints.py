n,m=map(int,input().split())
AB=[]
CD=[]
for i in range(n):
  AB.append(list(map(int,input().split())))
for i in range(m):
  CD.append(list(map(int,input().split())))

for a,b in AB:
  dis=[abs(a-c)+abs(b-d) for c,d in CD]
  print(dis.index(min(dis))+1)
