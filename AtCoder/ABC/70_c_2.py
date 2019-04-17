def gcd(x,y):
  r=x%y
  return gcd(y,r) if r else y
#最小公倍数
def lcm(x, y):
    return (x * y) // gcd(x, y)

n=int(input())
A=[int(input()) for i in range(n)]

#リスト内最小公倍数
k=A[0]
for i in A[1:]:
  k=lcm(k,i)
print(k)

