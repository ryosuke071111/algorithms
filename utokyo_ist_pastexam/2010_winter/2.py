from bisect import bisect_left
f=open('graph.txt')
info=f.read().split('\n')
info.pop()

graph=[[]for i in range(10)]
for i in info:
  if i[0]=="!":
    graph[int(i[1])].remove(int(i[4]))
  else:
    graph[int(i[0])].append(int(i[3]))



#---------------------2-1--------------
count=0
for i in graph:
  for j in i:
    if j:
      count+=1
print("グラフの辺の数は",count)
print()


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
  if i[0]=="!":
    graph[int(i[1])].remove(int(i[4]))
  else:
    graph[int(i[0])].append(int(i[3]))
  time+=1
  count,cycle_flag=DFS(0,0)
  if count >= 2:
    if time_r==0:
      time_r=time
    time_r=min(time_r,time)
  if cycle_flag==True:
    if time_cycle==0:
      time_cycle=time
    time_cycle=min(time_cycle,time)

print("R(b)の大きさは",DFS(0,0)[0])
print("R(t)>2のとなった時間",time_r)



#クロージャを使う場合はnonlocal変数を定義することでクロージャの外の変数へ影響を及ぼせる
#これを使うことによってforでグラフを作成しているけどそれが構築されるごとに逐次探索できるかm
