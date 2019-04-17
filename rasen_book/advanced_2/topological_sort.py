　# #深さ優先探索
# v, e = map(int, input().split())
# L = [] #順番を格納するリスト
# visited = [0 for i in range(v)] #訪問を示すリスト
# edges = [[] for i in range(v)]  #隣接リスト
# flag = 0

# def visit(x):
#   if visited[x] == 1:   #すでに訪問済みなら
#     flag = 1            #フラグを1にする
#   elif not visited[x]:  #まだ訪問していなかったら
#     visited[x] =1       #訪問済みにする　
#     for e in edges[x]:  #対象のお隣さんも訪問する
#       visit(e)
#     visited[x] = 2      #お隣さんへの訪問が終わったら2にする
#     L.insert(0, x)      #順番リストの先頭に訪問の終わった値を入れる

# for i in range(e):
#   s, t = map(int, input().split())
#   edges[s].append(t)

# for i in range(v):
#   if not visited[i]:
#     visit(i)

# for i in L:
#   print(i)


#幅優先探索
import sys
import os
import pprint
from collections import deque

v, e = map(int, input().split())
edges = [[] for i in range(v)] #お隣さんリスト
indig = [0]* v                 #入次の数

for i in range(e): #           #ペアの数だけ辺の本数がある
  s, t = map(int, input().split())
  edges[s].append(t)           #sのお隣さんリストにtを入れる
  indig[t] += 1                #入次数を+1
# print('edges is' , edges)
# print('indig is ', indig)

Q = deque()                    #仕事の終わったノードをキューに入れる
L = []                         #作業順番格納リスト

def bfs(index):
  Q.append(index)
  # print('Q is ', Q)

  while len(Q) != 0:
    u = Q.popleft()
    # print(u)
    L.append(u)
    # print('L is ', L)

    for c in edges[u]:
      # print('c is', c, "edges[u] is", edges[u])
      # print('indig[c] is', indig[c])
      indig[c] -= 1
      # print('indig is ', indig)
      if indig[c] == 0:
        Q.append(c)
        # print('Q is ', Q)

indig_copy = indig[:]
for i in range(v):
  # print('i is', i)
  if indig_copy[i] == 0:
    bfs(i)

for v in L:
  print(v)



#一言：着手すべき仕事の順序を列挙
#処理の流れ：①キューに入れて入次数を減らす②0になったら次のノードをキューへ
#計算量：O(|V| + |E|)
