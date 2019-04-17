n,k=map(int,input().split())
H=sorted([int(input()) for i in range(n)])
dif=10**9
for i in range(n-k+1):
  dif=min(dif,abs(H[i+k-1]-H[i]))
print(dif)
