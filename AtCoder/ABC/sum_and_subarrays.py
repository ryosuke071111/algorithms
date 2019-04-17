import itertools
import numpy as np


num=0
n,k = map(int,input().split())
A = list(map(int,input().split()))
nums=[]
z=1

for i in range(len(A)):
  while z <= len(A):
    nums.append(A[i:z])
    z+=1
  z=i+2

nums = [sum(i) for i in nums]


for i in itertools.combinations(nums,k):
  for j in range(k):
    if int(bin(i[j] & i[j]),2) >num:
      num = int(bin(i[j] & i[j]),2)
    print(i)

print(num)

# #組みあわせライブラリ
# itertools.combinations()
# itertools.permutations()
# enumerate

