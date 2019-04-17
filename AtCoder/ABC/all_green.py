# #ナイーブに解く
d,g = map(int,input().split())
ps=[]
cs=[]
counts = []
count = 0
visited = [0 for i in range(d)]
sums=0


for i in range(d):
  p,c = map(int,input().split())
  ps.append(p)
  cs.append(c)

def dfs(i,count,visited,sums):
  if visited[i] != ps[i]:
    local_visited=visited[:]
    count += 1
    sums += (i+1)*100
    local_visited[i] += 1
    if local_visited[i] == ps[i]:
      sums += cs[i]
    if sums >= g:
      counts.append(count)
      return
    for i in range(d):
      dfs(i,count,local_visited,sums)


for i in range(d):
  dfs(i,count,visited,sums)


print(min(counts))

#別解
import itertools
from collections import Counter
D, G = map(int, input().split())
P = [list(map(int, input().split())) for i in range(D)]
min_num = 10**8

judge_list = list(itertools.product([0, 1, 2], repeat=D)) #0:中途半端に解く 1:一問も解かない 2: 全部解く


for judge in judge_list:
    score = 0
    num = 0
    d = Counter() #インスタンスを生成
    d.update(judge)
    if (d[0] <= 1):
        for i in range(1, len(judge) + 1):
            if score >= G:
                break

            if judge[-i] == 1:
                pass

            if judge[-i] == 2:
                score += P[-i][0] * (D - i + 1) * 100 + P[-i][1]
                num += P[-i][0]

            if (judge[-i] == 0):
                for j in range(P[-i][0]):
                    if score >= G:
                        break
                    score += 100 * (D - i + 1)
                    num += 1

        if score >= G:
            min_num = min(num, min_num)

print(min_num)








