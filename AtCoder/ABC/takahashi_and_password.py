s=input()
k=int(input())
ls=set([])
for i in range(len(s)):
  j=i+k
  if j <=len(s):
    ls.add(s[i:j])
print(len(ls))

