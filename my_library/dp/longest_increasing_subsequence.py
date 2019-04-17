import bisect
N = int(input())
A = [int(input()) for _ in range(N)]
L = [A[0]]

for a in A[1:]:
  # print("変更前", L)
  if L[-1] < a:
    L.append(a)
  else:
    L[bisect.bisect_left(L,a)] = a
  # print("変更後", L)
    # print(L[bisect.bisect_left(L,a)])
print(len(L))
