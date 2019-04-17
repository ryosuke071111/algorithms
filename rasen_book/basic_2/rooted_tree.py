NIL = -1
class Node:          #ノード作成
  def __init__(self):
    self.parent = NIL
    self.left = NIL
    self.right = NIL

def getDepth(u):     #深さを調査
  d = 0
  while T[u].parent != NIL: #親がいたら
    u = T[u].parent         #上に上る
    d += 1                  #深さカウント+1
  return d

def getChildren(u):  #子供調査
  c = T[u].left      #自分の左側の子供をcとする
  result = []        #結果リスト
  while c != NIL:    #自分の左の子供が存在する限り
    result.append(c) #結果リストに子供を貼っていく
    c = T[c].right   #その右側にノードがあればその子を貼っていく
  return result

n = int(input())
T = [0]*n
for i in range(n):
  T[i] = Node()       #ノードのリスト

for i in range(n):
  tmp = list(map(int, input().split())) #[id, 子供の数、子供のid] リスト
  id = tmp.pop(0)
  k = tmp.pop(0)
  c = tmp                              #残ったら子供のリストとなる
  if k != 0:
    for j in range(len(c)):
      T[c[j]].parent = id
      T[id].left = c[0]     #自分の左の子供にtmpの最新の子供を貼り付ける
      for j in range(len(c)-1):
        T[c[j]].right = c[j+1] #自分の右の子供にtmpの子供を貼り付ける

for i in range(n):
  d = getDepth(i)
  c = getChildren(i)
  if d == 0:
    t = 'root'
  elif c == []:
    t = 'leaf'
  else:
    t = 'internal node'
  print('node ',i,': ','parent = ',T[i].parent,', depth = ',d,', ',t,', ',c,sep = '')

