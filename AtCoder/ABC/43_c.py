#8:40-
n=int(input())
A=list(map(int,input().split()))
ans=10**9
#平均を取る戦法でも良かったが、roundにして四捨五入することで小数点単位で最も近い方に切り上げ切り下げができるので気をつける
for i in range(-100,101):
  ans=min(sum(list(map(lambda x:(x-i)**2,A))),ans)
print(ans)
