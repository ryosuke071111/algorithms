n=int(input())
L=sorted(list(map(int,input().split())))
if L[-1]<sum(L[:-1]):
  print("Yes")
else:
  print('No')

