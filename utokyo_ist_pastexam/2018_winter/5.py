from collections import deque
import random
dic={"S":0,"s":0,"T":0,"t":0,"j":0,"b":0,"c":0,"r":0,"f":0}
# f=open("prog5.txt")
# f=f.read().strip('\n')
f="TSSSSb0012fssTTj0006"
f=" "+f
nums=[str(i) for i in range(10)]
ls=deque([])

def get_num(i):
  i=i
  j=i+1
  tmp=""
  while j<len(f) and f[j] in nums:
    tmp+=f[j]
    j+=1
  if len(tmp)>0:
    tmp=int(tmp)
    i=tmp
  else:
    i+=1
  return i

k=0
while k < 100:
  i=1
  s=0
  t=0
  while i<len(f):
    if f[i]=="S":
      s+=1
      i+=1
      dic["S"]+=1
    elif f[i] =="s":
      s-=1
      i+=1
      dic["s"]+=1
    elif f[i]=="T":
      t+=1
      i+=1
      dic["T"]+=1
    elif f[i]=="t":
      t-=1
      i+=1
      dic["t"]+=1
    elif f[i]=="j":
      i=get_num(i)
      dic["j"]+=1
    elif f[i]=="b":
      a=random.randrange(1,3)
      if a==1:
        i= get_num(i)
      else:
        i+=1
        while f[i] in nums:
          i+=1
      dic["b"]+=1
    elif f[i]=="c":
      ls.append(get_num(i))
      i+=1
      while f[i] in nums:
        i+=1
      dic["c"]+=1
    elif f[i]=="r":
      if ls:
        i=ls.pop()
      else:
        print('lsがない')
        print("s:",s,"t:",t,"ls:",ls)
        print(dic)
        exit()
        break
      dic["r"]+=1
    elif f[i]=="f":
      dic["f"]+=1
      if ls:
        i+=1
      else:
        break
  k+=1
print("s:",s,"t:",t,"ls:",ls)
print(dic)
