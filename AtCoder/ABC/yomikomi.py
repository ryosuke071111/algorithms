with open('goi.txt') as f:
  a=f.readlines()
count=0
for i in a:
  if "・" in i:
    count+=1
print(count)
