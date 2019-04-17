a = int(input())
b = int(input())
c = int(input())

box =[]
box.append(a)
box.append(b)
box.append(c)

def judge(a):
  if max(box) == a:
    print (1)
  elif min(box) == a:
    print(3)
  else:
    print(2)

judge(a)
judge(b)
judge(c)
