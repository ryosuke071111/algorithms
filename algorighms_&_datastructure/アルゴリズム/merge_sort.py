import numpy as np
x = np.random.randint(0, 300, 100)


def merge_sort(arr):
  if len(arr)<=1:
    return arr
  mid = len(arr)//2
  left = arr[:mid]
  right = arr[mid:]
  left = merge_sort(left)
  right = merge_sort(right)
  return merge(left, right)

def merge(left,right):
  merged=[]
  l_i ,r_i = 0,0
  while l_i < len(left) and r_i < len(right):
    if left[l_i] < right[r_i]:
      merged.append(left[l_i])
      l_i +=1
    else:
      merged.append(right[r_i])
      r_i +=1
  if l_i < len(left):
   merged.extend(left[l_i:])
  if r_i < len(right):
   merged.extend(right[r_i:])
  return merged

print(x)
x = merge_sort(x)
print(x)
