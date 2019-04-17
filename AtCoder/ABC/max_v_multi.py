A = int(input())
tmp = 0

for i in range(A):
  j = A - i
  if i * j > tmp:
    tmp = i*j

print(tmp)
