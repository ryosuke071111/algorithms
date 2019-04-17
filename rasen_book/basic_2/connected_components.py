v, e = map(int, input().split())   #ユーザ数、関係性の数
edge = [[] for _ in range(v)]      #お隣さんリスト


#連結成分作成部分のコード（各頂点を一度ずつ訪問して隣接リスト内の辺を訪問）
for _ in range(e):                 #関係性の数だけ
  s, t = map(int, input().split()) #始点と終点を入れる
  edge[s].append(t)                #sのお隣さんリストにtを
  edge[t].append(s)                #tのお隣さんリストにsを

group = [-1]*v                     #グループというリストを作る（こいつの値であとで友達か照合）
cnt = 0                            #グループ番号


#隣接リストに入っている同じノードをスタックに入れてグループ化する
for i in range(v):
  if group[i] == -1:
    group[i] = cnt                 #カウントの値を入れる
    stack = [i]                    #ノード番号を入れる
    while stack:
      v = stack.pop()              #ノードを代入　ー①
      for c in edge[v]:            #①のノードのお隣さんリストを辿っていく（幅優先探索）
        if group[c] == -1:         #お隣さんのグループが初期化状態なら
          group[c] = cnt          #グループリストにカウントを入れる
          stack.append(c)          #スタックにお隣さんを入れる
    cnt += 1                       #お隣さんの訪問が終わったらグループ番号を変える

#クエリのコード
for _ in range(int(input())):
  s, t = map(int, input().split())
  print('yes' if group[s] == group[t] else 'no')
