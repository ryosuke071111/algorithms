import numpy as np

with open('7.txt') as f:
  a = f.readlines()
  a=list(map(lambda x:x.strip("\\\n").split(","),a))
  for i in range(len(a)):
    for j in range(len(a[i])):
      a[i][j]=int(a[i][j])

area=np.array([[0 for i in range(1000)] for i in range(1000)])

#厚さの最大値
for x,y,w,h in a:
  for i in range(y,y+h):
    area[i][x:x+w]+=1
# print(np.amax(area))

from collections import deque

#クラスタの数
cluster=0

#クラスタの面積
square=0

#dfs
visited=[[False for i in range(1000)] for i in range(1000)]
xy = [(1,0),(0,-1),(-1,0),(0,1)]
for i in range(1000):
  for j in range(1000):
    if visited[i][j]==False and area[i][j]>=1:
      que=deque([(i,j)])
      tmp=0
      while que:
        y,x=que.popleft()
        if visited[y][x]== False:
          visited[y][x] = True
          tmp+=1
        for dx,dy in xy:
          if 0 <= y + dy <= 1000  and 0<=  x+ dx <=1000 and area[y+dy][x+dx]>=1 and visited[y+dy][x+dx]==False:
            que.append((y+dy,x+dx))
      cluster+=1
      square=max(tmp,square)

print("クラスタの数",cluster)
print("クラスタの面積の最大値",square)
