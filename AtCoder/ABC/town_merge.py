n=int(input())
towns=[]
for i in range(n):
  towns.append(input().split())
  towns[i][1]=int(towns[i][1])

pop=0
for i in range(len(towns)):
  pop+=towns[i][1]

half = pop//2

for i in range(len(towns)):
  if towns[i][1]>half:
    print(towns[i][0])
    exit()

print('atcoder')
