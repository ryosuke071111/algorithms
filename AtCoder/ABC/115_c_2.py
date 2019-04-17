n,k=map(int,input().split())
H=[int(input()) for i in range(n)]
H.sort()
ans=10**9
for i in range(len(H)-k+1):
  ans=min(ans,abs(H[i]-H[i+k-1]))
print(ans)
