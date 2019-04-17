n = int(input())
if n ==0:
  print(0)
s=''
while n !=0:
  #あまりが1の場合
  if n%2==1:
    #1をつける
    s="1"+s
    #1を引いた数を使ってnをわる
    n-=1
    n=-n//2
  else:
    s='0'+s
    n=-n//2
  print(n)
print(s)
