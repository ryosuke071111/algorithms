n = int(input())
sunuke = 1
for i in range(1, n+1):
  sunuke = sunuke * i % 1000000007

print(sunuke)

#別解（階乗計算をしている）
from math import factorial
n = int(input())
print(factorial(n) % (10**9 + 7))
