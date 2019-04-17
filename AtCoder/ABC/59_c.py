n=int(input())
A=list(map(int,input().split()))

ans1=0
ans2=0

#最初の符号が正の場合
sign=1
total=0
for i in range(n):
  total+= A[i]
  if total*sign<=0:   #符号が正しいかを判定（正が欲しい時に正とかけたら正、逆も然り）
    k=abs(total-sign)
    ans1+=k           #理想の値との差分
    total=sign        #暫定累積値を理想の値に変更
  sign*=-1            #一回ごとに符号を変更

#最初の符号が負の場合
sign=-1
total=0
for i in range(n):
  total+=A[i]
  if total*sign<=0:
    k=abs(total-sign)
    ans2+=k
    total=sign
  sign*=-1
print(min(ans1,ans2))

# if abs(A[1]-A[0])!=0:
#   tmp=A[1]+A[0]
#   if tmp>0 and A[0]>0:
#     count+=abs(-1-(A[1]+A[0]))
#     tmp=-1
#   elif tmp<0 and A[0]<0:
#     count+=abs(1-(A[1]+A[0]))
#     tmp=1
# else:
#   count+=abs(-1-(A[1]+A[0]))
#   tmp=-1


# for i in range(2,n):
#   if tmp<0:
#     if tmp+A[i]<=0:
#       count+= abs(1-(A[i]+tmp))
#       tmp=1
#     else:
#       tmp+=A[i]
#       continue
#   else:
#     if tmp+A[i]>=0:
#       count+=abs(-1-(A[i]+tmp))
#       tmp=-1
#     else:
#       tmp+=A[i]
#       continue
# print(count)


