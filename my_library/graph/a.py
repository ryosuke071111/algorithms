n=int(input())
m = [[-1 for i in range(n)] for j in range(n)]
for i in range(n): #隣接の辺のコストを入力
  nums = list(map(int, input().split()))
  for j in range(n):
    m[i][j] = nums[j]

d=[0]+[10**9]*(n-1)
visited=[0]*n

while 1:
  u=-1
  for i in range(n):
    if not visited[i] and (u<0 or d[i]<d[u]):
      u = i
  if u < 0:
    break
  visited[u]=1
  for v in range(n):
    if not visited[v] and m[u][v]!=-1:
      if m[u][v]<d[v]:
        d[v]=m[u][v]

print(sum(d))
