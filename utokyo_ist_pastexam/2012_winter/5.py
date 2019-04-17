# 9:40-
from collections import deque
f=open("prog3.txt")
f=f.read()[:-1].split('\n')
f=list(map(lambda x:x.split(),f))
alphabet = [chr(ord('a') + i) for i in range(26)]
vals={}
stack=deque([])

def op(i,j,k):
  global pc
  global stack
  if i == "ADD":
    if j not in alphabet:
      j=int(j)
    elif j in vals:
      j=int(vals[j])
    vals[k]+=j
    return vals[k]
  elif i == "PRN":
    if j in vals:
      j=vals[j]
    if k in vals:
      k=vals[k]
    print(j,k)
  elif i== "SET":
    vals[j]=int(k)
    return vals[j]
  elif i == "CMP":
    if j in vals:
      j=vals[j]
    if k in vals:
      k=vals[k]
    if j==int(k):
      pc+=1
  elif i == "JMP":
    pc+=int(j)
    pc-=1



pc=0
while pc < len(f):
  try:
    i=f[pc][0]
    j=f[pc][1]
    k=f[pc][2]
  except IndexError:
    pass
  if i == "SUB":
    stack.append(pc+1)
    pc+=int(j)
    continue
  if i == "BAK":
    if stack:
      pc=stack.pop()
      continue
    else:
      pc+=1
  try:
    op(i,j,k)
  except:
    print("エラー出てる",i,j,k)
  pc+=1




