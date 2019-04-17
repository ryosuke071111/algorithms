#強い人のコード
N=int(input())
ans='Yes'
odd=0
four=0
for x in map(int,input().split()):
    if x%2==1:
        odd+=1
    elif x%4==0:
        four+=1
#4の倍数+1が奇数の数より少ないとダメ
if four+1<odd:
    ans='No'
#4の倍数+1が奇数と同じかつその合計が全体より少ないとダメ（ひとつ奇数が余ることになる）
elif four+1==odd and odd+four<N:
    ans='No'
print(ans)


#自分のコード
# with open('1_11.txt') as f:
#   a = f.readlines()       #行ごとに読み込んでリスト

# n=int(a[0])
# A=list(map(int,(a[1].split())))
n=int(input())
A=list(map(int,input().split()))
four=list(filter(lambda x:x%4==0,A))
even=list(filter(lambda x:x%2==0,A))
odd=list(filter(lambda x:x%2==1,A))
# print(len(even))
# print(len(odd))
# print(len(four))

#全ての成分が偶数
if len(even)==len(A):
  print('Yes')
  exit()
#4の倍数が奇数の半分以上ある（切り下げ）かつ2の倍数が偶数個かつ元が偶数個
if len(four)>=len(odd)/2 and (len(even)-len(four))%2==0:
  if (len(even)-len(four))%2>0:
    print('Yes')
    print('aa')
    exit()
# #4の倍数が奇数の半分以上ある（切り上げ）かつ4の倍数が奇数個あるかつ2の倍数が奇数個あるかつ元が奇数個
if len(four)>=len(odd)/2 and len(four)%2!=0 and len(A)%2!=0:
  print('Yes')
  exit()
if len(four)>=len(odd)/2 and len(four)%2==0 and len(A)%2==0:
  print('Yes')
  exit()
else:
  print('No')
