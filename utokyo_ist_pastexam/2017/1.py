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

num=input()
for i in num:
  if i=="0":
    cambus_0+=zero_0+" "*2
    cambus_1+=zero_1+" "*2
    cambus_2+=zero_2+" "*2
    cambus_3+=zero_3+" "*2
    cambus_4+=zero_4+" "*2
  if i=="1":
    cambus_0+=one_0+" "*2
    cambus_1+=one_1+" "*2
    cambus_2+=one_2+" "*2
    cambus_3+=one_3+" "*2
    cambus_4+=one_4+" "*2
  if i=="2":
    cambus_0+=two_0+" "*2
    cambus_1+=two_1+" "*2
    cambus_2+=two_2+" "*2
    cambus_3+=two_3+" "*2
    cambus_4+=two_4+" "*2
  if i=="3":
    cambus_0+=three_0+" "*2
    cambus_1+=three_1+" "*2
    cambus_2+=three_2+" "*2
    cambus_3+=three_3+" "*2
    cambus_4+=three_4+" "*2
  if i=="4":
    cambus_0+=four_0+" "*2
    cambus_1+=four_1+" "*2
    cambus_2+=four_2+" "*2
    cambus_3+=four_3+" "*2
    cambus_4+=four_4+" "*2
  if i=="5":
    cambus_0+=five_0+" "*2
    cambus_1+=five_1+" "*2
    cambus_2+=five_2+" "*2
    cambus_3+=five_3+" "*2
    cambus_4+=five_4+" "*2
  if i=="6":
    cambus_0+=six_0+" "*2
    cambus_1+=six_1+" "*2
    cambus_2+=six_2+" "*2
    cambus_3+=six_3+" "*2
    cambus_4+=six_4+" "*2
  if i=="7":
    cambus_0+=seven_0+" "*2
    cambus_1+=seven_1+" "*2
    cambus_2+=seven_2+" "*2
    cambus_3+=seven_3+" "*2
    cambus_4+=seven_4+" "*2
  if i=="8":
    cambus_0+=eight_0+" "*2
    cambus_1+=eight_1+" "*2
    cambus_2+=eight_2+" "*2
    cambus_3+=eight_3+" "*2
    cambus_4+=eight_4+" "*2
  if i=="9":
    cambus_0+=nine_0+" "*2
    cambus_1+=nine_1+" "*2
    cambus_2+=nine_2+" "*2
    cambus_3+=nine_3+" "*2
    cambus_4+=nine_4+" "*2
with open('out1.txt', mode = 'w') as f:
  f.write(str(cambus_0)+"\n")
  f.write(str(cambus_1)+"\n")
  f.write(str(cambus_2)+"\n")
  f.write(str(cambus_3)+"\n")
  f.write(str(cambus_4)+"\n")

# print(*cambus_0)
# print(*cambus_1)
# print(*cambus_2)
# print(*cambus_3)
# print(*cambus_4)

