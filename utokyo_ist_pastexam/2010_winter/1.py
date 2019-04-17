from bisect import bisect_left
f=open('graph.txt')
info=f.read().split('\n')
info.pop()

graph=[[]for i in range(10)]
for i in info:
  graph[int(i[0])].append(int(i[3]))

#---------------------1-1--------------
count=0
for i in graph:
  if i:
    count+=1
print("グラフの頂点数は",count)
print()

#----------------------1-2--------------
#出次
length=0
v=0
for i in range(len(graph)):
  if len(graph[i])>length:
    length=len(graph[i])
    v=i
print("出次数最大の頂点番号",v)
print("出次数最大の数",length)
print()

#入次
from collections import Counter
counter={}
for i in graph:
  for j in i:
    if j not in counter:
      counter[j]=1
    else:
      counter[j]+=1
counter=Counter(counter)

max_indeg_v=counter.most_common()[0][0]
max_indeg_num=counter.most_common()[0][1]
print("入次数最大の頂点番号",max_indeg_num)
print("入次数最大の数",max_indeg_num)
print()

#頂点の数が5を超えるタイミング
vs=set([])
for i in range(len(info)):
  vs.add(info[i][0])
  vs.add(info[i][3])
  if len(vs)>5:
    print("頂点の数が5を超えた時間は",i)
    break

#v0から辿れる数が5以上になるタイミング
def DFS(count,num):
  visited=[False]*10
  count=count
  num=num
  cycle_flag=False
  def dfs(num):
    nonlocal count
    nonlocal visited
    nonlocal cycle_flag
    if visited[num]==False:
      visited[num]=True
      count+=1
      if graph[num]:
        for e in graph[num]:
          dfs(e)
          if e == 0:
            cycle_flag=True
  dfs(num)
  return count,cycle_flag


graph=[[]for i in range(10)]
time_r=0
time=0
time_cycle=0
for i in info:
  time+=1
  graph[int(i[0])].append(int(i[3]))
  count,cycle_flag=DFS(0,0)
  if count >= 5:
    if time_r==0:
      time_r=time
    time_r=min(time_r,time)
  if cycle_flag==True:
    if time_cycle==0:
      time_cycle=time
    time_cycle=min(time_cycle,time)

print("R(V)>= 5となった時間は",time_r)
print("0がサイクルの一部となった時間は",time_cycle)



#クロージャを使う場合はnonlocal変数を定義することでクロージャの外の変数へ影響を及ぼせる
#これを使うことによってforでグラフを作成しているけどそれが構築されるごとに逐次探索できるかm
