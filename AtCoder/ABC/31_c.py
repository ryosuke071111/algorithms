#9:25-
n=int(input())
A=list(map(int,input().split()))
ans=-100
for i in range(n):
  tmp=-1000
  J=-100
  #高橋くんがiの時の青木君の最大得点とそのインデックスJを確定
  for j in range(n):
    if i==j:
      continue
    l,r= sorted([i,j])
    if sum(A[l+1:r+1:2])>tmp:
      J=j
      tmp=sum(A[l+1:r+1:2])
  l,r=sorted([i,J])
  #各iについて、青木くんが最前戦略を取った時の高橋くんの最高得点を更新
  ans=max(sum(A[l:r+1:2]),ans)
print(ans)

#for文のi,jは変数に代入した方が安全（otherwise 予想外の挙動が起こる）
#i>jの時数字を入れ替えたい場合はi,j=sorted([i,j])が便利

