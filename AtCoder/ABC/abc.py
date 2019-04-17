s = input()
abc=['a','b','c']


for i in range(len(s)):
  if s[i] in abc:
    abc.remove(s[i])

if len(abc) == 0:
  print('Yes')
else:
  print('No')

#別解
s = input()

if ''.join(sorted(list(s))) == 'abc':
  print('Yes')
else:
  print('No')

