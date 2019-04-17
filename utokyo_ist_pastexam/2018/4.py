from collections import deque
m,n,s=map(int,input().split())
A=[[1]*n for i in range(m)]
B=[[1]*m for i in range(n)]
C=[[0]*m for i in range(m)]

cache=deque([])

cnt=0
cnt1=0
for i in range(m):
  for j in range(m):
    for k in range(n):
      C[i][j]+=A[i][k]*B[k][j]
      cnt+=2
      cnt1+=2
      if ["A",i,k] in cache:
        cnt-=1
        cache.append(cache.remove(["A",i,k]))
      else:
        if len(cache)<s:
          cache.append(["A",i,k])
        else:
          cache.popleft()
          cache.append(["A",i,k])
      if ["B",k,j] in cache:
        cnt-=1
        cache.append(cache.remove(["B",k,j]))
      else:
        if len(cache)<s:
          cache.append(["B",k,j])
        else:
          cache.popleft()
          cache.append(["B",k,j])
print("キャッシュヒット率:",(cnt1-(cnt1-cnt))/cnt1)



