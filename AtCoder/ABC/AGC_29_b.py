n=int(input())
A=list(map(int,input().split()))
count=0
for i in range(1,len(A)):
  if A[i-1]==A[i]:
    count+=1
  elif A[i-1]>A[i]:
    try:
      if flag==1:
        count+=1
    except NameError:
      count  +=1
  elif A[i-1]<A[i]:
    flag=1
    continue
  flag=0
print(count+1)

