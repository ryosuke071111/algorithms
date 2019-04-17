s = input()
t = input()

if len(t)>len(s):
  print("UNRESTORABLE")
  exit()

ans = []

for i in range(len(s)-len(t)+1):
  for j in range(len(t)):
    if s[i+j] != t[j] and s[i+j]!='?':
      break #jのループが止まる
  else:
      #:iまでの文字はSを引き継ぎ、tを足し、残りは引き継ぎ、?部分はaに
      # print('Bの方')
    ans.append((s[:i]+t+s[i+len(t):]).replace('?','a'))
    print(ans)

if len(ans) == 0:
  print('UNRESTORABLE')
else:
  ans.sort()
  print(ans[0])
