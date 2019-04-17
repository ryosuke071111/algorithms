n,m=map(int,input().split())
A=[input() for i in range(n)]
B=[input() for i in range(m)]

for i in range(n):
  for j in range(n):
    k=j+m
    if k <= n:
      if A[i][j:k]== B[0]:
        o=1
        for l in range(i+1,i+m):
          if l<n:
            if A[l][j:k]!=B[o]:
              break
            else:
              o+=1
        if o==m:
          print('Yes')
          exit()
print('No')


#赤色の人のコード
import sys

stdin = sys.stdin
def na():
  return map(int, stdin.readline().split())
def ns():
  return stdin.readline().strip()

n,m = na()
ba = []
for i in range(n):
    ba.append(ns())
bb = []
for i in range(m):
    bb.append(ns())

for i in range(n-m+1):
    for j in range(n-m+1):
        ok = True
        for k in range(m):
            if ba[i+k][j:j+m] != bb[k]:
                ok = False
                break
        if ok:
            print("Yes")
            sys.exit(0)
print("No")
