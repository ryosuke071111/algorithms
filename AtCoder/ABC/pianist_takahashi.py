doremi = "WBWBWWBWBWBW"*4
s = input()

if s==doremi[0:20] or s==doremi[1:21]:
    print("Do")
elif s==doremi[2:22] or s==doremi[3:23]:
    print("Re")
elif s==doremi[4:24]:
    print("Mi")
elif s==doremi[5:25] or s==doremi[6:26]:
    print("Fa")
elif s==doremi[7:27] or s==doremi[8:28]:
    print("So")
elif s==doremi[9:29] or s==doremi[10:30]:
    print("La")
else:
    print("Si")
