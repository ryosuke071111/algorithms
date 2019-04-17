n=int(input())
s=input()
x=0
tmp=0

for i in s:
  if i=="I":
    x +=1
  else:
    x -= 1
  tmp=max(x,tmp)
print(tmp)
