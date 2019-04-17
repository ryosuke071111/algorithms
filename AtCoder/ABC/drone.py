s=input()
t=int(input())
xy=[0,0]
addi=0

for i in s:
  if i == "U":
    xy[1] +=1
  elif i == "D":
    xy[1] -=1
  elif i == "L":
    xy[0] -=1
  elif i == "R":
    xy[0] +=1
  else:
    addi+=1


if t==1:
  print(abs(xy[1])+abs(xy[0])+addi)
else:
  print(max(abs(xy[1])+abs(xy[0])-addi,len(s)%2))
