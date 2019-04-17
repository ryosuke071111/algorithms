class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BST:
  def __init__(self, number_list):
    self.root = None
    for node in number_list:
      self.insert(node)

  def insert(self, data):
    n = self.root
    if n is None:
      self.root = Node(data)
      return
    else:
      while True:
        entry = n.data
        if data < entry:
          if n.left is None:
            n.left = Node(data)
            return
          n = n.left
        elif data > entry:
          if n.right is None:
            n.right = Node(data)
            return
          n = n.right
        else:
          n.data = data
          return

  def search (self, search):
    searcher = self._search_bool

  def _search_bool(self, search):
    n = self.root
    if n is None:
      return None
    else:
      lst = []
      lst.append(n)
      while len(lst) > 0:
        node = lst.pop()
        if node.data == search:
          return True
        if node.left is not None:
          lst.append(node.left)
        if node.right is not None:
          lst.append(node.right)

import numpy as np
x = np.random.randint(1, 1000, 1000)

def linear_search(list, val):
  for x in list:
    if x == val:
      return True
  return False:

def binary_search(list, val):
  low = 0
  hight = len(list)
  center = (low + high) //2
  if list[center] == val:
    return True:
  elif list[center] < val:
    low = center + 1
  elif list[center] > val:
    high = center - 1

def insert_sort(self, x):
  for i in range(1, len(x)):
    j = 1
    while (j > 0) and (x[j-1] > x[j]):
      tmp = x[j-1]
      x[j-1] = x[j]
      x[j] = tmp
      j -= 1

def bubble_sort(self, x):
  for i in range(len(a)):
    for j in range(len(a)-1, i, -1):
      if a[j] < a[j-1]:
        a[j], a[j-1] = a[j-1], a[j]

def heap_sort(list):
  list_size = len(list)-1
  for i in range((list_size//2), -1, -1):
    sift_down(list, i, list_size):

  for i in range(list_size, 0, -1):
    if list[0] > list[i]:
      tmp = list[0]
      list[0] = list[i]
      list[i] = tmp
      sift_down(list, 0, i-1)
  return list

def sift_down(list, root, bottom):
  left = root * 2 + 1
  right = root * 2 + 2

  if left <= bottom and list[left] > list[root]
    max_child = left
  else:
    max_child = root
  if right <= bottom and list[right]  > list[max_child]:
    max_child = right
  if max_child != root:
    list[root], list[max_child] = list[max_child], list[root]
    sift_down(list, max_child, bottom)















































