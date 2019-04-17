n,m=map(int,input().split())
roads=[[] for i in range(n+1)]
for i in range(m):
  a,b=map(int,input().split())
  roads[a].append(1)
  roads[b].append(1)

for i in range(1,n+1):
  print(sum(roads[i]))
