#8:50-
n=int(input())
s=[list(map(int,input().split())) for i in range(n)]
s.sort(key=lambda x:x[2],reverse=True)
x0,y0,h0=s[0]
for cx in range(101):
  for cy in range(101):
    H=h0+abs(x0-cx)+abs(y0-cy)
    for xi,yi,hi in s:
      if hi != max(0,H-abs(xi-cx)-abs(yi-cy)):
        break
    else:
      print(x,y,H)
      exit()









# x0,y0,h0=s[0] #少なくとも一つはhi>0だからhの最大のものを取る
# for x in range(101):
#   for y in range(101):
#     H=h0+abs(x0-x)+abs(y0-y) #h0=H-abs(x0-x)+abs(y0-y)の式変形(hiが0以上の前提)
#     for xi,yi,hi in s:
#       if hi!=max(0,H-abs(xi-x)-abs(yi-y)):
#         break
#     else: #for文の下のelseは(breakすることなしに)for文を抜けることができたら反映
#       print(x,y,H)
#       exit()
