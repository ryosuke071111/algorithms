from statistics import mean
from math import ceil
n=int(input())
A=list(map(int,input().split()))
A=[i for i in A if i>0]
print(ceil(mean(A)))
