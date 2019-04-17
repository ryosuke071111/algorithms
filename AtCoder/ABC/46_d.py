s=input()
budet=0
point=0

for i in s:
  if i == "g":
    if budet==0:
      budet+=1
    else:
      budet-=1
      point+=1
  elif i =="p":
    if budet==0:
      budet+=1
      point-=1
    else:
      budet-=1
print(point)

#強い人
S = [1 if _ == 'p' else 0 for _ in input()]
N = len(S)
#結局パーはs/2回しか出さない。自分と相手のパーの出した数の差
print(N // 2 - sum(S))
