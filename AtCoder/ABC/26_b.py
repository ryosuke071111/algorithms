import math
n=int(input())
R=[int(input()) for i in range(n)]
R.sort()
print(abs(sum(list(map(lambda x:x**2,R[::2])))-sum(list(map(lambda x:x**2,R[1::2]))))* math.pi)
