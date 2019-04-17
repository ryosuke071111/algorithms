import fractions

n,x = map(int,input().split())
nums = list(map(int,input().split()))

min_n = abs(x-nums[0])
for i in range(1,n):
  min_n = fractions.gcd(min_n,abs(x-nums[i]))

print(min_n)
