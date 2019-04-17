n = int(input())
x = list(map(int, input().split()))
y = sorted(x)
a = y[n//2-1]
b = y[n//2]
for i in range(n):
  if x[i] <= a:
    print(b)
  else:
    print(a)

