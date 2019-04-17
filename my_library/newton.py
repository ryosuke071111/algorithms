import math
from sympy import *
x_ans= math.sqrt(2)

#xの関数を作る
#例：√2を求めたいならx=√2,x^2=2 x^2-2=0
def f(x):
  x2=x**2
  return x2-40

i=0
loop=100
x=5
while i < loop:
  x=x-(f(x)/(2*x))
  i+=1
  print("xの値:",x)
