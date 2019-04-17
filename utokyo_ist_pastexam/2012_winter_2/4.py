import matplotlib.pyplot as plt
import numpy as np

f=open('data1.txt')
f=f.readlines()
f=list(map(lambda x:x.strip('\n').strip('(').strip(')'),f))
f=list(map(lambda x:x.split(','),f))
max_y=0
ans=[]
xs=[]
ys=[]
for i,v in f:
  if int(v)>max_y:
    max_y=int(v)
    ans=[i,v]
  xs.append(int(i))
  ys.append(int(v))

def a():
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
  return ue/shita

def b():
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
  return ue/shita

a=a()
b=b()
def f(x):
  return a*x+b

X=[i for i in range(1,31)]
Y=list(map(lambda x:f(x),X))
plt.plot(X,Y,"bo")
ax=plt.subplot()
ax.scatter(xs,ys)
plt.show()
