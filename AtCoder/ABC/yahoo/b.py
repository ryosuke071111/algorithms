edges=[[]for i in range(4)]
for i in range(3):
  a,b=map(int,input().split())
  edges[a-1].append(b-1)
  edges[b-1].append(a-1)

for i in range(4):
  if len(edges[i])>=3:
    print('NO')
    exit()
print('YES')
