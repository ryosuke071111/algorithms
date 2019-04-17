# #TLEになってしまう
n = int(input())
T=[int(input()) for i in range(n)]
T = sorted(T,reverse=True)

a = T[0]
i =1
while True:
  if sum(map(lambda x:T[0]%x, T)) !=0:
    T[0] += a
  else:
    print(T[0])
    exit()
  i += 1

# #正解
n = int(input())
T=[int(input()) for i in range(n)]


def euclid(a,b):
  r = a % b
  return euclid(b,r) if r else b

def lcm(a,b):
  return a * b //euclid(a,b)

num = T[0]
for i in range(1,n):
  num = lcm(num, T[i])
print(num)

