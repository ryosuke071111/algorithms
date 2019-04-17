with open('7.txt') as f:
  a = f.read().split("\n")
  a=list(map(lambda x:x.split(","),a))
  a.pop()

for _,_,i,j in a:
  print(int(i)*int(j))
