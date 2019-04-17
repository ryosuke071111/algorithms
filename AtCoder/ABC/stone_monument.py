a,b, = map(int,input().split())
nums=[1]
for i in range(1, 999):
  nums.append(nums[i-1]+i+1)

print(nums[b-a-1]-b)

#別解
a,b, = map(int,input().split())
sum = 0
for i in range(1,b-a):
  sum+=i

print(sum-a)
