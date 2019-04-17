n=int(input())
d,x=map(int,input().split())
chocho=0

for i in range(n):
  j=1
  chocho+=1
  A=int(input())
  tmp=j*A+1
  while tmp <= d:
    j+=1
    tmp=j*A+1
    chocho+=1
print(chocho+x)


