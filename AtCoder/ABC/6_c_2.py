#15:02-
#式変形で解ける
n,m=map(int,input().split())

for x in range(n+1):
  y=-m-2*x+4*n
  z=-3*n+x+m
  if x+y+z==n:
    if y>=0 and z>=0:
      if 2*x+3*y+4*z==m:
        print(x,y,z)
        exit()
print(-1,-1,-1)


for z in range(n+1):
  x=z+3*n-m
  y=m-2*n-2*z
  if x+y+z==n:
    if x>=0 and y>=0:
      if 2*x+3*y+4*z==m:
        print(x,y,z)
        exit()
print(-1,-1,-1)

#列挙で解く
n,m=map(int,input().split())
y=m%2
for x in range(n+1):
  z=n-x-y
  if z>=0 and 2*x+3*y+4*z==m:
    print(x,y,z)
    exit()
print(-1,-1,-1)



