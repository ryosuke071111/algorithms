import random
l=list(range(10))

f=open('graph1.txt')
a=f.read().strip('\n').split()
with open('graph2.txt', mode = 'w') as f:
  for i in a:
    print(i)
    random.shuffle(l)
    if l[0]==8:
      f.write("!"+i+"\n")
    else:
      f.write(i+"\n")
