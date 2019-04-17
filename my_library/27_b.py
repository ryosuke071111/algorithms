n=int(input())
A=list(map(int,input().split()))
everyone=sum(A)
bridge=0
debt=0
if everyone%n != 0:
  print(-1)
else:
  ave=everyone//n
  curr=0
  ans=0
  for i in A:
    curr += (i-ave) #借金のやりとりしている。貯金があったら増えるし、足りなかったら借金。
    if curr != 0:   #借金か貯金がチャラになったところでは橋を足さない。貯金使えばいいし借金を払う。
      ans = ans+1   #借金か貯金していたら橋を足す。
  print(ans)

