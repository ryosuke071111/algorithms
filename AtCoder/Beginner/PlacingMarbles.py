one_box = []
zero_box = []

s1, s2,s3 = map(int, input())

for a in s1, s2,s3:
  if a == 1:
    one_box.append(a)

print(len(one_box))

#または
print(input().count('1'))
