n = int(input())

if n % 2 == 0:
  print(n*(1+n)//2)
else:
  print((n*(1+(n-1))//2)+(n//2+1))
