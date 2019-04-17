n=int(input())
A=list(map(int,input().split()))
B=[2,4,5,6,8,10]
count=0
for i in A:
  while i in B:
    i-=1
    count+=1
print(count)
