import statistics
import numpy as np

def getNearestValue(list, num):
    idx = np.abs(np.asarray(list) - num).argmin()
    return list[idx]

n = int(input())
A = list(map(int,input().split()))
mean = statistics.mean(A)
print(A.index(getNearestValue(A,mean)))
