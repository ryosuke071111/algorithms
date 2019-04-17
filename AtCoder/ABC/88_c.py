area=[list(map(int,input().split())) for i in range(3)]
count=0
for a1 in range(area[0][0]+1):
  b1=area[0][0]-a1
  b2=area[0][1]-a1
  b3=area[0][2]-a1
  a2=area[1][0]-b1
  a3=area[2][0]-b1
  if b1>=0 and b2>=0 and b3>=0 and a2>=0 and a3>=0:
    if a2+b2== area[1][1]:
      if a2+b3==area[1][2]:
        if a3+b1==area[2][0]:
          if a3+b2==area[2][1]:
            if a3+b3==area[2][2]:
              print('Yes')
              exit()
print('No')
