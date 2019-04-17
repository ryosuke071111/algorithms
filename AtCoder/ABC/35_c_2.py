n,q=map(int,input().split())
imos=[0]*(n+2)
for i in range(q):
  l,r=map(int,input().split())
  imos[l]+=1
  imos[r+1]-=1
for i in range(len(imos)-1):
  imos[i+1]+=imos[i]
print("".join(list(map(lambda x:"0" if x%2==0 else "1",imos[1:-1]))))
