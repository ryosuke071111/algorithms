# #17:02-

#O(n^2)
N,Y=map(int,input().split())
for x in range(N+1):
  for y in range(N-x+1):
    z=N-x-y
    if 10000*x+5000*y+1000*z==Y and z>=0:
      print(x,y,z)
      exit()
print(-1,-1,-1)

#O(n)
N,Y=map(int,input().split())
tmp1000=N*1000
if tmp1000>Y:
  print(-1,-1,-1)
  exit()
dif= y-tmp1000
for y in range(dif//4000+1):
  tmp5000=y*4000
  if dif - tmp5000<0:
    break
  if dif - tmp5000 % 9000 ==0:
    x=(dif-tmp5000)//9000
    if x>=0 and x+y<=n:
      print(x,y,n-x-y)
  print(-1,-1,-1)

#O(n)
N,Y=map(int,input().split())
Y//=1000
for z in range(N+1):
  x=round(-N+0.8*z+0.2*Y,5)
  y=round(-0.2*Y-1.8*z+2*N,5)
  if x.is_integer() and y.is_integer() and x+y+z==N:
    if x>=0 and y>=0:
      if 10*x+5*y+z==Y:
        print(int(x),int(y),int(z))
        exit()
print(-1,-1,-1)

