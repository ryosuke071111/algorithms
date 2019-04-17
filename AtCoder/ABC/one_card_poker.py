a,b= map(int,input().split())

if a == 1:
  a = 15
if b == 1:
  b = 15

if a == b:
  print('Draw')
elif a > b:
  print('Alice')
else:
  print('Bob')
