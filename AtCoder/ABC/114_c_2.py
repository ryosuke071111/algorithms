#10:13-
# n=int(input())
# s=[]
# def dfs(string,cur):
#   if cur==len(str(n)):
#     if string.count('3')>0 and string.count('5')>0 and string.count('7'):
#       s.append(string)
#     return
#   dfs(string+"",cur+1)
#   dfs(string+"7",cur+1)
#   dfs(string+"5",cur+1)
#   dfs(string+"3",cur+1)
# dfs("",0)

# cnt=0
# for i in set(s):
#   if int(i)<=n:
#     cnt+=1
# print(cnt)

n=int(input())
def dfs(s):
  if int(s)>n:
    return 0
  ret = 1 if all(s.count(c) for c in "753") else 0
  for c in '753':
    ret+=dfs(s+c)
  return ret
print(dfs("0"))
