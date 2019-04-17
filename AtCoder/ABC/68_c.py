# #8:39-
n,m=map(int,input().split())
edges=[[]for i in range(n)]


for i in range(m):
  a,b=map(int,input().split())
  edges[a-1].append(b-1)
  edges[b-1].append(a-1)

for v in edges[-1]:
  if 0 in edges[v]:
    print('POSSIBLE')
    exit()
print('IMPOSSIBLE')

# # if visited[-1]==True and cnt==2:
# #   print('POSSIBLE')
# # else:
# #   print('IMPOSSIBLE')



