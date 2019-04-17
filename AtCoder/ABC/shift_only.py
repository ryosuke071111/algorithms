#lambda
n=int(input())
A=list(map(int,input().split()))
count=0

while True:
  if (sum(list(map(lambda x:x%2,A))))!= False:
    print(count)
    exit()
  else:
    A=list(map(lambda x:x/2,A))
    count+=1
