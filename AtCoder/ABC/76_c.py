s=input()
t=input()
ans="UNRESTORABLE"
for i in range(len(s)-len(t)+1):
  flag=True
  for j in range(len(t)):
    if s[i+j]==t[j] or s[i+j]=="?":
      continue
    else:
      flag=False
  if flag:
    ans=s[:i]+t+s[i+len(t):]
    ans=ans.replace("?","a")
print(ans)

#文字列の部分一致
#一致条件①同じ②「?」がある
#後ろで一致したものを優先的に回答とする

