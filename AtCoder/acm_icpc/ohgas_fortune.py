import math
m=int(input())
ans=[]
for i in range(m):
  initial_money=int(input())
  management_yrs=int(input())
  num_of_management=int(input())
  tmp=0
  for j in range(num_of_management):
    op,rate,fee=map(float,input().split())
    interest,fee=int(op),int(fee)
    money=initial_money
    profit=0
    if op==0:
      for k in range(management_yrs):
        profit+=math.floor(money*rate)
        money-=fee
      final=money+profit
    else:
      for k in range(management_yrs):
        profit=math.floor(money*rate)
        money+=profit-fee
      final=round(money,0)
    tmp=max(final,tmp)
  ans.append(tmp)

for i in ans:
  print(i)






#最終資金を最大にする運用方法の最終資金
