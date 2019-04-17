a =input()
#ord：()内のunicode番号
#chr：()内の文字列
alphabet=[chr(ord('a') + i) for i in range(26)]
if len(a) > 1:
  print(a[:-1])
elif a != "a":
  print(alphabet[alphabet.index(a)-1])
else:
  print(-1)

