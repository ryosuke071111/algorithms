# 9:40-
f=open("prog1.txt")
f=f.read()[:-1].split('\n')
f=list(map(lambda x:x.split(),f))
for _,j,_ in f:
  print(j)
