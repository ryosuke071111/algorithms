f=open('mat2.txt')
a=f.read().split("\n")[:-1]
a=a[0].split(',')
a=list(map(lambda x:x.split(),a))
tmp=0
for i in range(len(a)):
  for j in range(len(a[i])):
    if i==j:
      tmp+=int(a[i][j])
print(tmp)

