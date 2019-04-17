from collections import deque
import random
# f="SSSSj0013ssTb0010f"
# f="j0018j0013Tfj0011j0006"
# f="TSSSSb0012fssTTj0006"

i=0
# one=[]
# two=[]
# while i < 10**5:
#   a=random.randrange(1,3)
#   if a== 1:
#     one.append(a)
#   else:
#     two.append(a)
#   i+=1
# print(len(one),len(two))
# f="c0007fSSttr"
f="Tc0008fTc0015rsr"
f=" "+f
s=0
t=0
i=1
nums=[str(i) for i in range(10)]
ls=deque([])

def get_num(i):
  i=i
  j=i+1
  tmp=""
  try:
    while f[j] in nums:
      tmp+=f[j]
      j+=1
    if len(tmp)>0:
      tmp=int(tmp)
      i=tmp
    else:
      i+=1
  except IndexError:
    i=int(tmp)
    pass
  return i

while i<len(f):
  if f[i]=="S":
    s+=1
    i+=1
  elif f[i] =="s":
    s-=1
    i+=1
  elif f[i]=="T":
    t+=1
    i+=1
  elif f[i]=="t":
    t-=1
    i+=1
  elif f[i]=="j":
    i=get_num(i)
  elif f[i]=="b":
    if s>0:
      i= get_num(i)
    else:
      i+=1
      while f[i] in nums:
        i+=1
  elif f[i]=="c":
    ls.append(get_num(i))
    i+=1
    while f[i] in nums:
      i+=1
  elif f[i]=="r":
    if ls:
      i=ls.pop()
    else:
      print('lsがない')
      break
  elif f[i]=="f":
    if ls:
      i+=1
    else:
      break
print("s:",s,"t:",t,"ls:",ls)
