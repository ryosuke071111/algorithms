k,s=map(int,input().split())
count=0

nums=[i for i in range(k+1)]

for i in range(len(nums)):
  for j in range(len(nums)):
    if 0 <= s-i-j <= k:
      count+=1
print(count)
