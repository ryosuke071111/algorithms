from itertools import permutations
import time

start = time.time()


n,m,r = map(int,input().split())
R = list(map(int,input().split()))
inf = 10**9

edges=[[inf for i in range(n+1)] for i in range(n+1)]

for i in range(m):
  a,b,c = map(int,input().split())
  edges[a][b] = c
  edges[b][a] = c


for k in range(1,n+1):
  for i in range(1,n):
    for j in range(i,n+1):
      if edges[i][j] > edges[i][k] + edges[k][j]:
        edges[i][j] = edges[i][k]+edges[k][j]
        edges[j][i] = edges[i][j]


ans = inf
for i in permutations(R):
  tmp = 0
  for j in range(r-1):
    tmp += edges[i[j]][i[j+1]]
  ans = min(tmp, ans)

elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(round(elapsed_time,3)) + "[sec]")

print(ans)

#わからないところ
#①ワーシャルフロイドの正確なアルゴリズム
#②算出した経路をもとに複数の町を訪れた時の距離を算出するアルゴリズム
