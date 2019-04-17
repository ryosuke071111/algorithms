n=int(input())
s=input()
W=[0]*n
E=[0]*n
W[0]=1 if s[0]=="W" else 0
for i in range(n-1):
  W[i+1]=W[i]+ (1 if s[i+1]=="W" else 0)
  E[i+1]=(i+2)-W[i+1]
ans=E[-1]-E[0]
for i in range(1,n):
  ans=min(ans,(W[i-1]+E[-1]-E[i]))
print(ans)
