n=int(input())
ls=[list(map(int,input().split())) for i in range(n)]
ls=sorted(ls,key=lambda x:sum(x),reverse=True)
taka=sum([ls[i][0] for i in range(0,len(ls),2)])
aoki=sum([ls[i][1] for i in range(1,len(ls),2)])

print(taka-aoki)
