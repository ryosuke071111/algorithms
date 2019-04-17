a,b=map(int,input().split())
count=0
for i in range(a,b+1):
  i=str(i)
  j=-1
  k=0
  while i[k]==i[j]:
    k+=1
    j-=1
    if k==(len(i)//2)+1:
      count+=1
      break
print(count)
