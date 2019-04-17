s=j=0  #水たまりの総面積 とその箱
a =[] #「\の入った個数」
b =[] #水たまりの個数
d =[] #水たまりのそれぞれの面積

for i, x in enumerate(input()):
  if x == '\\':
    a += [i]
  elif x =='/' and a:
    j = a.pop()
    c = i-j
    s += c
    while b and b[-1] > j:
      c+=d.pop()
      b.pop()
    b +=[j]
    d +=[c]
print(s)
print(len(b), *(d))
