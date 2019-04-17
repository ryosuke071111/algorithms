from bisect import bisect_left
n=int(input())
A=[int(input()) for i in range(n)]
setA=sorted(list(set(A)))

for i in range(n):
  print(bisect_left(setA,A[i]))
