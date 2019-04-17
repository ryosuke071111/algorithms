import numpy as np

class Node:
  def __init__(self, data):
    self.data = data
    self.right = None
    self.left = None

class BST:
  def __init__(self, number_list):
    self.root = None
    for node in number_list:
      self.insert(node)

  def insert(self, data)
  n = self.root
  if n == None:
    self.root = Node(data)
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

  def search_bool(self, search):
    n = self.root
    if n is None:
      return None
    else:
      lst =[]
      lst.append(n)
      while len(lst)>0:
        node =lst.pop()
        if node.data == search:
          return node.data
        if node.left is not None:
          lst.append(node.left)
        if node.right is not None:
          lst.append(node.right)
    return False

TARGET = 3797645

NUM = 1000000000000000000 # 1億個
list = range(NUM) # [0, 1, 2...]

low = 0
high = len(list)

while(low != high):
  center = (low + high)//2
  if(list[center] < TARGET):
    low = center + 1
  elif(TARGET > list[center]):
    high = center -1
  else:
    break:



