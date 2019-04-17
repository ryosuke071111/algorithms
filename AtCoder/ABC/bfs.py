 from collections import deque

r,c = map(int,input().split())
sy,sx = list(map(int,input().split()))
sy,sx = sy-1,sx-1
gy,gx = list(map(int,input().split()))
gy,gx = gy-1,gx-1
xy = [(1,0),(0,-1),(-1,0),(0,1)]
visited = [[True for i in range(c)] for i in range(r)]
area = [input() for i in range(r)]
counter = [[100 for i in range(c)] for i in range(r)]

for i in range(r):
  for j in range(c):
    if area[i][j] =='.':
      visited[i][j] = False

visited[sy][sx] = True

edges = [[[] for i in range(c)] for i in range(r)]
for i in range(r):
  for j in range(c):
    for x,y in xy:
      if 0 <= i + y < r and 0<= j + x < c:
        if area[i+y][j+x] == '.':
          edges[i][j].append((i+y,j+x))


que1 = deque([sy])
que2 = deque([sx])
counter[sy][sx] =0

while len(que1) and len(que2) != 0:
  y,x = que1.popleft(), que2.popleft()
  for vy,vx in edges[y][x]:
    if visited[vy][vx] == False:
      visited[vy][vx] = True
      if area[vy][vx] == '.':
        que1.append(vy)
        que2.append(vx)
        counter[vy][vx] = counter[y][x]+1

print(counter[gy][gx])


#別解：
from collections import deque
R, C = map(int, input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())
sx, sy = sx - 1, sy - 1
gx, gy = gx - 1, gy - 1
T = [[] for i in range(R)]
for i in range(R):
    a = list(input())
    T[i] = a

que = deque([(sx,sy)])
INF= float('inf')
d = [[INF]*C for i in range(R)]
d[sx][sy] = 0
while que:
  x,y =que.popleft()
  for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
    nx,ny = x+dx,y+dy
    if 0 <= nx < R and 0 <= ny < C and d[nx][ny] == INF and T[nx][ny] =='.':
      d[nx][ny] = d[x][y] +1
      que.append((nx,ny))









