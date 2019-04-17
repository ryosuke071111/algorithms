import re
S=[input() for i in range(12)]
count=0
for i in S:
  if re.search('r',i):
    count+=1

print(count)
