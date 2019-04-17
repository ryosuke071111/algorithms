N=int(input())
K=int(input())
X=int(input())
Y=int(input())

extra = N-K
if extra < 0:
  extra = 0
  K = N
print(X*K+Y*extra)
