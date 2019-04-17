# class Tree:
#   def __init__(self, v):
#     self.value =v
#     self.left = None
#     self.right = None

# def search(self, v):
#   while tree:
#     if self.value == v: return True
#     if v < self.value:
#       self = self.left
#     else:
#       self = self.right
#   return False

# def insert(self, v):
#   if self is None:
#     return Tree(v)
#   elif v == self.value:
#     return self
#   elif v < self.value:
#     self.left = insert(self.left, v)
#   else:
#     self.right = insert(self.right, v)
#   return self

class Node:
    def __init__(self, x):
        self.data  = x
        self.left  = None
        self.right = None

    # 探索
    def search(node, x):
        while node:
            if node.data == x: return True
            if x < node.data:
                node = node.left
            else:
                node = node.right
        return False

    # 挿入
    def insert(node, x):
        if node is None: return Node(x)
        elif x == node.data: return node
        elif x < node.data:
            node.left = insert(node.left, x)
        else:
            node.right = insert(node.right, x)
        return node

a = Node(2)
# a.insert(10)
# a.insert(1330)
# a.insert(133110)
# a.insert(1330)
print(a)


# def insert(node, x):
#     if node is None: return Node(x)
#     elif x == node.data: return node
#     elif x < node.data:
#         node.left = insert(node.left, x)
#     else:
#         node.right = insert(node.right, x)
#     return node

# def insert(node, x):
#     if node is None: return Node(x)
#     elif x == node.data: return node
#     elif x < node.data:
#         node.left = insert(node.left, x)
#     else:
#         node.right = insert(node.right, x)
#     return node

# def search(node, x):
#     while node:
#         if node.data == x: return True
#         if x < node.data:
#             node = node.left
#         else:
#             node = node.right
#     return False
