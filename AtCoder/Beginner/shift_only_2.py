import sys
n = int(input())
nums = list(map(int,input().split()))
count = 0
b = 0

while b <1:
  for i in range(n):
    if nums[i] % 2 ==0:
      nums[i] //= 2
    else:
      print(count)
      sys.exit()
  count += 1

print(count)

