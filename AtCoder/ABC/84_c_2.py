#13:44-
n=int(input())
ls=[]
for i in range(n-1):
  c,s,f=map(int,input().split())
  ls.append(s)
  ls=list(map(lambda x:(x+c+(0 if x%f==0 else (f-x%f)) if s<=x else s+c),ls))
ls=ls+[0]
print(*ls,sep="\n")

#xがmod fで割り切れない場合はx+(f-x%f)
