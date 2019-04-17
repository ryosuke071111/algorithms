is_prime=[True]*(10**6+1)
for i in range(2,10**6+1):
  if is_prime[i]:
    for j in range(2*i,10**6+1,i):
      is_prime[j]=False
is_prime[0],is_prime[1]=False,False

ls=[]
while True:
  a,b,c=map(int,input().split())
  if a==0 and b==0 and c==0:
    break
  ls.append([a,b,c])

print('-'*20)

for i in range(len(ls)):
  a,d,n=ls[i][0],ls[i][1],ls[i][2]
  if a==0 and d==0 and n==0:
    break
  count=0
  while True:
    if is_prime[a]==True:
      count+=1
      if count==n:
        print(a)
        break
    a+=d



