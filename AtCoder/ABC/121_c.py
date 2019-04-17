from collections import Counter
n,m=map(int,input().split())
ls=[list(map(int,input().split())) for i in range(n)]
ls.sort(key=lambda x:x[0])
ans=0
tmp=0
# print(ls)
for i in range(len(ls)):
  if tmp+ls[i][1]<=m:
    tmp+=ls[i][1]
    ans+=ls[i][0]*ls[i][1]
  else:
    ans+=ls[i][0]*(m-tmp)
    print(ans)
    exit()
print(ans)
