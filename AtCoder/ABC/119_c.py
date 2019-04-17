# #深さ優先探索で列挙するパターン
N,A,B,C=map(int,input().split())
l=[int(input()) for i in range(N)]
inf=10**9
def dfs(cur,a,b,c):
  if cur==N:
    return abs(a-A)+abs(b-B)+abs(c-C)-30 if min(a,b,c)>0 else inf
  ret0 = dfs(cur+1,a,b,c)
  ret1 = dfs(cur+1,a+l[cur],b,c)+10
  ret2 = dfs(cur+1,a,b+l[cur],c)+10
  ret3 = dfs(cur+1,a,b,c+l[cur])+10
  return min(ret0,ret1,ret2,ret3)
print(dfs(0,0,0,0))


#itertoolsのver
import itertools
n,a,b,c=(map(int,input().split()))
l=[int(input()) for i in range(n)]
ans=10**9
for k in itertools.product(range(4),repeat=n):
    A=[[] for i in range(4)]
    for i in range(n):
        A[k[i]]+=[l[i]]
    print(A)
    if A[1] and A[2] and A[3]:
        tmp=10*(n-len(A[0])-3) #A[0]が少なければ少ないほどコストが増える(=なんども合成してる、最初の3回は合成していない)
        tmp+=abs(a-sum(A[1]))
        tmp+=abs(b-sum(A[2]))
        tmp+=abs(c-sum(A[3]))
        ans=min(tmp,ans)
print(ans)

#bit演算のパターン
n,A,B,C=(map(int,input().split()))
l=[int(input()) for i in range(n)]
ans=10**9
a=b=c=[]
for i in range(1<<n):
    for j in range(1<<n):
        res=0
        a=b=c=[]
        for k in range(n):
            if i&(1<<k):
                if j&(1<<k):
                    b.append(l[k])
                else:
                    a.append(l[k])
            elif j&(1<<k):
                c.append(l[k])
        if a and b and c:
            res = 10*(len(a)-1)+abs(A-sum(a))+10*(len(b)-1)+abs(B-sum(b))+10*(len(c)-1)+abs(C-sum(c))
            ans=min(ans,res)
print(ans)


