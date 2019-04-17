import itertools
strings=input()
ops=["+","&","!"]
operand=set([])
for i in strings:
  if i not in ops:
    operand.add(i)
operand=sorted(operand)

ans=[]
s={}
for i in itertools.product((0,1),repeat=len(operand)):
  tmp=strings
  for j in range(len(i)):
    s[operand[j]]=i[j]
  for j in range(len(operand)):
    tmp=tmp.replace("!"+operand[j],str(abs(s[operand[j]]-1)))
    tmp=tmp.replace(operand[j],str(s[operand[j]]))
  tmp=tmp.split('+')
  for i in tmp:
    if eval(i)==1:
      ans.append(str(s))
      continue

ans=list(set(ans))
if len(ans)==0:
  print('none')
  exit()
for i in ans:
  print(i)

