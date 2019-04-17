import numpy as np


ls=np.array([["a","b","c"],["a","b","c"],["a","b","c"]],dtype=str)
ls[2:,1:]=np.core.defchararray.add(ls[2:,1:],["a"])
print(ls)
