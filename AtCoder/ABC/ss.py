s=input()

flag = True

i=1
while flag:
  s = s[:-i]
  if len(s)%2==0:
    mid = (len(s)//2 -1)
    if s[mid+1:] == s[:mid+1]:
      print(len(s))
      exit()



