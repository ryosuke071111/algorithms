# #9:21-
n,m=map(int,input().split())
s=input()
t=input()

def gcd(x,y):
  r=x%y
  return gcd(y,r) if r else y
#最小公倍数
def lcm(x, y):
    return (x * y) // gcd(x, y)

L=lcm(n,m)
g=gcd(n,m)
for i in range(g):
  if s[int(i*n/g)]!=t[int(i*m/g)]:
    print(-1)
    exit()
print(L)


# ##間違った答え(メモリエラーになる)
# n,m=map(int,input().split())
# s=input()
# t=input()

# def gcd(x,y):
#   r=x%y
#   return gcd(y,r) if r else y
# #最小公倍数
# def lcm(x, y):
#     return (x * y) // gcd(x, y)

# L=lcm(n,m)
# if s[0]==t[0]:
#   X=[""]*(L+1)
# else:
#   print(-1)
#   exit()
# for i in range(1,n):
#   X[int(i*L/n)+1]=s[i]
# for i in range(1,m):
#   if X[int(i*L/m)+1] !="":
#     if X[int(i*L/m)+1] !=t[i]:
#       print(-1)
#       exit()
# print(L)
