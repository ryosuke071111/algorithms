import re
s=input()
t=input()
check=["a","t","c","o","d","e","r"]

for i in range(len(s)):
  if s[i]!=t[i]:
    if t[i] != "@" and s[i] != "@":
      print("You will lose")
      exit()
    elif t[i] != "@" and t[i] not in check:
      print("You will lose")
      exit()
    elif s[i] != "@" and s[i] not in check:
      print("You will lose")
      exit()
print('You can win')



