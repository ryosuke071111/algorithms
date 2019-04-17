n=int(input())
list=[2**(1*i) for i in range(7)]
ans=1000
sol=0
for i in list:
  if i <= n:
    dis=abs(i-n)
    if dis < ans:
      ans=dis
      sol=i
print(sol)

