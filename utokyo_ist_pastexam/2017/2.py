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

cambus_0=""
cambus_1=""
cambus_2=""
cambus_3=""
cambus_4=""

f=open("out1.txt")
a=f.read().split('\n')
for i in range(len(a)):
  a[i]+="  "
line0=[]
line1=[]
line2=[]
line3=[]
line4=[]

num_list0=["****  ","*  *  "]
num_list1=["   |  ","|  |  ","|     "]
num_list2=["****  ","*  *  ","   *  "]
num_list3=["   |  ","|  |  ","|     "]
num_list4=["   *  ","****  "]

i=5
while i<len(a[0]):
  if a[0][i-5:i+1] not in num_list0 or a[1][i-5:i+1] not in num_list1 or a[2][i-5:i+1] not in num_list2 or a[3][i-5:i+1] not in num_list3 or a[4][i-5:i+1] not in num_list4:
    line0.append(a[0][i-5])
    line1.append(a[1][i-5])
    line2.append(a[2][i-5])
    line3.append(a[3][i-5])
    line4.append(a[4][i-5])
    i+=3
    continue
  line0.append(a[0][i-5:i+1])
  line1.append(a[1][i-5:i+1])
  line2.append(a[2][i-5:i+1])
  line3.append(a[3][i-5:i+1])
  line4.append(a[4][i-5:i+1])
  i+=6

ans=[]
i=0
while i < len(line0):
  if len(line0[i])==1:
    ans.append(1)
  else:
    if line0[i][:4]==zero_0:
      if line1[i][:4]==zero_1:
        if line2[i][:4]==zero_2:
          if line3[i][:4]==zero_3:
            if line4[i][:4]==zero_4:
              ans.append(0)
    if line0[i][:4]==two_0:
      if line1[i][:4]==two_1:
        if line2[i][:4]==two_2:
          if line3[i][:4]==two_3:
            if line4[i][:4]==two_4:
              ans.append(2)
    if line0[i][:4]==three_0:
      if line1[i][:4]==three_1:
        if line2[i][:4]==three_2:
          if line3[i][:4]==three_3:
            if line4[i][:4]==three_4:
              ans.append(3)
    if line0[i][:4]==four_0:
      if line1[i][:4]==four_1:
        if line2[i][:4]==four_2:
          if line3[i][:4]==four_3:
            if line4[i][:4]==four_4:
              ans.append(4)
    if line0[i][:4]==five_0:
      if line1[i][:4]==five_1:
        if line2[i][:4]==five_2:
          if line3[i][:4]==five_3:
            if line4[i][:4]==five_4:
              ans.append(5)
    if line0[i][:4]==six_0:
      if line1[i][:4]==six_1:
        if line2[i][:4]==six_2:
          if line3[i][:4]==six_3:
            if line4[i][:4]==six_4:
              ans.append(6)
    if line0[i][:4]==seven_0:
      if line1[i][:4]==seven_1:
        if line2[i][:4]==seven_2:
          if line3[i][:4]==seven_3:
            if line4[i][:4]==seven_4:
              ans.append(7)
    if line0[i][:4]==eight_0:
      if line1[i][:4]==eight_1:
        if line2[i][:4]==eight_2:
          if line3[i][:4]==eight_3:
            if line4[i][:4]==eight_4:
              ans.append(8)
    if line0[i][:4]==nine_0:
      if line1[i][:4]==nine_1:
        if line2[i][:4]==nine_2:
          if line3[i][:4]==nine_3:
            if line4[i][:4]==nine_4:
              ans.append(9)
  i+=1

print(*ans)















