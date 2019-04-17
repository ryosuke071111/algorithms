s = input()
string=[]
for i in s:
  if i == "B" and len(string)>0:
    del string[-1]
  elif i == "1" or i == "0":
    string.append(i)
print("".join(string))
