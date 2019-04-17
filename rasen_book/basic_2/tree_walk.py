class Node():
    def __init__(self, parent = -1, left = -1, right = -1):
        self.parent = parent
        self.left = left
        self.right = right

def preorder(ns, i):
    print(" " + str(i), end ="")
    if ns[i].left != -1:
        preorder(ns, ns[i].left)
    if ns[i].right != -1:
        preorder(ns, ns[i].right)

def inorder(ns, i):
    if ns[i].left != -1:
        inorder(ns, ns[i].left)
    print(" " + str(i), end ="")
    if ns[i].right != -1:
        inorder(ns, ns[i].right)

def postorder(ns, i):
    if ns[i].left != -1:
        postorder(ns, ns[i].left)
    if ns[i].right != -1:
        postorder(ns, ns[i].right)
    print(" " + str(i), end ="")


n = int(input())
ns = [Node() for i in range(n)]
for i in range(n):
    p, l, r = map(int, input().split())
    if l != -1:
        ns[p].left = l
        ns[l].parent = p
    if r != -1:
        ns[p].right = r
        ns[r].parent = p

for i in range(n):
    if ns[i].parent == -1:
        print("Preorder")
        preorder(ns, i)
        print()
        print("Inorder")
        inorder(ns, i)
        print()
        print("Postorder")
        postorder(ns, i)
        print()
