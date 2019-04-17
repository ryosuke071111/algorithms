#引数にリストを入れるとその最大公約数が返ってくる

#最大公約数
def gcd(x,y):
  r=x%y
  return gcd(y,r) if r else y
#最小公倍数
def lcm(x, y):
    return (x * y) // gcd(x, y)

#リスト内最小公倍数
for i in A:
  k=lcm(k,i)
