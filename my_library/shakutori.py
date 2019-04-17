n,k=map(int,input().split())
S=[int(input()) for i in range(n)]
tmp=1
cnt=0
ans=0
l,r=0,0 #左端と右端を設定

# if not 0 in S:

#右端が数列の最後にたどり着くまで
for r in range(n):
  tmp*=S[r] #答えに右端をかける
  if k < tmp: #答えが条件より大きくなった場合には
    tmp//=S[l] #左端を答えから削る
    l+=1       #左端を進める
  ans=max(ans,r-l+1) #右と左の差分を計算
print(ans)

# else:
#   print(n)
