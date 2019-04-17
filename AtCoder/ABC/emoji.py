from collections import Counter
n = int(input())
v = list(map(int, input().split()))
a = Counter(v[::2]).most_common()
b = Counter(v[1::2]).most_common()
if len(a) ==1:
  a.append([0,0])
if len(b) == 1:
  b.append([0,0])
if a[0][0] == b[0][0]:
  if a[1][1]>b[1][1]:
    print(n-a[1][1] - b[0][1])
  else:
    print(n-a[0][1]-b[1][1])
else:
  print(n-a[0][1]-b[0][1])
