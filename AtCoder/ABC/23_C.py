#12:05-
r,c,k=map(int,input().split())
n=int(input())
RC=[list(map(int,input().split())) for i in range(n)]
rows=[0]*r
columns=[0]*c
for r,c in RC:
  rows[r-1]+=1
  columns[c-1]+=1
from collections import Counter
rows2=Counter(rows)
columns2=Counter(columns)
ans=0
#n個の行が何個あるか、列が何個あるかでk個になるような組み合わせ
for i in rows2:
  ans+=rows2[i]*columns2[k-i]

#被っているところがあるのでそこは+1じゃないと減らすようにする。逆に+1があったら増やす
for r,c in RC:
  if rows[r-1]+columns[c-1]==k:
    ans-=1
  if rows[r-1]+columns[c-1]==k+1:
    ans+=1
print(ans)

