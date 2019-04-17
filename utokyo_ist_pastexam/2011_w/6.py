from uti import *
f1=open('s3.txt')
f1=f1.read().strip('\n')
ls=[]
while len(f1)>0:
  ls.append(f1[:1000])
  f1=f1[1000:]

# #圧縮
strings=""
dics=[]
for i in ls:
  string,dic=compression(i)
  strings+=string
  # dics.append(dic)
print(strings)
#展開
print()
ans=decompression(string)
print(ans)
