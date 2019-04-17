#10:35-
flag=True
n=int(input())
A=list(map(int,input().split()))
cnt=0
while flag:
  ls=[]
  tmp=False
  for a in A:
    if a%2==0:
      tmp=True
      cnt+=1
      ls.append(a//2)
  A=ls
  if tmp==False:
    flag=False
print(cnt)



