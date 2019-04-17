n=int(input())
X=sorted(list(map(int,input().split())))
tmp=0
for i in range(1,n):
  tmp+=i*(n-i)*(X[i]-X[i-1])
print(tmp)

