#自分の回答
from collections import Counter
n=int(input())
a=input()
b=input()
c=input()
i=0
ans=""
while i<len(a):
  tmp=[]
  tmp.append(a[i])
  tmp.append(b[i])
  tmp.append(c[i])
  tmp=Counter(tmp)
  ans+=tmp.most_common()[0][0]
  i+=1
diff=0
i=0
while i<len(a):
  if a[i]!=ans[i]:
    diff+=1
  if b[i]!=ans[i]:
    diff+=1
  if c[i]!=ans[i]:
    diff+=1
  i+=1
print(diff)

#短い回答
n=int(input())
a,b,c=input(),input(),input()
ans=0
for i in range(n):
  ans+=len(set([a[i],b[i],c[i]]))-1
print(ans)
