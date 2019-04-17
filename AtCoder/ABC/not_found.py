s=list(input())
alphabet = [chr(ord('a') + i) for i in range(26)]

s.sort()

for i in alphabet:
  if i not in s:
    print(i)
    exit()
print('None')
