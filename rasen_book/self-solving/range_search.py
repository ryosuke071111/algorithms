from sys import stdin
import math
from operator import itemgetter
from bisect import bisect_left, bisect_right
readline = stdin.readline

def main():
  xy = [tuple(map(int, readline().split())) + (i,) for i in range(int(readline()))]
  xy.sort()
  root = int(math.sqrt(len(xy)))

  low = [x for x, y, i in xy[::root]]
  high = [x for x, y, i in xy[root -1::root]] + [float('inf')]

  xy = [sorted(xy[i:i+root], key=itemgetter(1)) for i in range(0, len(xy),root)]
  xy = [([y for x, y, i in xyi], xyi) for xyi in xy]
  for sx, tx, sy, ty in (map(int, readline().split()) for _ in range(int(readline()))):
    ret =[]
    for i in range(bisect_left(high,sx), bisect_right(low, tx)):
      k,v = xy[i]
      for i in range(bisect_left(k, sy), bisect_right(k,ty)):
        if sx <= v[i][0]<=tx:
          ret.append(v[i][2])

    if ret:
      ret.sort()
      print('\n'.join(map(str,ret)))
    print()
main()
