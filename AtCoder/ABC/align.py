from collections import deque
n = int(input())
nums =[]

for i in range(n):
  nums.append(int(input()))

nums.sort()
nums = deque(nums)
a = [nums.pop()]
a = deque(a)

while not len(nums) == 0:
  try:
    a.appendleft(nums.popleft())
    a.append(nums.popleft())
    a.appendleft(nums.pop())
    a.append(nums.pop())
  except IndexError:
    pass

tmp_1 = abs(a[-1] - a[-2])
tmp_2 = abs(a[-1] - a[0])

if tmp_1 < tmp_2:
  a.appendleft(a.pop())

sub = 0
for i in range(1, len(a)):
  sub += abs(a[i-1]-a[i])
print(sub)
