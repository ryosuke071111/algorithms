f= open('prog1.txt')
f= f.readlines()
f= list(map(lambda x:x.strip("\n").split(),f))

for i,x,y in f:
  print(x)
