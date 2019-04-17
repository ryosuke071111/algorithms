
class UnionFind:
  def __init__(self, num):
    self.rank = [0]*num
    self.par = [i for i in range(num)] #基準(par = parentのpar)
    self.n   = num

  def find(self, x):
    if self.par[x] == x:
      return x
    else:
      self.par[x] = self.find(self.par[x]) #自分じゃなきゃ親を探す
      return self.par[x]

  def merge(self, x, y):
    x = self.find(x)
    y = self.find(y)
    if x == y:
      return
    if self.rank[x] > self.rank[y]: #ランクの高い方に基準を合わせる
      self.par[y] = x
    else:
      self.par[x] = y
      if self.rank[x] == self.rank[y]:
        self.rank[y] += 1

  def same(self, x, y):
    return self.find(x) == self.find(y)

N, Q = map(int, input().split())
uf = UnionFind(N)

for i in range(Q):
  C, X, Y = map(int, input().split())

  if C == 0:
    uf.merge(X, Y)

  elif C == 1:
    print(1 if uf.same(X, Y) else 0)
  else:
    print(uf.find(X))

#計算量O(logn)経路圧縮とrankを用いた計算量
#-経路圧縮：葉から根へたどる際に通過したノードの親ポインタを根にする
#-rank：木を合併する際に、ノードの高さの高い方に低い方が結合しにいく

#処理の流れ
#same:  入力受け取り→親が同じ？→true/false
#unite: 高さがどっちが高いか？→高い方へ結合
