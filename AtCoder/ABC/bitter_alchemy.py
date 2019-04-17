n,x = map(int,input().split())
M = sorted([int(input()) for i in range(n)])
count = n
x = x-(sum(M))
while x >= 0:
  x = x-M[0]
  count += 1
  if x < 0:
    print(count-1)
    exit()
print(count)
