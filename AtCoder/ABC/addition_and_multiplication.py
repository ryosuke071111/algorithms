n=int(input())
k=int(input())
num=1
for i in range(n):
  num = min(2*num,num+k)
print(num)
