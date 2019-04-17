import re
s = input()
s= re.sub("B+","B",s)
s= re.sub("W+","W",s)
print(len(s)-1)
