from collections import Counter
w = Counter(input()).most_common()
for _, i in w:
  if i % 2 !=0:
    print('No')
    exit()
print("Yes")

