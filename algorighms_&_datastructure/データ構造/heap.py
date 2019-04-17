# 最小の値を常にrootにする
heap = []

def swap (list,a,b):
  list[a],list[b] = list[b],list[a]
  return a, b

def insert(heap,object):
  heap.append(object)
  i = heap.index(object)
  while i > 0:
    if (heap[int((i-1)/2)] > heap[i]):
      swap (heap, int((i-1)/2), i)
      i = int((i-1)/2)
    else:
      i = 0

def deletemin(heap):
  heap[0]=heap[-1]
  heap.pop()
  print(heap)
  i = 0
  last = heap[-1]
  while i < (heap.index(last)):
    try:
      if (heap[i] > heap[i*2+1]):
        if (heap[i*2+2] < heap[i*2+1]):
          swap(heap, i, i*2+2)
          i = i*2+2
        else:
          swap(heap, i, i*2+1)
          i = i*2+1
      elif (heap[i]>heap[i*2+2]):
        swap(heap, i, i*2+2)
        i = i*2+2
      else:
        return
    except:
      return heap

insert(heap, 31)
print(heap)
insert(heap, 21)
print(heap)
insert(heap, 48)
print(heap)
insert(heap, 9)
print(heap)
deletemin(heap)
print(heap)
insert(heap, 26)
print(heap)
insert(heap, 13)
print(heap)
deletemin(heap)
print(heap)
