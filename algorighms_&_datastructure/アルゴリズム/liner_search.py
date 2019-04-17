import numpy as np

x = np.random.randint(1, 1000, 1000)

def linear_search(aList, val):
    for x in aList:
        # if x == -1:
        #   print(x)
        if x == val:
            print(x)
            return True
    return False

linear_search(x, 2)

def liear_search(aList,val):
  for x in aList:
    if x == val:
      return True
  return False
