s=0
t=0
f="SSSSj0013ssTb0010f"
f=" "+f
nums=[str(i) for i in range(10)]
def get_num(i):
  tmp=""
  i+=1
  while i<len(f) and f[i] in nums:
    tmp+=f[i]
    i+=1
  i=int(tmp)
  return i
i=1
while i < len(f):
  if f[i]== "S":
    s+=1
    i+=1
  if f[i]=="s":
    s-=1
    i+=1
  if f[i]=="T":
    t+=1
    i+=1
  if f[i]== "t":
    t-=1
    i+=1
  if f[i]=="f":
    print('sの値:',s,"tの値:",t)
    exit()
  if f[i]=="j":
    i=get_num(i)
  if f[i]=="b":
    if s>0:
      i=get_num(i)
    else:
      i+=1
      while i < len(f) and f[i] in nums:
        i+=1



