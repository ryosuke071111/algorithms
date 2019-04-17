import numpy as np
np.random.seed(5)
ls= np.random.randint(1, 100, 10)
print(ls)
for i in range(10,0,-1):
  j=i
  while j<len(ls) and ls[j-1]>ls[j]:
    tmp=ls[j-1]
    ls[j-1]=ls[j]
    ls[j]=tmp
    j+=1

print(ls)
