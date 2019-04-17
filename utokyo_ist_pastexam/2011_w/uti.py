def judge(string):
  flag=True
  if string.__contains__('0'):
    flag=False
  if string.__contains__('1'):
    flag=False
  if string.__contains__('2'):
    flag=False
  if string.__contains__('3'):
    flag=False
  if string.__contains__('4'):
    flag=False
  if string.__contains__('5'):
    flag=False
  if string.__contains__('6'):
    flag=False
  if string.__contains__('7'):
    flag=False
  if string.__contains__('8'):
    flag=False
  if string.__contains__('9'):
    flag=False
  return flag

def compression(string):
  dic={}
  i=0
  while i<len(string):
    if judge(string[i:i+6])==True and len(string[i:i+6])==6:
      if string[i:i+6] not in dic :
        dic[string[i:i+6]]="0"*(3-len(str(i)))+str(i)
        i+=1
      elif string[i:i+6] in dic:
        string=string[:i]+str(dic[string[i:i+6]])+string[i+6:]
        i+=1
    else:
      i+=1
  return string,dic

def decompression(string):
  i=0
  while i<len(string):
    if judge(string[i])==False:
      index=int(string[i:i+3])
      # print('index:',index)
      if index+5>=i:
        zenhan=string[:i]
        kouhan=string[i+3:]
        j=i
        tmp=j
        karimoji=str(string[index:j])
        j+=len(karimoji)
        string=zenhan+karimoji+kouhan
        while len(karimoji)<6:
          karimoji+=string[tmp:j]
          string=zenhan+karimoji+kouhan
          diff=j-tmp
          tmp+=diff
          j+=diff
        string=zenhan+karimoji+kouhan
      else:
        string=string[:i]+string[index:index+6]+string[i+3:]
    i+=1
  return string
