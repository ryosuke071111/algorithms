w =input()

for i in w:
  count = 0
  for j in w:
    if i == j:
      count += 1
  if count % 2 != 0:
    print('No')
    exit()
print('Yes')

#別解
w =input()
for i in w:
  if w.count(i) % 2 != 0:
    print('No')
    exit()
print('Yes')
