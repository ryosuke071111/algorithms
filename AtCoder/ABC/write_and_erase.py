#TLEした
# from collections import deque

# n = int(input())
# nums = deque([])

# for i in range(n):
#   a = int(input())
#   try:
#     nums.remove(a)
#   except ValueError:
#     nums.append(a)

# print(len(nums))

#早い
import collections
ans = 0
n = int(input())
nums = [int(input()) for i in range(n)]
con = collections.Counter(nums)

for i in con.values():
  if i % 2 != 0:
    ans += 1
print(ans)
