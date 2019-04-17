n=int(input())
T=[0]+list(map(int,input().split()))
m=int(input())
PX=[list(map(int,input().split())) for i in range(m)]


for i,j in PX:
  tmp=T[:i]+[j]+T[i+1:]
  print(sum(tmp))
