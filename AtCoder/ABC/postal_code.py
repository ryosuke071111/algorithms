a,b = map(int,input().split())
s = input()

s = s.split('-')

if len(s[0]) == a and len(s[1]) == b:
  print('Yes')
else:
  print('No')

