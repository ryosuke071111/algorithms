n = int(input())
nums = list(map(int ,input().split()))
Alice = []
Bob = []

while len(nums) > 0:
  Alice.append(max(nums))
  a = nums.index(max(nums))
  nums.pop(a)

  if len(nums) == 0:
    break
  Bob.append(max(nums))
  b = nums.index(max(nums))
  nums.pop(b)

Alice = sum(Alice)
Bob = sum(Bob)
print(Alice-Bob)



#別解
n = int(input())
nums = list(map(int ,input().split()))
nums.sort(reverse=True)
Alice = sum(nums[::2])
Bob = sum(nums)-Alice
print(Alice-Bob)
print(nums)
