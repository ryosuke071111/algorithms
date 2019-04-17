#bit
a=list(map(int,input()))
n=len(a)
for i in range(1<<n-1):
  tmp=a[0]
  string=str(a[0])
  # print(bin(i))
  for j in range(1,n):
    if (i>>j-1)&1==0:
      tmp-=a[j]
      string+="-"
      string+=str(a[j])
    else:
      tmp+=a[j]
      string+="+"
      string+=str(a[j])
    # print("",tmp)
  if tmp==7:
    print(string+"=7")
    exit()

#dfs
a=list(map(int,input()))
n=len(a)

def dfs(tmp,cur,strs):
  if cur==n:
    if tmp==7:
      print("".join(strs)+"=7")
      exit()
    else:
      return
  ret0=dfs(tmp+a[cur],cur+1,strs+["+"]+[str(a[cur])])
  ret1=dfs(tmp-a[cur],cur+1,strs+["-"]+[str(a[cur])])
dfs(a[0],1,[str(a[0])])

