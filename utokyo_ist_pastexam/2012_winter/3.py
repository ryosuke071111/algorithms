# 9:40-
f=open("prog1.txt")
f=f.read()[:-1].split('\n')
f=list(map(lambda x:x.split(),f))

alphabet = [chr(ord('a') + i) for i in range(26)]
vals={}

def op(i,j,k):
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

for i,j,k in f:
  try:
    op(i,j,k)
  except:
    print("エラー出てる",i,j,k)

