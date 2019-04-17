from statistics import median
n = int(input())
nums = list(map(int,input().split()))
bs = nums[:]
tmp =0

for i in range(n):
  bs[i] -= i+1

med = median(bs)

for i in range(n):
  tmp += abs(nums[i]-(med+(i+1)))

print(int(tmp))
