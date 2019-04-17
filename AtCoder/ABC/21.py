n=int(input())
a,b=map(int,input().split())
k=int(input())
P=list(map(int,input().split()))
P.append(a)
P.append(b)
ls= set(P)


if len(ls) != len(P):
  print('NO')
else:
  print('YES')
