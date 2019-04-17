n = int(input())

divisor = 0

for i in range(1,n+1):
  count = 0
  if i % 2 != 0:
    for j in range(1,i+1):
      if i % j ==0:
        count += 1
    if count == 8:
      divisor += 1

print(divisor)

