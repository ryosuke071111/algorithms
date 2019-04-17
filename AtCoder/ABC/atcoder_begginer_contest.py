n=int(input())
length=len(str(n))

if int(str(n)[0])>= int(str(n)[-1]) and int(str(n)[0])>= int(str(n)[1]):
  print((str(n)[0])*length)
else:
  print(str((int(str(n)[0]))+1)*length)
