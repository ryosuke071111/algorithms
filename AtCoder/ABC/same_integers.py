nums = list(map(int,input().split()))
nums.sort()
diff = (nums[-1]-nums[1]) + (nums[-1]-nums[0])
a,b = divmod(diff,2)
print(a+b*2)

#別解
nums = list(map(int,input().split()))
nums.sort()
count = 0
if nums[0]!=nums[2]:
  if nums[0]%2 == nums[1]%2:
    count += (nums[2]-nums[0])//2
    count += (nums[2]-nums[1])//2
    count += (nums[2]-nums[0])%2
  else:
    count += (nums[2]-nums[0])//2
    count += (nums[2]-nums[1])//2
    count += 2
print(count)
