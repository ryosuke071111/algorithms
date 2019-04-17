import matplotlib.pyplot as plt
import statistics
import numpy as np
import math

with open('data1.txt') as f:
  nums = f.readlines()       #行ごとに読み込んでリスト化
  nums="".join(nums).split("\n")
  nums.pop()
  nums=list(map(lambda x:x.strip("(",).strip(')'),nums))
  nums=[i.split(",") for i in nums]
  x1=[int(i[0]) for i in nums]
  y1=[int(i[1]) for i in nums]

  #x1
  #-a
  tmp_x1=0
  for i,j in zip(x1,y1):
    tmp_x1+=i*j
  tmp2_x1=sum(x1)*sum(y1)
  upper=tmp_x1*(len(x1))-tmp2_x1
  tmp3_x1=sum(list(map(lambda x:x**2,x1)))*len(x1)
  tmp4_x1=sum(x1)**2
  lower=tmp3_x1-tmp4_x1
  a_1=upper/lower
  print(a_1)
  #-b
  tmp5_x1=sum(list(map(lambda x:x**2,x1)))*sum(y1)
  tmp6_x1=tmp_x1*sum(x1)
  upper=tmp5_x1-tmp6_x1
  lower=lower
  b_1=upper/lower


  def f1(x):
    return a_1*x+b_1

  x=np.arange(0,30,0.001)
  plt.scatter(x1,y1)
  plt.plot(x,f1(x))
  plt.show()

