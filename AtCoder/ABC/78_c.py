# n,m=map(int,input().split())
# left=n-m
# sum=0
# sum+=((1900*m)+(left*100))*(2**m)
# print(int(round(sum,0)))



#連立方程式の解
n,t=map(int,input().split())
T=list(map(int,input().split()))
ans=0
for i in range(1,n):
  ans+=min(t,T[i]-T[i-1])
print(ans+t)

