a,b,c,d=map(int,input().split())
ls=[a,b,c,d]
num=[1,9,7,4]
for i in num:
  if i in ls:
    ls.remove(i)
if len(ls)==0:
  print('YES')
else:
  print('NO')

