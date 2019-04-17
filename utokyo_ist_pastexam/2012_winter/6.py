# 9:40-
from collections import deque
f=open("prog5.txt")
f=f.read()[:-1].split('\n')
f=list(map(lambda x:x.split(),f))
alphabet = [chr(ord('a') + i) for i in range(26)]

def recursive(pc,x,stack):
  pc=pc
  stack=stack
  vals={}
  vals["in"]=x
  while pc < len(f):
    #現在のpc、辞書（必要なら値も）、stack
    try:
      i=f[pc][0]
      j=f[pc][1]
      k=f[pc][2]
    except IndexError:
      pass
    if i == "ADD":
      if j not in alphabet:
        j=int(j)
      elif j in vals:
        j=int(vals[j])
      vals[k]+=j
    elif i == "PRN":
      if j in vals:
        j=vals[j]
      if k in vals:
        k=vals[k]
      print(j,k)
    elif i== "SET":
      if k == "in":
        k=vals["in"]
      vals[j]=int(k)
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
        continue
    if i == "CAL":
      stack.append(pc+1)
      if k in vals:
        k=vals[k]
      result=recursive(pc+int(j),k,stack)
      vals["out"]=result
    if i == "RET":
      if stack:
        pc=stack.pop()
        return vals["y"]
      else:
        pc+=1
        continue
    pc+=1
recursive(0,0,stack=[])



