n,q=map(int,input().split())
s=input()
ls=[0]*n
i=1
while i < len(s):
  if s[i-1]+s[i]=="AC":
    ls[i]=1
  i+=1
for i in range(len(ls)-1):
  ls[i+1]=ls[i+1]+ls[i]

for i in range(q):
  l,r=map(int,input().split())
  print(ls[r-1]-ls[l-1])
