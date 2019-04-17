n=int(input())
W=[input() for i in range(n)]
W_s=set(W)

if len(W) !=  len(W_s):
  print('No')
  exit()

for i in range (1, len(W)):
  if W[i][0] == W[i-1][-1]:
    continue
  else:
    print('No')
    exit()
print('Yes')
