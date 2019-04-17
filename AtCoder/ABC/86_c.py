n=int(input())
plan=[list(map(int,input().split())) for i in range(n)]
pret=0
prexy=0
for t,x,y in plan:
  t_diff=t-pret
  xy_diff=abs((x+y)-prexy)
  if t_diff>=xy_diff:
    if t_diff%2==0 and xy_diff%2==0:
      pass
    elif t_diff%2==1 and xy_diff%2==1:
      pass
    else:
      print('No')
      exit()
  else:
    print('No')
    exit()
  pret=t
  prexy=x+y
print('Yes')


