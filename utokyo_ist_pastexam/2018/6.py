from collections import deque
from functools import lru_cache

m,n,p,s=map(int,input().split())


A=[[1]*n for i in range(m)]
B=[[1]*m for i in range(n)]
C=[[0]*m for i in range(m)]

cache=deque([])

@lru_cache(maxsize=None)
def count(i,k,j,cnt):
  global A
  global B
  global C
  i,k,j=i,k,j
  cnt=cnt
  C[i][j]+=A[i][k]*B[k][j]
  cnt+=2
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

  return i,k,j,cnt


cnt=0
u=0
while u<m:
  v=0
  while v < m:
    w = 0
    while w < n:
      i=u
      while i < u+p:
        j = v
        while j < v + p:
          k=w
          while k < w+p:
            i,k,j,cnt=count(i,k,j,cnt)
            k+=1
          j+=1
        i+=1
      w+=p
    v+=p
  u+=p

print(cnt)

