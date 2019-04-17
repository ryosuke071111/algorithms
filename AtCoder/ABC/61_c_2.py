#愚直シミュレーションせずにn番目を求める
n,k=map(int,input().split())
cnt=0
dic={}
for i in range(n):
  a,b=map(int,input().split())
  if a in dic:
    dic[a]+=b
  else:
    dic[a]=b

dic=sorted(dic.items())
for i,j in dic:
  cnt+=j
  if k<=cnt:
    print(i)
    exit()
