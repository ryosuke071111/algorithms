import math

a,b = input().split()
num = int(a+b)
if math.sqrt(num) % 1 == 0:
  print('Yes')
else:
  print('No')
