f=open('s1.txt')
f=f.read().strip('\n')
dic={}
i=0

while i <len(f)-5:
  if f[i:i+6] not in dic:
    dic[f[i:i+6]]="0"*(3-len(str(i)))+str(i)
  else:
    pass
  i+=1
print(len(dic))

