def gcd(m, n):
  r = m % n
  return gcd(n, r) if r else n

print(gcd(*map(int, input().split())))
