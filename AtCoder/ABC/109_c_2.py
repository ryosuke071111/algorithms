#最大公約数
def gcd(x,y):
  r=x%y
  return gcd(y,r) if r else y

n,x=map(int,input().split())
X=list(map(int,input().split()))
X.append(x)
X.sort()
X=[X[i]-X[i-1] for i in range(1,len(X))]
k=X[0]
for i in X:
  k=gcd(k,i)
print(k)
