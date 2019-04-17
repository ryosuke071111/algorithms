n,k=map(int,input().split())
A=list(map(int,input().split()))
bit_max=40
ans=0

#1ビットずつ見ていく
for c in range(bit_max,-1,-1):
  #2ビット表現を大きい方から順に小さくしていく
  Xi = 1<<c
  #Aの中でk番目にビットが立っているものの数
  ck=len([1 for a in A if a&Xi!=0])
  tmp=ck
  #もしckの値がn-ckより小さいならn-ck個を採用
  if Xi<= k and ck<=n-ck:
    #ckの値を変更
    tmp=n-ck
    k-=Xi
  contribution=Xi*tmp
  ans+=contribution
print(ans)


