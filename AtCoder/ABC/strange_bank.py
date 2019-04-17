#メモ化再帰
n = int(input())
max_n = 10000
memo = [999999]*(max_n+1)
memo[0]=0
for i in range(1,n+1):
  memo[i] = memo[i-1]+1
  k = 6
  while i -k >= 0:
    memo[i] = min(memo[i], memo[i-k]+1)
    k *= 6
  k = 9
  while i - k >= 0:
    memo[i] = min(memo[i],memo[i-k]+ 1)
    k*=9
print(memo[n])

#DP（配る）
n = int(input())
max_n = 100000
dp = [10000 for i in range(max_n+1)]
dp[0] = 0

for i in range(n+1):
  k = 1
  while i + k <= n:
    dp[i+k] = min(dp[i+k],dp[i]+1)
    k *=6
  k = 1
  while i + k <= n:
    dp[i+k] = min(dp[i+k],dp[i]+1)
    k*=9

print(dp[n])

#DP（貰う）
import deque
n = int(input())
max_n = 100000
dp = [10000 for i in range(max_n+1)]
dp[0] = 0

for i in range(n+1):
  k = 1
  while k <= n:
    dp[i] = min(dp[i],dp[i-k]+1)
    k *=6
  k = 1
  while k <= n:
    dp[i] = min(dp[i],dp[i-k]+1)
    k*=9
print(dp[n])

#bfs
from collections import deque
n = int(input())
max_n = 100000
dp = [10000 for i in range(max_n+1)]
dp[0] = 0
que = deque()
que.append(0)

while len(que) > 0:
  v = que.popleft()
  k = 1
  while v + k <= n:
    if dp[v+k] == 10000:
      dp[v+k]=dp[v]+1
      que.append(v+k)
    k *= 6
  k = 1
  while v + k <= n:
    if dp[v+k] == 10000:
      dp[v+k]=dp[v]+1
      que.append(v+k)
    k *= 9
print(dp[n])

#Dijkstra ※わからない
import heapq

n = int(input())
max_n = 100000
dp = [10000 for i in range(max_n+1)]
dp[0] = 0
que = []
heapq.heappush(que,(0,0))

while len(que) >0:
  u,v = que.pop()[0],que.pop()[1]
  k = 1
  while v + k <=n:
    nv = v + k

#普通のdpの書き方
max_n = 100000
I = lambda:list(map(int,input().split()))

s = []
for i in range(1,7):
  s.append(9**i)
  s.append(6**i)
n, = I()
a = [0]*100009
for i in range(1,100007):
  a[i] = a[i-1]+1
  for j in s:
    if i-j >=0:
      a[i] = min(a[i-j]+1,a[i])
print(a[n])

