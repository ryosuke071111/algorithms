s=input()
num=10**9
for i in range(len(s)):
  j=i+3
  if j <=len(s)+3:
    num=min(num, abs(int(s[i:j])-753))
print(num)
