#状態の列挙ではなく、イテレーションごとに全体としてどこまでvisitできているかを調査
def DFS(count,num):
  visited=[False]*10
  count=count #訪問できる頂点の数
  num=num     #開始点
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
          if e == 0:        #0から始まる探索のどこかの辺の先に0があった場合（閉路有無探索）
            cycle_flag=True
  dfs(num)
  return count,cycle_flag


#使用例
#グラフに辺と頂点を追加していく中で、0から始まる探索がどこまでいけるかをDFSで調べている

graph=[[]for i in range(10)]
time_r=0 #0から始まる訪問がグラフをたどってどこまでいけるか
time=0
time_cycle=0 #いつ閉路ができるか
for i in info:
  time+=1
  graph[int(i[0])].append(int(i[3]))
  count,cycle_flag=DFS(0,0) #ここで使っている
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
