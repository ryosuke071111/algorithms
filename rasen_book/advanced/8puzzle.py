from collections import deque, OrderedDict

class Puzzle:
    def __init__(self, field=None, path=''):
        self.f = field
        self.space = None
        for i in range(9):
            if self.f[i] == 9:
                self.space = i
        self.path = path

    def __lt__(self, pzl): # <
        for i in range(9):
            if self.f[i] == pzl.f[i]:
                continue
            return self.f[i] > pzl.f[i]
        return False

    def __gt__(self, pzl): # >
        for i in range(9):
            if self.f[i] == pzl.f[i]:
                continue
            return self.f[i] < pzl.f[i]
        return False

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
dir = ['u', 'l', 'd', 'r']

def is_target(pzl):
    for i in range(9):
        if pzl.f[i] != i+1:
            return False
    return True

def bfs(pzl):
    queue = deque([])
    V = {}
    pzl.path = ''
    queue.append(pzl)
    V[str(pzl.f)] = True
    if is_target(pzl):
      return pzl.path

    while len(queue) != 0:
        u = queue.popleft()
        sx, sy = u.space//3, u.space%3
        for r in range(4):
            tx, ty = sx + dx[r], sy + dy[r]
            if tx < 0 or ty < 0 or tx >= 3 or ty >= 3:
                continue
            v = Puzzle(field=[u.f[i] for i in range(9)], path=u.path)
            v.f[u.space], v.f[tx*3+ty] = v.f[tx*3+ty], v.f[u.space]
            v.space = tx*3 + ty
            if str(v.f) not in V:
                V[str(v.f)] = True
                v.path += dir[r]
                if is_target(v): return v.path
                queue.append(v)
    return 'unsolvable'

field = []
for i in range(3):
    field.extend(list(map(int, input().split(' '))))

for i in range(9):
    if field[i] == 0: field[i] = 9

pzl = Puzzle(field=field)
ans= bfs(pzl)
print(len(ans))
