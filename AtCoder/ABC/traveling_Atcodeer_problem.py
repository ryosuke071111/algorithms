n = int(input())
A = list(map(int,input().split()))
A.sort()
num=0
for i in range(1, len(A)):
  num += A[i] - A[i-1]

print(num)
