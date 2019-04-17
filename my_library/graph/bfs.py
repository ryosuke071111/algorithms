from collections import deque
que=deque([])

visited=[False]*n

while len(que)!= 0:
  u = que.popleft()
  for e in edges[u]:
    if visited[e] == False:
      visited[e] = True
      if area[e] == '.':
        que.append(e)

