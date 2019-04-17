n = int(input())
count = 0

for i in range (1, 101):
  if n*i <= 100:
    count += 1

print(100-count)
