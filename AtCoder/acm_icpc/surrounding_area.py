import sys
sys.setrecursionlimit(1000000)
while True:
  w,h=map(int,input().split())
  if w==0:
    break
  mp=["X"+input()+"X" for _ in range(h)]
  mp.insert(0,"X"*(w+2))
  mp.append('X'*(w+2))
  print(mp)

  visited_w=[[False]*(w+2) for _ in range(h+2)]
  visited_b=[[False]*(w+2) for _ in range(h+2)]
  vec=((0,1),(0,-1),(1,0),(-1,0))
  # print(visited_b)

  def search(x,y,visited):
    for dx, dy in vec:
      nx,ny=x+dx,y+dy
      if not visited[ny][nx] and mp[ny][nx]==".":
        visited[ny][nx]=True
        search(nx,ny,visited)

  for y in range(1,h+1):
    for x in range(1,w+1):
      if mp[y][x]=="W":
        search(x,y,visited_w)
      elif mp[y][x]=="B":
        search(x,y,visited_b)

  ans_w=ans_b=0

  for y in range(1,h+1):
    for x in range(1,w+1):
      if visited_w[y][x] and not visited_b[y][x]:
        ans_w +=1
      elif not visited_w[y][x] and visited_b[y][x]:
        ans_b+=1
  print(ans_b,ans_w)
