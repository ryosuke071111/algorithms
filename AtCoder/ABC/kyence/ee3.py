# a,b,x=map(int,input().split())
# count=0
# if x==1:
#   print(b-a+1)
#   exit()
# else:
#   if a%x==0:
#     print(b//x-a//x+1)
#   else:
#     print(b//x-a//x)
x,y,z=map(int,input().split())
x=x-(y+z*2)
print(x//(y+z)+1)
