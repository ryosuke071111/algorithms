x = [4, 100, 1, 5, 400,53, 54, 53432,5678, 13, 65, 6, 0, 32]

def quick_sort(arr):
  left =[]
  right =[]
  if len(arr)<=1:
    return arr
  ref = arr[0]
  ref_count = 0
  for ele in arr:
    if ele < ref:
      left.append(ele)
    elif ele > ref:
      right.append(ele)
    else:
      ref_count +=1
  left = quick_sort(left)
  right = quick_sort(right)
  return left + [ref]*ref_count + right

