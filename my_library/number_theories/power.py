m,n=map(int,input().split())
print(pow(m,n,1000000007))

# #pow（x, y, z） xのy乗の答えを返す。zは1000..7で割った時のあまり

#普通に計算したとき
mod =1000000007
l = input().split()
m = int(l[0])
n = int(l[1])

def power(x, y):
  if y ==0:
    return 1
  elif y == 1:
    return x % mod
  elif y % 2 ==0:
    return power(x, y/2)**2 % mod
  else:
    return power(x, int(y/2))**2 * x % mod
ans = power(m, n)
print(ans)
