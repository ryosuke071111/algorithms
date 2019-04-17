from collections import Counter

s=input()
t=input()
if len(Counter(t))==len(Counter(s)) and len(s)==len(t):
  ls1=sorted([Counter(t)[x] for i,x in enumerate(Counter(t))])
  ls2=sorted([Counter(s)[x] for i,x in enumerate(Counter(s))])
  for i in range(len(ls1)):
    if ls1[i]!= ls2[i]:
      print('No')
      exit()
  print('Yes')
else:
  print("No")


#なぜか文字の順番が目指すTと違くても正解になる


#思考過程
# 文字の種類の数が違うから
# abcccaaa -> cbaaaccc->
# aaabbccc

# acccaaa ->abbbaaa->cbbb
# aaabbbb


# print(Counter(s))
# print(Counter(t))

#文字の種類が奇数の時は種類ごとの数が違ったら入れ替えできない
#文字の種類が偶数の時は種類ごとの数が違っても入れ替えられる
