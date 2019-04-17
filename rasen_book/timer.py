import numpy as np
import timeit

def insert_sort():
  np.random.seed(0)
  n =  100
  list1 = np.random.randint(1,10,n)

  #i = 0の時はエラーが出る
  for i in range(1, len(list1)):
    j = i
    while (j>0) and (list1[j] < list1[j-1]):
      tmp = list1[j-1]
      list1[j-1] =  list1[j]
      list1[j] = tmp
      j -= 1
    print(list1)

loop = 10
result = timeit.timeit('insert_sort()', globals=globals(), number=loop)
print(result / loop)
