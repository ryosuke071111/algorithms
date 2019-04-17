n,a,b=map(int,input().split())
num=0
for i in range (n+1):
  if a <= sum(list(map(int,list(str(i)))))<=b:
    num+=i
print(num)
