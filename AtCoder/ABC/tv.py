w,h=map(int,input().split())

if w%16==0 and h%9==0:
  print('16:9')
else:
  print('4:3')
