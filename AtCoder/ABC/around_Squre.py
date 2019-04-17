# import math
n = int(input())

for i in range(n,-1,-1):
  if math.sqrt(i) % 1 ==0:
    print(i)
    exit()

#別解（floorをすることで自動でその近場の平方根にしてくれるのでそれを二乗する）
import math
print(int(math.sqrt(int(input())))**2)
