a=int(input())
b=int(input())

if abs(a-b) > (10-a)+b:
  print((10-a)+b)
elif abs(a-b)> 10-b+a:
  print(10-b+a)
else:
  print(abs(a-b))
