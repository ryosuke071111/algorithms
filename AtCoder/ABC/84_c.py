# n=int(input())
# ls=[]
# ans=[]
# for i in range(n-1):
#   ls.append(list(map(int,input().split())))

# def calculate(i):
#   time=ls[i][1]+ls[i][0]
#   for j in range(i+1,len(ls)):
#     if time<ls[j][1]:
#       time=ls[j][1]+ls[j][0]
#     else:
#       additional_time=ls[j][2]
#       while time %additional_time!=0:
#         time+=1
#       time+=ls[j][0]
#   return time

# for i in range(len(ls)):
#   ans.append(calculate(i))
# ans.append(0)
# for i in ans:
#   print(i)

 #----------------------------------------
n=int(input())
ls=[]
ans=[]
for i in range(n-1):
  ls.append(list(map(int,input().split())))

def calculate(i):
  time=ls[i][1]+ls[i][0]
  for j in range(i+1,len(ls)):
    if time<ls[j][1]:
      time=ls[j][1]+ls[j][0]
    elif time %ls[j][2]==0:
      time+=ls[j][0]
    else:
      time+=ls[j][0]+ls[j][2]-time%ls[j][2]
  return time

for i in range(len(ls)):
  ans.append(calculate(i))
ans.append(0)
for i in ans:
  print(i)
