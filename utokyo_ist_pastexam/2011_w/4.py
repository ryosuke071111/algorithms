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

f1=open('s1.txt')
f1=f1.read().strip('\n')
dic={}
i=0
while i<len(f1):
  if judge(f1[i:i+6])==True:
    if f1[i:i+6] not in dic:
      dic[f1[i:i+6]]="0"*(3-len(str(i)))+str(i)
      i+=1
    else:
      f1=f1[:i]+str(dic[f1[i:i+6]])+f1[i+6:]
      i+=1
  else:
    i+=1
print("文字列の長さ:",len(f1),"末尾5文字:",f1[-5:])

f2=open('s2.txt')
f2=f2.read().strip('\n')
dic={}
i=0
while i<len(f2):
  if judge(f2[i:i+6])==True:
    if f2[i:i+6] not in dic:
      dic[f2[i:i+6]]="0"*(3-len(str(i)))+str(i)
      i+=1
    else:
      f2=f2[:i]+str(dic[f2[i:i+6]])+f2[i+6:]
      i+=1
  else:
    i+=1
print("文字列の長さ:",len(f2),"末尾5文字:",f2[-5:])
