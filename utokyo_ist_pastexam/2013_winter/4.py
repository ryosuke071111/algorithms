import itertools
strings=input()
ops=["+","&","!","(",")"]

#オペランドを登録
operand=set([])
for i in strings:
  if i not in ops:
    operand.add(i)
operand=sorted(operand)

ans=[]
s={}

#かっこの文字列を取り出す
def formulation(strings):
  ls=[]
  i=0
  while  i < len(strings):
    if strings[i]=='(':
      tmp=i
      while strings[tmp]!=')':
        tmp+=1
      ls.append(strings[i:tmp+1])
      i+=tmp
    else:
      ls.append(strings[i])
      i+=1
  return ls

from collections import deque
#オペランドにパターンを入れていく
for i in itertools.product((0,1),repeat=len(operand)):
  tmp=strings
  for j in range(len(i)):
    s[operand[j]]=i[j]
  for j in range(len(operand)):
    tmp=tmp.replace("!"+operand[j],str(abs(s[operand[j]]-1)))
    tmp=tmp.replace(operand[j],str(s[operand[j]]))

  #かっこを先に取り出す
  ls=deque(formulation(tmp))
  j=0
  while j < len(ls):
    if ls[j]=="!":
      ls[j+1]= abs(eval(ls[j+1])-1)
      j+=2
    elif ls[j].startswith('('):
      ls[j]=eval(ls[j])
      j+=1
    else:
      j+=1
      pass
  ls=[i for i in ls if i!="!"]

  tmp=""
  for j in ls:
    if isinstance(j,int) and j>1:
      tmp+=str(1)
    else:
      tmp+=str(j)
  if eval(tmp)==1:
    ans.append(str(s))
    continue


ans=list(set(ans))
if len(ans)==0:
  print('none')
  exit()
for i in ans:
  print(i+"  =1")
