import time
start = time.time()

n,w = map(int,input().split())
items = [[0,0] for i in range(n+1)]
dp =[[0 for i in range(w+1)] for i in range(n+1)]

for i in range(1, n+1):
  items[i][0],items[i][1] = map(int,input().split())

for i in range(1,n+1):
  for j in range(1,w+1):
    if items[i][0] <= j:
      dp[i][j] = max(dp[i-1][j],dp[i-1][j-items[i][0]]+items[i][1])
    else:
      dp[i][j] = dp[i-1][j]

print(dp[n][w])

elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

#①一つ上の行の方の数字を持ってくる
#（常に上の人を持って来ればその時の最適地になっている。今の段階のアイテムは入れられないけどその前の段階のアイテムはそこにその重さで入れることができるから。）

#次のアイテムにキャパができた時は一つ上の行のアイテムの重さ分を引いた値を足した時とそのアイテムを直接入れた時のどちらが大きいかを比較する

#実質j-items[1]が重さチェックになっている（アイテム入る！でも前にアイテム入っているし、、の防止）


#早いバージョン
import time
start = time.time()

from collections import defaultdict
n, W = list(map(int, input().split()))
wv = [list(map(int, input().split())) for _ in range(n)]

dp = defaultdict(int)
dp[0] = 0
for w, v in wv:
    dp_cur = list(dp.items())
    for w_cur, v_cur in dp_cur:
        if w_cur+w <= W:
            dp[w_cur+w] = max(dp[w_cur+w], v_cur+v)
print(max(dp.values()))

elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
