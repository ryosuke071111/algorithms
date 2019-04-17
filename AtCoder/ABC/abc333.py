a,b = map(int,input().split())

for i in range(1,4):
  if a*b*i % 2 == 1:
    print('Yes')
    exit()
print('No')
