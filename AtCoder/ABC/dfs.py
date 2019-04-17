n = int(input())
nums = list(map(int,input().split()))
sums = []
count = 0

def dfs(sums_l, i):
  sums.append(sums_l)
  if i < len(nums):
    dfs(sums_l+nums[i],i+1)
    dfs(sums_l ,i+1)
  return sums

dfs(0,0)
print(len(set(sums)))
