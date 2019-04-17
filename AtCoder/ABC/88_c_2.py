C=[list(map(int,input().split())) for i in range(3)]
for a1 in range(101):
  b1=C[0][0]-a1
  b2=C[0][1]-a1
  b3=C[0][2]-a1
  a2=C[1][0]-b1
  a3=C[2][0]-b1
  if b1>=0 and b2>=0 and b3>=0 and a2>=0 and a3>=0:
    if a2+b2==C[1][1]:
      if a2+b2==C[1][1]:
        if a2+b3==C[1][2]:
          if a3+b1==C[2][0]:
            if a3+b2==C[2][1]:
              if a3+b3==C[2][2]:
                print('Yes')
                exit()
print('No')

#どれも決まらない場合は一つを決め打ちで他が成立するか試す

