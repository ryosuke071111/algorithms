import math
tmp=0
x=int(input())

upper_b=int(math.sqrt(x))

for i in range(1,upper_b+1):
  for j in range(2,11):
    if i**j <=x:
      tmp=max(tmp,i**j)
print(tmp)
