n,x =map(int,input().split())
deg_like =[list(map(int,input().split())) for i in range(n)]

deg_like = sorted(deg_like,key=lambda x:(x[1]),reverse=True)
suma=0

deg_like[0][0]+=1*x

for i in range(n):
  suma += deg_like[i][0]* deg_like[i][1]

print(suma)
