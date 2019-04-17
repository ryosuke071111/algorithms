class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

  def get(self):
    return self.data

  def set(self, data):
    self.data = data

  def getChildren(self):
    children =[]
    if(self.left != None):
      children.append(self.left)
    if(self.right != None):
      children.append(self.right)
    return children

class BST:
  def __init__(self,data):
    self.root = None
    self.data = data
    self.left = None
    self.right = None

  def setRoot(self,data):
    self.root = Node(data)

  def insert(self, data):
    if (self.root is None):
      self.setRoot(data)
    else:
      self.insertNode(self.root, data)

  def insertNode(self, currentNode, data):
    if (data <= currentNode.data):
      if(currentNode.left):
        self.insertNode(currentNode.left,data)
      else:
        currentNode.left = Node(data)
    elif(data > currentNode.data):
      if(currentNode.right):
        self.insertNode(currentNode.right, data)
      else:
        currentNode.right = Node(data)
  def find(self, data):
    return self.findNode(self.root,data)

  def findNode(self, currentNode, data):
    if (currentNode is None):
      return False
    elif(data == currentNode.data):
      return True
    elif(data < currentNode.data):
      return self.findNode(currentNode.left, data)
    else:
      return self.findNode(currentNode.right, data)

  # def minimum(self):
  #   while self.left:
  #     self = self.left
  #   return self

  #  def maximum(self):
  #   while self.right:
  #     self = self.right
  #   return self


aiueo = BST(10)
print(aiueo.data)
aiueo.insertNode(aiueo, 20)
print(aiueo.right.data)
aiueo.insertNode(aiueo, 5)
print(aiueo.left.data)
print(aiueo.findNode(aiueo,3))
