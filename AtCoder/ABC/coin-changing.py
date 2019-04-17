# n = int(input())
# change = 1000-n
# count = 0

# while change > 0:
#   while change >= 500:
#     change -= 500
#     count += 1
#   while change >= 100:
#     change -= 100
#     count += 1

#   while change >= 50:
#     change -= 50
#     count += 1

#   while change >= 10:
#     change -= 10
#     count += 1

#   while change >= 5:
#     change -= 5
#     count += 1

#   while change >= 1:
#     change -= 1
#     count += 1
# print(count)

#別解
n = int(input())
change = 1000-n
count = 0
lis = [500,100,50,10,5,1]

for i in range(6):
  while change >= lis[i]:
    change -= lis[i]
    count += 1
print(count)
