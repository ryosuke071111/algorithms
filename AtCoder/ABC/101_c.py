n,k=map(int,input().split())
# A=list(map(int,input().split()))

i=1
if n % k ==0:
  print(n//(k-1))
  exit()
else:
  # while k+(k-1)*i< n:
  #   i+=1
  a=(n-k)//(k-1)
print(1+a+1)
