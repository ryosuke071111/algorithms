s1=open('s1.txt')
s1=s1.read().strip('\n')
i=0
dic={}
while i+5<=len(s1):
  try:
    if len(s1[i:i+6])==6 and s1[i:i+6] not in dic:
      dic[s1[i:i+6]]=str(i).zfill(3)
    elif s1[i:i+6] in dic:
      print(s1[i:i+6]+"は"+dic[s1[i:i+6]]+"にある")
    i+=1
  except KeyError:
    pass
print(dic)
