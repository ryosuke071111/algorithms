f1=open('s1.txt')
f1=f1.read().strip('\n')
dic={}
for i in range(len(f1)-5):
  if f1[i:i+6] not in dic:
    dic[f1[i:i+6]]="0"*(3-len(str(i)))+str(i)
print(len(dic))
