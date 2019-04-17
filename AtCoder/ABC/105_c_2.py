#12:08-
n = int(input())
if n ==0:
  print(0)
s=''
while n !=0:
  if n%2==1:
    s="1"+s
    n-=1
  else:
    s='0'+s
  n=-n//2
print(s)


n=int(input())
if n==0:
  print(0)
else:
  s= ""
while n!=0:
  if n%2==1:
    s="1"+s
    n-=1
  else:
    s="0"+s
  n=n//2
