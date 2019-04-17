from enum import IntEnum


class Action(IntEnum):
    ADD = 1
    SEARCH = 2
    REMOVE = 3


class Color(IntEnum):
    BLACK = 0
    RED = 1

    @staticmethod
    def flip(c):
        return [Color.RED, Color.BLACK][c.value]


class Node:
    __slots__ = ('value', 'left', 'right', 'color', 'valid')

    def __init__(self, value):
        self.value = value
        self.left = Leaf
        self.right = Leaf
        self.color = Color.RED
        self.valid = True

    def flip_color(self):
        self.color = Color.flip(self.color)

    def is_red(self):
        return self.color == Color.RED

    def __str__(self):
        return ('(' + str(self.left) + ', '
                + str(self.value) + ', ' + str(self.right) + ')')


class LeafNode(Node):
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None
        self.color = None
        self.valid = False

    def flip_color(self):
        pass

    def is_red(self):
        return False

    def __str__(self):
        return 'Leaf'


Leaf = LeafNode()


class RedBlackBST:
    def __init__(self):
        self.root = Leaf

    def add(self, value):
        def _add(node):
            if node is Leaf:
                node = Node(value)
            if node.value > value:
                node.left = _add(node.left)
            elif node.value < value:
                node.right = _add(node.right)
            else:
                if not node.valid:
                    node.valid = True

            node = self._balance(node)
            return node

        self.root = _add(self.root)
        self.root.color = Color.BLACK

    def _balance(self, node):
        if node.right.is_red() and not node.left.is_red():
            node = self._rotate_left(node)
        if node.left.is_red() and node.left.left.is_red():
            node = self._rotate_right(node)
        if node.left.is_red() and node.right.is_red():
            node = self._flip_colors(node)
        return node

    def _rotate_left(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = Color.RED
        return x

    def _rotate_right(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = Color.RED
        return x

    def _flip_colors(self, node):
        node.flip_color()
        node.left.flip_color()
        node.right.flip_color()
        return node

    def remove(self, value):
        def _remove(node):
            if node is Leaf:
                return
            if node.value > value:
                _remove(node.left)
            elif node.value < value:
                _remove(node.right)
            else:
                node.valid = False

        _remove(self.root)

    def count(self, min_, max_):
        def _range(node):
            if node is Leaf:
                return 0

            if node.value > max_:
                return _range(node.left)
            elif node.value < min_:
                return _range(node.right)
            else:
                count = _range(node.left) + _range(node.right)
                if node.valid:
                    count += 1
                return count

        return _range(self.root)

    def __str__(self):
        return str(self.root)


def count_intersections(segments):
    segments.sort()
    tree = RedBlackBST()
    count = 0
    for seg in segments:
        x, action, y = seg
        if action == Action.SEARCH:
            count += tree.count(*y)
        elif action == Action.ADD:
            tree.add(y)
        elif action == Action.REMOVE:
            tree.remove(y)

    return count


n=int(input())
segs=[]

for i in range(n):
  x1,y1,x2,y2=map(int,input().split())
  if x1>x2 or y1>y2:
    x1,x2=x2,x1
    y1,y2=y2,y1
  if x1==x2:
    segs.append((x1,Action.SEARCH,(y1,y2)))
  else:
    segs.append((x1,Action.ADD,y1))
    segs.append((x2,Action.REMOVE,y2))
print(count_intersections(segs))




