from collections import deque
n=int(input())
s=deque(input())
ok=["a","b","c"]
count=0

while len(s)>1 and s[0] in ok and s[-1] in ok:
  if s[0]=="a" and s[-1]=="c":
    s.popleft()
    s.pop()
    count+=1
  elif s[0]=="c" and s[-1]=="a" and len(s)> 1:
    s.popleft()
    s.pop()
    count+=1
  elif s[0]=="b" and s[-1]=="b" and len(s)> 1:
    s.popleft()
    s.pop()
    count+=1
  else:
    break
if len(s)==1:
  print(count)
else:
  print(-1)

