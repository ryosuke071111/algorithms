# n = int(input())
# s = input()

# minc = 100000000

# for i in range(len(s)):
#   minc = min(minc,(s[0:i].count('W')+s[i:].count('E')))

# print(minc)

#↑ TLE。
#↓答え.すでに前の順番の人の記録は記憶しておいてその差分だけ更新していく。

n = int(input())
s = input()


nums = [s[1:].count('E')]

for i in range(1,n):
  tmp = nums[i-1]
  if s[i-1] == "W":
    tmp += 1
  if s[i] == "E":
    tmp -=1
  nums.append(tmp)

print(min(nums))
