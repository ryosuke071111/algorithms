#18:20-
s=input()
strings=["dreamer","dream", "eraser","erase"]
i=-1
while len(s)!=0:
  if s[i-1:] in strings:
    s=s[:i-1]
    i=-1
  i-=1
  if i==-len(s):
    print('NO')
    exit()
if len(s)==0:
  print('YES')

