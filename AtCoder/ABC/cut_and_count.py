n= int(input())
s = input()
count = 0

for i in range(1, len(s)-1):
  a = set(s[:i])
  b = set(s[i:])
  c = a & b
  count = max(count, len(c))
print(count)

