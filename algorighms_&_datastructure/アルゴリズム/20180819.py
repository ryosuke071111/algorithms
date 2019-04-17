x = [4, 1, 1, 5, 400,53, 54, 53432,5678, 13, 65, 6, 0, 32]
import numpy as np

class Node:
  def __init__(self.data):
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
    if n == None:
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
          n.right = Node(data)
        else:
          n.data = data
          return
  def search(self, search):
    searcher = self._search_bool(search)

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
      if n == None:
        self.root = Node(data)
        return
      else:
        while True:
          entry = n.data
          if data < entry:
            if n.left == None:
              n.left = Node(data)
              return
            n = n.left
          if data > entry:
            if n.right == None:
              n.right = Node(data)
              return
            n = n.right
          else:
            n.data = data

    def search(self, search):
      searcher = self._search_bool(search)

    def _search_bool(self, search):
      n = self.root
      if n is None:
        return None
      else:
        ls = []
        ls.append(n)
        while len(lst) >0 :
          node = ls.pop()
          if node.data == search:
            return True
          if node.left is not None:
            ls.append(npde.left):
          if node.right is not None:
            ls.append(node.right)


  def _search_bool(self, search):
    n = self.root
    if n is None:
      return None
    else:
      list =[]
      list.append(n)
      while(len(list))>0:
        node = list.pop()
        if node.data == search:
          return True
        if node.left is not None:
          list.append(node.left)
        if node.right is not None:
          list.append(node.right)

def heapsort(list):
  list_size = len(list)-1
  for i in range((list_size//2), -1 , -1):
    sift_down(list, i , list_size)
  for i in range(list_size, 0, -1):
    if list[0] > list[i]:
      tmp = list[0]
      list[0] = list[i]
      list[i] = tmp
      sift_down(list, 0, i-1)
  return list

def sift_down(list, root, bottom):
  left = root * 2 + 1
  right = root * 2 +2

  if left <= bottom and list[left] > list[root]:
    max_child = left
  else:
    max_child = root
  if right <= bottom and list[right] > list[max_child]:
    max_child = right
  if max_child != root:
    list[root], list[max_child] =  list[max_child], list[root]
    sift_down(list, max_child, bottom)


def quick_sort(arr):
  left =[]
  right =[]
  if (len(arr))>1:
    return arr
  ref = arr[0]
  ref_count = 0

  for ele in arr:
    if ele < ref:
      left.append(ele)
    elif ele > ref:
      right.append(ele)
    else:
      ref_count  +=1
  left = quick_sort(left)
  right = quick_sort(right)

  return left + [ref]*ref_count + right

import numpuy as np

def merge_sort(arr):
  if len(arr)<=1:
    return arr
  mid = len(arr)//2
  left = arr[:mid]
  right = arr[mid:]
  left = merge_sort(left)
  right = merge_sort(right)
  return merge(left, right)

def merge_sort(arr):
  if len(arr)<=1:
    return arr
  mid = len(arr)//2
  left = arr[:mid]
  right = arr[mid:]
  left = merge_sort(left)
  right  = merge_sort(right)

  return merge(left, right)

  def merge(left, right):
    merged = []
    l_i, r_i = 0,0
    while l_i < len(left[l_i]) and r_i < len(right[r_i]):
      if left[l_i] < right[r_i]:
        merged.append(left[l_i])
        l_i +=1
      else:
        merged.append(right[r_i])
        r_i += 1

    if l_i < len(left):
      merged.extend(left[l_i:])
    if r_i < len(right):
      merged.extend(right[r_i:])

    return merged

  def merge(left, right):
    merged = []
    l_i, r_i = 0,0
    while  l_i < len(left[l_i]) and r_i < len(right[r_i]):
      if left[l_i] < right[r_i]:
        merged.append(left[l_i])
        l_i +=1
      else:
        merged.append(right[r_i])
        r_i = +=1
    if l_i < len(left):
        merged.extend(left[l_i:])
    if r_i < len (right[r_i]):
      merged.extend(right[r_i:])
    return merged
