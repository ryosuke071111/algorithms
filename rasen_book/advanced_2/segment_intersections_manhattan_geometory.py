import sys
file_input = sys.stdin
n = file_input.readline()

EP = []   #yの端点を入れるリスト
l = -1000000001
u = 1000000001
vs_x = set()
h_num = 0

for line in file_input:
  x1, y1, x2, y2 = map(int, line.split()) #それぞれの座標を受け取る
  if x1 == x2:                            #x同士の座標が同じ値ん場合には
    if y1 < y2:                           #yのサイズを比較して
      EP.append((y1, l, x1))              #小さい方はlowとセットにEPへ
      EP.append((y2, u, x1))              #大きい方はupとセットにEPへ
    else:
      EP.append((y1, u, x1))
      EP.append((y2, l, x1))
    vs_x.add(x1)                          #x1を頂点のxリストに代入
  else:                                   #x同士の値が違う場合には
    if x1 < x2:                           #
      EP.append((y1, x1, x2))             #大きい方をリスト内容その右側へ
    else:
      EP.append((y1, x2, x1))
    h_num += 1

class BinaryIndexedTree:
  def __init__(self, n):
    self.data = [0] *(n+1)               #インデックスツリーのデータの値初期化
    self.num = n                         #インデックスツリー内のノードの数

  def switch(self, i, d):
    while  i <= self.num:               #ノードの数より自分の数が小さければ
      self.data[i] += d                 #比較元のデータが比較対象より小さければ
      i += i & -i                       #iに値を加える

  def sum(self, i):
    s = 0
    while  i:
      s += self.data[i]
      i -= i & -i
    return s

  def seg_sum(self, a, b):
    return self.sum(b) - self.sum(a- 1)

import bisect

EP.sort()
BIT = BinaryIndexedTree(len(vs_x))
vs_x = [l] + sorted(vs_x)
d_vs_x = {e:i for i, e in enumerate(vs_x)}

cnt = 0

for p in EP:
  e = p[1]
  if e== l:
    BIT.switch(d_vs_x[p[2]], 1)
  elif e==u:
    BIT.switch(d_vs_x[p[2]], -1)
  else:
    l_x = bisect.bisect_left(vs_x, e)
    r_x = bisect.bisect(vs_x, p[2]) -1
    cnt += BIT.seg_sum(l_x,r_x)
    h_num -= 1
  if h_num ==0:
    break
print(cnt)


#一言：平面操作でユーグリッド空間上の線分交点を求める
#処理の流れ：入力された線分端点をyを基準に昇順にリストに入れる。→順番に取り出す。→下恥ならBSTに挿入。・上端ならBSTから削除。入れたものがx軸と交差したらそこで探索を開始する。
#計算量：O(nlogn+k)（二分木探索の計算量nlogn+交点k）
