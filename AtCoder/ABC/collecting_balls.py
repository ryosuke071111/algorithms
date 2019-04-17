n=int(input())
k=int(input())
X=list(map(int,(input().split())))
ans=0
for i in X:
  ans+= 2*(min(abs(i-k),abs(i)))
print(ans)
