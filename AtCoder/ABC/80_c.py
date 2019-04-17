#9:08-
import sys
input=sys.stdin.readline
n=int(input())
F=[list(map(int,input().split())) for i in range(n)]
P=[list(map(int,input().split())) for i in range(n)]
ans=-10**9
for i in range(1,2**10):
  tmp=0
  for j in range(n):
    f,p=F[j],P[j]
    cnt=0
    for k in range(10):
      if (i>>k)&1 and f[k]:
        cnt+= 1
    tmp+=p[cnt]
  ans=max(ans,tmp)
print(ans)

#josinoお姉ちゃんの営業時間は固定（他のお店ごとにバラバラではない）
#その時に他のお店とどのくらい被っているか
