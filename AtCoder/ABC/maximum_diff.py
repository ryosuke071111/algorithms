n = int(input())
nums = list(map(int,input().split()))

nums.sort()
max = nums[-1]
min = nums[0]
tmp = abs(max-min)
for i in range(len(nums)):
  if tmp < abs(max - nums[i]):
    tmp = abs(max - nums[i])

print(tmp)
