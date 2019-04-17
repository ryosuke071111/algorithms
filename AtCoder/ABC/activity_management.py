l,h=map(int,input().split())
n=int(input())

A=[int(input()) for i in range(n)]
for i in A:
  if l<= i <= h:
    print(0)
  elif h<i:
    print(-1)
  else:
    print(l-i)
