a=list(input())
l = ["+","-"]

for p in l:
  for q in l:
    for r in l:
      x = a[0]+p+a[1]+q+a[2]+r+a[3]
      if eval(x) == 7:
        print(x+  '=7')
        exit()
l = ['+','-']
