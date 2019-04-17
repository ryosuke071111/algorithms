#8:43-

#引数にリストを入れるとその最小公倍数が返ってくる

def gcd(x,y):
  r=x%y
  return gcd(y,r) if r else y

def lcm(x, y):
    return (x * y) // gcd(x, y)

n=int(input())
A=list(map(int,input().split()))
k=1
for i in A:
  k=lcm(k,i)
def f(n):
  return sum(list(map(lambda x:n%x,A)))
print(f(k-1))


