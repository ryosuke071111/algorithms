import numpy as np

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

  def search(self, search):
    searcher = self._search_bool(search)
    if searcher is None:
      return None
    if searcher == True:
      return True
    if searcher == False:
      return False

  def _search_bool(self, search):
    n = self.root
    if n is None:
      return None
    else:
      lst =[]
      lst.append(n)
      while len(lst)>0:
        node = lst.pop()
        if node.data == search:
          return True
        if node.left is not None:
          lst.append(node.left)
        if node.right is not None
          lst.append(node.right)
      return False












