# s=input()
# ls=["A",'C','G','T']
# ans=0
# u=0
# i=0
# while i < len(s):
#   if s[i] in ls:
#     cnt=1
#     i+=1
#     while i<len(s) and s[i] in ls:
#       i+=1
#       cnt+=1
#     ans=max(cnt,ans)
#   i+=1
# print(ans)

s=input()
n=len(s)
ans=0
for i in range(n):
  for j in range(i,n):
    #特定区間の配列要素の1つずつについて、所定の文字列にその1要素があるか。
    if all('ACGT'.count(c)==1 for c in s[i:j+1]):
      ans=max(ans,j-i+1)
print(ans)
