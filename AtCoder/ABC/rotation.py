area=[]
for i in range(4):
  area.append(input())

for i in range(3,-1,-1):
  print(area[i][::-1])
