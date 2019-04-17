# x,y,z,k=map(int,input().split())
# A=sorted(list(map(int,input().split())),reverse=True)
# B=sorted(list(map(int,input().split())),reverse=True)
# C=sorted(list(map(int,input().split())),reverse=True)

# tmp=[]
# for a in A:
#   for b in B:
#     tmp.append(a+b)
# tmp.sort(reverse=True)
# tmp=tmp[:k+1]

# ans=[]
# for c in C:
#   for t in tmp:
#     ans.append(c+t)

# ans.sort(reverse=True)
# for i in range(k):
#   print(ans[i])

import heapq
x,y,z,K=map(int,input().split())
A=sorted(list(map(int,input().split())),reverse=True)
B=sorted(list(map(int,input().split())),reverse=True)
C=sorted(list(map(int,input().split())),reverse=True)
q=[(-(A[0]+B[0]+C[0]),0,0,0)]
S=set()

for n in range(K):
  p,i,j,k=heapq.heappop(q)
  print(-p)
  if i+1<x and ((i+1,j,k) not in S):
    S.add((i+1,j,k))
    heapq.heappush(q,(-(A[i+1]+B[j]+C[k]),i+1,j,k))
  if j+1<y and ((i,j+1,k) not in S):
    S.add((i,j+1,k))
    heapq.heappush(q,(-(A[i]+B[j+1]+C[k]),i,j+1,k))
  if k+1<z and ((i,j,k+1) not in S):
    S.add((i,j,k+1))
    heapq.heappush(q,(-(A[i]+B[j]+C[k+1]),i,j,k+1))

