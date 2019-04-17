import math
n = input()
a = list(map(int,input().split()))
count = float('inf')

for i in a:
  count = min(count, len(bin(i))-bin(i).rfind('1')-1)
print(int(count))
