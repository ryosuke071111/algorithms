import math
n=int(input())
A=[int(input()) for i in range(5)]
print(math.ceil(n/min(A))+4)

