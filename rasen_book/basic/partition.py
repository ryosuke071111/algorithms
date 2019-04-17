def partition(A, p, r):
  x = A[r]
  i = p - 1
  for j in range (p, r):
    if A[j]  <= x:
      i += 1
      print('iの値は', i)
      A[i], A[j] = A[j], A[i]
  A[i+1], A[r] = A[r],A[i + 1]
  return i + 1

n = int(input())
a = list(map(int, input().split()))
i = partition(a, 0, n-1)
print('iの値は', i)
a[i] = "[" + str(a[i]) + "]"
print(" ".join(map(str, a)))

# 基準値より小さいものが来た時はi+1、iとjの数値を入れ替える
# 基準値より大きいものが来た時は場所はそのままにして置く
