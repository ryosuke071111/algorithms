from collections import deque
h,w=map(int,input().split())
frame=["#"*(w+2)]
for i in range(h):
  frame.append("#"+input()+"#")

frame.append("#"*(w+2))
for i in frame:
  print(i)
