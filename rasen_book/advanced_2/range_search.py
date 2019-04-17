from sys import stdin
import math
from operator import itemgetter
from bisect import bisect_left, bisect_right
readline = stdin.readline

def main():
  xy = [tuple(map(int, readline().split())) + (i,) for i in range(int(readline()))]#最初の入力受付（x,y,i）
  xy.sort()  #昇順に並べ替え
  root = int(math.sqrt(len(xy)))
  # print('xy is', xy)

  low = [x for x, y, i in xy[::root]] #xyのx入力を0番目から2ずつとる（奇数番目）
  # print('low is ', low)
  high = [x for x, y, i in xy[root -1::root]] + [float('inf')] #xyのx入力を1番目から2ずつとる（偶数番目）
  # print('high is ', high)

  xy = [sorted(xy[i:i+root], key=itemgetter(1)) for i in range(0, len(xy), root)]
  #2つのリストごとにyの大きい順に並べている
  # print('sorted xy is ',xy)
  xy = [([y for x, y, i in xyi], xyi) for xyi in xy] #yを基準に並べた時のyを個別のリストに入れて別個でさらに通常のリストを同時に出力している
  # print('xyi is ', xy)
  for sx, tx, sy, ty in (map(int, readline().split()) for _ in range(int(readline()))):
    ret = []
    for i in range(bisect_left(high, sx), bisect_right(low, tx)):#xについてソート
      k, v = xy[i]
      # print('k,v, sx,tx is', k,v,sx,ty)
      for i in range(bisect_left(k, sy), bisect_right(k, ty)): #yについてソート
        # print('k,v, sy,ty is', k, v, sy, ty)
        if sx <= v[i][0] <=tx:
          ret.append(v[i][2])

    if ret:
      ret.sort()
      print('\n'.join(map(str,ret)))
    print()
main()



#一言：指定範囲内に入る点を列強する
#処理の流れ：指定された範囲で部分木生成（中央値で分ける）→x,y座標ごとに交互にソート→小さいものを再帰的に作っていく
#計算量：O(nlog^2n)：O(nlogn)ソートを木の高さ分logn回行うので。
