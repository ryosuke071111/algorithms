m, n = map(int, input().split())
mod = 1000000007

def power(x,y):
  if y == 0:
    return 1
  elif y == 1:
    return x % mod
  elif y % 2 == 0:
    return power(x, y/2)**2 % mod
  else:
    return power(x, int(y/2))**2 * x % mod
ans = power(m,n)
print(ans)
