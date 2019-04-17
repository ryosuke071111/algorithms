s=input()
string=""

i=0
if len(s)==1:
  print(s+"1")
  exit()
while not i == len(s):
  count=1
  while i+1 < len(s) and s[i]==s[i+1]:
    count+=1
    i+=1
  string += s[i]+str(count)
  i+=1

print(string)

#いけてる答え
from itertools import groupby
for a, l in groupby(input()):
    l = len(list(l))
    s += '{}{}'.format(a, l)
    print(a,l)
print(s)
