def min_heapify(A,i):
  l = 2*i
  r = 2*i+1
  minimum = i

  if l < len(A) and A[l] < A[i]:
    minimum = l
  if r < len(A) and A[r] < A[minimum]:
    minimum = r
  if minimum != i:
    tmp = A[i]
    A[i] = A[minimum]
    A[minimum] = tmp
    min_heapify(A,minimum)

def build_heap(A):
  i = len(A)//2
  while i >= 0:
    min_heapify(A,i)
    i -= 1
  return A

def insert(A,num):
  A.append(num)
  minimum = A.index(num)
  build_heap(A)
  return A

def deletemin(A):
  num = A.pop(0)
  build_heap(A)
  return A, num


A = [i for i in range(10,3,-1)]
print(A)
print(build_heap(A))
print(insert(A,0))
print(deletemin(A))

#インデントがずれると常に自分と自分を入れ替えてのループになって止まらなくなる
