import matplotlib.pyplot as plt
import numpy as np

f=open('data1.txt')
f=f.readlines()
f=list(map(lambda x:x.strip('\n').strip('(').strip(')'),f))
f=list(map(lambda x:x.split(','),f))
max_y=0
max_x=0
ans=[]
xs=[]
ys=[]
for i,v in f:
  if int(v)>max_y:
    max_y=int(v)
    ans=[i,v]
  if int(i)>max_x:
    max_x=int(i)
  xs.append(int(i))
  ys.append(int(v))

def get_a(xs,ys):
  a=0
  ue=0
  shita=0
  sum_xy=0
  Nxy=0
  for x,y in zip(xs,ys):
    sum_xy+=x*y
  Nxy=len(xs)*sum_xy
  squre_x=list(map(lambda x:x**2,xs))
  Nxx=len(xs)*sum(squre_x)
  ue=Nxy-(sum(xs)*sum(ys))
  shita=Nxx-(sum(xs)**2)
  # print("xs:",xs,"ys:",ys,'ue:',ue,"shita:",shita)
  if ue !=0 and shita!=0:
    return ue/shita
  else:
    pass

def get_b(xs,ys):
  b=0
  ue=0
  shita=0
  sum_xy=0
  for x,y in zip(xs,ys):
    sum_xy+=x*y
  squre_x=list(map(lambda x:x**2,xs))
  Nxx=len(xs)*sum(squre_x)
  ue=sum(squre_x)*sum(ys)-(sum_xy*sum(xs))
  shita=Nxx-(sum(xs)**2)
  if ue !=0 and shita!=0:
    return ue/shita
  else:
    pass

def E(xs,ys,f):
  e=0
  for x,y in zip(xs,ys):
    e+=(y-f(x))**2
  return e


def f(x):
  return a*x+b
def f():
  e=10**9
  a=10**9
  b=10**9
  xm=0
  for i in range(1,30):
    first_half_x=xs[:i+1]
    second_half_x=xs[i+1:]
    first_half_y=ys[:i+1]
    second_half_y=ys[i+1:]
    a1=get_a(first_half_x,first_half_y)
    b1=get_b(first_half_x,first_half_y)
    a2=get_a(second_half_x,second_half_y)
    b2=get_b(second_half_x,second_half_y)
    tmp=0
    for j in range(len(xs)):
      if xs[j]<xs[i] and a1 and b1:
        tmp+=(ys[j]-(a1*xs[j]+b1))
      elif a2 and b2:
        tmp+=(ys[j]-(a2*xs[j]+b2))
    if tmp<e:
      e=tmp
      xm=i
  return a1,b1,a2,b2,e,xm
print(f())
# X=[i for i in range(1,31)]
# Y=list(map(lambda x:f1(x),X))
# plt.plot(X,Y,"bo")
# ax=plt.subplot()
# ax.scatter(xs,ys)
# plt.show()
