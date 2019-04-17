import numpy as np
np.random.seed(0)
ls= np.random.randint(1, 100, 10)
print(ls)

for j in range(1,10):
  i=j-1
  key=ls[j]
  while i >0 and ls[i]>key:
    ls[i+1]=ls[i]
    i-=1
  ls[i+1]=key

print(ls)
