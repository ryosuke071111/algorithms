k = int(input())
even=0
odd = 0
for i in range(1,k+1):
  if i % 2 ==0:
    even += 1
  else:
    odd += 1

print(even*odd)

#別解(二種類しか数字がないので一つとって残りとかける。n*(n-k))
k = int(input())
s = (k+1)//2
print(s*(k-s))
