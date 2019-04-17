n,m=map(int,input().split())
X=sorted(list(map(int,input().split())))
ans=[]
if m<n:
  print(0)
  exit()
for i in range(m-1):
  ans.append(X[i+1]-X[i])
ans=sorted(ans)
print(sum(ans[:m-n]))
# init=[]
# tmp=0
# i=1
# while i<len(X):
#   init.append([X[i]-X[i-1],i])
#   i+=1
# init.sort(reverse=True,key=lambda x:x[0])
# init=list(map(lambda x:x[1],init))
# ans=0
# init=sorted(init[:n-1])
# if len(init)==0:
#   print(X[-1]-X[0])
#   exit()
# tmp=0
# for i in init:
#   ans+=(X[i-1]-X[tmp])
#   tmp=i
# try:
#   if i!=len(X)-1:
#     ans+=X[-1]-X[i]
# except IndexError:
#   print(0)
#   exit()
# print(ans)
