# x = [4, 100, 1, 5, 400,53, 54, 53432,5678, 13, 65, 6, 0, 32]
import numpy as np
np.random.seed(10)
ls= np.random.randint(1, 100*9, 10**6)
print(ls)

def quick_sort(ls):
  left=[]
  right=[]
  if len(ls)<=1:
    return ls
  ref=ls[1]
  ref_cnt=0
  for i in ls:
    if i < ref:
      left.append(i)
    elif i > ref:
      right.append(i)
    else:
      ref_cnt+=1
  left=quick_sort(left)
  right=quick_sort(right)
  return left + ref_cnt*[ref]+ right


print(quick_sort(ls))
