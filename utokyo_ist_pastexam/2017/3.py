zero_0="****"
zero_1="|  |"
zero_2="*  *"
zero_3="|  |"
zero_4="****"

one_0="*"
one_1="|"
one_2="*"
one_3="|"
one_4="*"

two_0="****"
two_1="   |"
two_2="****"
two_3="|   "
two_4="****"

three_0="****"
three_1="   |"
three_2="****"
three_3="   |"
three_4="****"

four_0="*  *"
four_1="|  |"
four_2="****"
four_3="   |"
four_4="   *"

five_0="****"
five_1="|   "
five_2="****"
five_3="   |"
five_4="****"

six_0="****"
six_1="|   "
six_2="****"
six_3="|  |"
six_4="****"

seven_0="****"
seven_1="   |"
seven_2="   *"
seven_3="   |"
seven_4="   *"

eight_0="****"
eight_1="|  |"
eight_2="****"
eight_3="|  |"
eight_4="****"

nine_0="****"
nine_1="|  |"
nine_2="****"
nine_3="   |"
nine_4="   *"

from collections import deque

vals={}

op=input().split(",")

lines=0
j=1
while j<len(op):
  lines+=int(op[j])
  j+=2
lines+=5
for i in range(lines):
  vals["cambus_"+str(i)]=""
op=deque(op)
i=0
num=op.popleft()
j=0
while i <len(num):
  k=0
  ue=op.popleft()
  j+=int(ue)
  if op:
    indent=int(op.popleft())
  if num[i]=="0":
    while k < lines:
      if k==j:
        vals["cambus_"+str(j)]+=zero_0+" "*indent
        vals["cambus_"+str(j+1)]+=zero_1+" "*indent
        vals["cambus_"+str(j+2)]+=zero_2+" "*indent
        vals["cambus_"+str(j+3)]+=zero_3+" "*indent
        vals["cambus_"+str(j+4)]+=zero_4+" "*indent
        k+=5
      else:
        vals["cambus_"+str(k)]+=" "*4+" "*indent
        k+=1
  if num[i]=="1":
    while k < lines:
      if k==j:
        vals["cambus_"+str(j)]+=one_0+" "*indent
        vals["cambus_"+str(j+1)]+=one_1+" "*indent
        vals["cambus_"+str(j+2)]+=one_2+" "*indent
        vals["cambus_"+str(j+3)]+=one_3+" "*indent
        vals["cambus_"+str(j+4)]+=one_4+" "*indent
        k+=5
      else:
        vals["cambus_"+str(k)]+=" "*1+" "*indent
        k+=1
  if num[i]=="2":
    while k < lines:
      if k==j:
        vals["cambus_"+str(j)]+=two_0+" "*indent
        vals["cambus_"+str(j+1)]+=two_1+" "*indent
        vals["cambus_"+str(j+2)]+=two_2+" "*indent
        vals["cambus_"+str(j+3)]+=two_3+" "*indent
        vals["cambus_"+str(j+4)]+=two_4+" "*indent
        k+=5
      else:
        vals["cambus_"+str(k)]+=" "*4+" "*indent
        k+=1
  if num[i]=="3":
    while k < lines:
      if k==j:
        vals["cambus_"+str(j)]+=three_0+" "*indent
        vals["cambus_"+str(j+1)]+=three_1+" "*indent
        vals["cambus_"+str(j+2)]+=three_2+" "*indent
        vals["cambus_"+str(j+3)]+=three_3+" "*indent
        vals["cambus_"+str(j+4)]+=three_4+" "*indent
        k+=5
      else:
        vals["cambus_"+str(k)]+=" "*4+" "*indent
        k+=1
  if num[i]=="4":
    while k < lines:
      if k==j:
        vals["cambus_"+str(j)]+=four_0+" "*indent
        vals["cambus_"+str(j+1)]+=four_1+" "*indent
        vals["cambus_"+str(j+2)]+=four_2+" "*indent
        vals["cambus_"+str(j+3)]+=four_3+" "*indent
        vals["cambus_"+str(j+4)]+=four_4+" "*indent
        k+=5
      else:
        vals["cambus_"+str(k)]+=" "*4+" "*indent
        k+=1
  if num[i]=="5":
    while k < lines:
      if k==j:
        vals["cambus_"+str(j)]+=five_0+" "*indent
        vals["cambus_"+str(j+1)]+=five_1+" "*indent
        vals["cambus_"+str(j+2)]+=five_2+" "*indent
        vals["cambus_"+str(j+3)]+=five_3+" "*indent
        vals["cambus_"+str(j+4)]+=five_4+" "*indent
        k+=5
      else:
        vals["cambus_"+str(k)]+=" "*4+" "*indent
        k+=1
  if num[i]=="6":
     while k < lines:
      if k==j:
        vals["cambus_"+str(j)]+=six_0+" "*indent
        vals["cambus_"+str(j+1)]+=six_1+" "*indent
        vals["cambus_"+str(j+2)]+=six_2+" "*indent
        vals["cambus_"+str(j+3)]+=six_3+" "*indent
        vals["cambus_"+str(j+4)]+=six_4+" "*indent
        k+=5
      else:
        vals["cambus_"+str(k)]+=" "*4+" "*indent
        k+=1
  if num[i]=="7":
     while k < lines:
      if k==j:
        vals["cambus_"+str(j)]+=seven_0+" "*indent
        vals["cambus_"+str(j+1)]+=seven_1+" "*indent
        vals["cambus_"+str(j+2)]+=seven_2+" "*indent
        vals["cambus_"+str(j+3)]+=seven_3+" "*indent
        vals["cambus_"+str(j+4)]+=seven_4+" "*indent
        k+=5
      else:
        vals["cambus_"+str(k)]+=" "*4+" "*indent
        k+=1
  if num[i]=="8":
     while k < lines:
      if k==j:
        vals["cambus_"+str(j)]+=eight_0+" "*indent
        vals["cambus_"+str(j+1)]+=eight_1+" "*indent
        vals["cambus_"+str(j+2)]+=eight_2+" "*indent
        vals["cambus_"+str(j+3)]+=eight_3+" "*indent
        vals["cambus_"+str(j+4)]+=eight_4+" "*indent
        k+=5
      else:
        vals["cambus_"+str(k)]+=" "*4+" "*indent
        k+=1
  if num[i]=="9":
    while k < lines:
      if k==j:
        vals["cambus_"+str(j)]+=nine_0+" "*indent
        vals["cambus_"+str(j+1)]+=nine_1+" "*indent
        vals["cambus_"+str(j+2)]+=nine_2+" "*indent
        vals["cambus_"+str(j+3)]+=nine_3+" "*indent
        vals["cambus_"+str(j+4)]+=nine_4+" "*indent
        k+=5
      else:
        vals["cambus_"+str(k)]+=" "*4+" "*indent
        k+=1
  i+=1

length=0
for i in vals:
  length=max(length,len(vals[i]))
for i in vals:
  vals[i]+=" "*(length-len(vals[i]))
  print(vals[i])

with open('out2.txt', mode = 'w') as f:
  for i in vals:
    f.write(vals[i]+"\n")
