# f="SSSSj0013ssTb0010f"
f="j0018j0013Tfj0011j0006"
f=" "+f
s=0
t=0
i=1
nums=[str(i) for i in range(10)]
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
  elif f[i]=="b":
    if s>0:
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
    else:
      i+=1
      while f[i] in nums:
        i+=1
  elif f[i]=="f":
    break
print("s:",s,"t:",t)
