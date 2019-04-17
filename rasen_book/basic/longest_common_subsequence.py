def longest_common(x, y):
  cost = [0]
  for c in y:
    for i in range(len(cost)-1, -1, -1):
      index = x.find(c, cost[i]) + 1
      print("cは", c, "indexは",index, "iは", i, "len(cost)は", len(cost),"costの中身は", cost)
      if index:
        if i + 1 < len(cost):
          cost[i + 1] = min(cost[i+1], index)
        else:_
          cost.append(index)
  print("costの長さは", len(cost))
  return len(cost) -1

n = int(input())
for _ in range(n):
  x = input()
  y = input()
  print(longest_common(x, y))

#rangeの場合、始点、終点、ステップ数
#正し、終点に入れた数字は包含されない
#つまり、(1,10)と入れ場合には10番目はカウントされないので注意
#しかし、始点についてはその数字がカウントされる
#逆に言うと、遡る時はそれを考慮して0まで下ろして来たい場合は-1にする必要がある

import numpy as np
np.array([])
