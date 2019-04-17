import numpy as np

with open('7.txt') as f:
  a = f.read().split('\n')
  a.pop()
  a.pop()
  a=list(map(lambda x:x.split(),a))
  for i in range(len(a)):
    for j in range(len(a[i])):
      a[i][j]=int(a[i][j])
pile=0

# # ---------------------------------------------
area=np.array([[0 for i in range(10)] for i in range(10)])

#厚さの最大値
for x,y,w,h in a:
  for i in range(y,y+h):
    area[i,x:x+w]+=1
    print(area[3::,3::]+1)
# print(np.amax(area))

from collections import deque

#クラスタの数
cluster=0

#クラスタの面積
square=0
tmp=0
xy = [(1,0),(0,-1),(-1,0),(0,1)]
for i in range(30):
  for j in range(30):
    if area[i][j]>=1:
      que=deque([(i,j)])
      tmp=0
      while que:
        y,x=que.popleft()
        for dx,dy in xy:
          if 0 <= y + dy <= 1000  and 0<=  x+ dx <=1000 and area[y+dy][x+dx]>=1:
            tmp+=1
            area[y+dy][x+dx]=0
            que.append((y+dy,x+dx))
      # cluster+=1
    square=max(tmp,square)

print("クラスタの数",cluster)
print("クラスタの面積の最大値",square)
