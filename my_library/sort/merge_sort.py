import numpy as np
np.random.seed(10)
ls= np.random.randint(1, 100*9, 10**5)
print(ls)

def merge_sort(ls):
  if len(ls)<=1:
    return ls
  mid=len(ls)//2
  left=ls[:mid]
  right=ls[mid:]
  left=merge_sort(left)
  right=merge_sort(right)
  return merge(left,right)

def merge(left,right):
  merged=[]
  l,r=0,0
  while l<len(left) and r<len(right):
    if left[l]<right[r]:
      merged.append(left[l])
      l+=1
    else:
      merged.append(right[r])
      r+=1
  if l<len(left):
    merged.extend(left[l:])
  if r<len(right):
    merged.extend(right[r:])

  return merged


print(merge_sort(ls))
