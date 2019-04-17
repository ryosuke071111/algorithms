n,k=map(int,input().split())
X=list(map(int,input().split()))
ans=10**9
for i in range(n-k+1):
  l=X[i]
  r=X[i+k-1]
#右端と左端の区間の差を取ること
  #=結局10 20 30 40の区間それぞれの幅を取ること
  #=かつ、左端or右端を足すことは、0か はみ出ている分の絶対値を足すこと
  route1=abs(l)+r-l
  route2=abs(r)+r-l
  tmp=min(route1,route2)
  ans=min(ans,tmp)
print(ans)


#間違いコード
# import numpy as np
# n,k=map(int,input().split())
# X=list(map(int,input().split()))
# dis=10**9
# X.append(0)
# X.sort()

# if len(X)==2:
#   print(0)
#   exit()

# for i in range(n-k):
#   tmp=0
#   for j in range(i,i+k):
#     if j+1<n:
#       if np.sign(X[j+1])== np.sign(X[j]):
#         tmp += abs(X[j+1]-X[j])
#       else:
#         tmp += abs(X[j+1]-X[j])
#         tmp += abs(X[j])
#   dis=min(dis,tmp)
# print(dis)
