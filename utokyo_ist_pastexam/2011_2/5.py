f=open('c2.txt')
f=f.read().strip('\n')
nums=[str(i) for i in range(10)]
def num_check(string):
  for i in nums:
    if string.find(i)!=-1:
      return True
  return False

def decompression(f):
  i=0
  while i < len(f):
    if f[i]in nums:
      index=int(f[i:i+3])
      if num_check(f[index:index+6])==False:
        f=f[:i]+f[index:index+6]+f[i+3:]
      else:
        tmp=f[index:i]
        tmp1= tmp
        while len(tmp)<6:
          tmp+=tmp1[:6-len(tmp)+1]
        f=f[:i]+tmp+f[i+3:]
      i+=6
    else:
      i+=1
  return f
print(decompression(f))


