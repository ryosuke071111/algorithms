nums = list(map(int,input().split()))
k=int(input())
a = max(nums)*(2**k)
print(sum(nums) + max(nums)*(2**k)-max(nums))

