n = int(input())
a = 0
if n <= 0 or 101 <= n:
  exit()
list1 = list(map(int, input().split()))

for i in range(len(list1)):
  minj = i
  for j in range(i, len(list1)):
    if list1[j] < list1[minj]:
      minj = j
  if i != minj:
    list1[minj], list1[i] = list1[i], list1[minj]
    a += 1
print(' '.join(map(str, list1)))
print(a)
