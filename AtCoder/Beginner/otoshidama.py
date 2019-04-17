import sys
n,y = map(int,input().split())

for i in range(n+1):
  for j in range(n-i+1):
    k = n-i-j
    if y - (10000*i + 5000*j + 1000*k) ==0 :
      print(i,j,k)
      sys.exit()

print(-1, -1, -1)
