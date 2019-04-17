#17:48-
n=int(input())
A=sorted(list(map(int,input().split())))
g=A[0]

def gcd(a,b):
  while b:
    a,b=b,a%b
  return a

for a in A:
  g=gcd(g,a)
print(g)
