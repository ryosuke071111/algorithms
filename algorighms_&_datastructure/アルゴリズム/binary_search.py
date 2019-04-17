import math as m
TARGET = 7
from bisect import bisect_left

NUM = 999999999990000000 # 1億個
lists = [i for i in range(8)]

low = lists[0]
high = lists[-1]
moji = "ありましたよおおおおおおこの数値：{0}"
count = "{}回目に見つかりました。"
i = 0

print(bisect_left(lists,7))
# while (low != high):
#   center = (low + high) // 2
#   print("center",center)
#   i += 1
#   if (list[center] < TARGET):
#     low = center + 1
#   elif (list[center] == TARGET):
#     print("-"*10)
#     print(moji.format(TARGET))
#     print(count.format(i))
#     break
#   # if (TARGET < list[center]):
#   elif(TARGET < list[center]):
#     high = center - 1
