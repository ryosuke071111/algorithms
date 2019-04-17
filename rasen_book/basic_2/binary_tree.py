NIL = -1
class Node:  #ノード作成
  def __init__(self):
    self.parent = NIL
    self.left = NIL
    self.right = NIL
    self.type = NIL
    self.depth = NIL
    self.sibling = NIL
    self.degree = NIL
    self.height = NIL

def setHeight(u): #高さカウント（上にあるほど数字が高い）
  h1 = h2 = 0
  if T[u].right != NIL:
    h1 = setHeight(T[u].right) + 1
  if T[u].left != NIL:
    h2 = setHeight(T[u].left) + 1
  if h1 == h2 == NIL:
    return NIL
  else:
    return max(h1, h2)

def getDepth(u): #上に登っていく（したにあるほど数字が高い）
  d = 0
  while T[u].parent != NIL:
    u = T[u].parent
    d += 1
  return d

def getSibling(u): #兄弟を探す
  if T[u].parent == NIL:
    return NIL
  if T[T[u].parent].left != u and T[T[u].parent].left != NIL: #親の左の子が自分でなく、かつ、存在していれば、その値を返す
    return T[T[u].parent].left
  if T[T[u].parent].right != u and T[T[u].parent].right != NIL: #親の右の子が自分でなく、かつ、存在していれば、その値を返す
    return T[T[u].parent].right
  return NIL

def getDegree(u): #子供の数
  deg = 0
  if T[u].left != NIL:
    deg += 1
  if T[u].right != NIL:
    deg += 1
  return deg

n = int(input())
T = [0]*n
for i in range(n):
  T[i] = Node()

for i in range(n): #id, 左、右の値をもらう
  id, l, r = map(int,input().split())
  T[id].left = l
  T[id].right = r

for i in range(n): #親と子供を連結
  if T[i].left != NIL: #自分の左の子供が存在していたら
    T[T[i].left].parent = i #左の子供の親が私です
  if T[i].right != NIL: #自分の右の子供が存在していたら
    T[T[i].right].parent = i #右の子供の親が私です

for i in range(n):
  if T[i].parent == NIL:
    T[i].type = 'root'
  elif T[i].parent != NIL and (T[i].left != NIL or T[i].right != NIL):
    T[i].type = 'internal node'
  else:
    T[i].type = 'leaf'

for i in range(n):
  T[i].depth = getDepth(i)
  T[i].sibling = getSibling(i)
  T[i].degree = getDegree(i)
  T[i].height = setHeight(i)

for i in range(n):
  print('node ',i,': parent = ',T[i].parent,', sibling = ',T[i].sibling,', degree = ',T[i].degree,', depth = ',T[i].depth,', height = ',T[i].height,', ',T[i].type,sep = '')
















