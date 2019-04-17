from collections import deque

A=deque(input())
B=deque(input())
C=deque(input())

turn={"a":A,"b":B,"c":C}

next = A.popleft()

flag = True
while flag:
  if len(turn[next]) != 0:
    next = turn[next].popleft()
  else:
    print(next.upper())
    break


