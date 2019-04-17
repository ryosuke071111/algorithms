n,k = map(int,input().split())

if k%2 ==1:
  print(int(n//k)**3)
else:
  print(int((n//k)**3 + ((n+(k/2))//k)**3))
