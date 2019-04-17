s = input()
t = input()

for i in range(len(s)):
  s = s[-1]+s[0:len(s)-1]
  if s == t:
    print('Yes')
    exit()

print('No')
