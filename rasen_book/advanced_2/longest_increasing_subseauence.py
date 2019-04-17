import bisect
n = int(input())
A =[]


for i in range(n):
  A.append(int(input()))

L = [A[0]]

for i in A:
  if L[-1] < i:
    L.append(i)
  else:
    L[bisect.bisect_left(L, i)] = i

print(len(L))
#一言：数列から昇順になる数字の長さを出力
#プロセス：L[]に常に左から順番に昇順で並んでいる最小値を入れる→lengthをカウントで増やしていく
#計算量：O(nlog)⇦O(n^2) 最小値をbisectで見つけて、後ろにつけていく

import bisect
n =int(input())
A =[]

for i in range(n):
  A.append(int(input()))

L = A[[0]]

for i in A:
  if[L-1] < i:
    L.append(i)
  else:
    L[bisect.bisect_left(L,1)] = i

