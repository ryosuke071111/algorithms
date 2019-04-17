n = int(input())
nums = map(int,input().split())

count = 0
for i in nums:
  if i % 2 ==0:
    while i % 2 ==0:
      i /= 2
      count += 1

print(count)

#いかにその偶数の割り算を多く成し遂げられるか問題に帰着する
