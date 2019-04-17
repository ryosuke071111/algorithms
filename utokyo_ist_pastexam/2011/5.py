s1=open('s1.txt')
s1=s1.read().strip('\n')
# s1="vwabcdefxy002st"
s1="ab000ab"
i=0
dic={}
dic2={}
s2=s1
alphabet = [chr(ord('a') + i) for i in range(26)]

while i+5<=len(s1):
  try:
    if len(s1[i:i+6])==6 and s1[i:i+6] not in dic:
      dic[s1[i:i+6]]=str(i).zfill(3)
      dic2[str(i).zfill(3)]=s1[i:i+6]

      while dic2[str(i).zfill(3)] in s1:
        tmp=""
        k=0
        while True:
          if dic2[str(i).zfill(3)][k] in alphabet:
            tmp+=dic2[str(i).zfill(3)][k]
            k+=1
          else:
            break
        s1=s1[:i+1]+tmp+s1[i+1]
        dic2[str(i).zfill(3)]=s1[i:i+6]
        print(dic,dic2,s1)
    i+=1
  except KeyError:
    pass
  except IndexError:
    break
print(s1)


