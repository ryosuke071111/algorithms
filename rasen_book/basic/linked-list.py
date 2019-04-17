from collections import deque
n = int(input())
q = deque()

for i in range(n):
  cmd = input().split()
  if cmd[0] == "insert":
    q.appendleft(cmd[1])
  elif cmd[0] == "delete":
    try:
      q.remove(cmd[1])
    except ValueError :
      pass
  elif cmd[0] == "deleteFirst":
    q.popleft()
  elif cmd[0] == "deleteLast":
    q.pop()
print(" ".join(q))
