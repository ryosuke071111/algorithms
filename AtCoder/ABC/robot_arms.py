import sys

N = int(input())
XY = [[int(_) for _ in input().split()] for i in range(N)]

mc = [0, 0]
maxl = 0

for x, y in XY:
    l = abs(x) + abs(y)
    maxl = max(maxl, l)
    mc[l % 2] += 1

if mc[0] > 0 and mc[1] > 0:
    print(-1)
    sys.exit()

def calc(sx, sy, ex, ey, d):
    dx, dy = ex - sx, ey - sy
    if dx > dy:
        if dx > -dy:
            return "R", sx + d, sy
        else:
            return "D", sx, sy - d
    else:
        if dx > -dy:
            return "U", sx, sy + d
        else:
            return "L", sx - d, sy

import math

l = math.ceil(math.log(maxl + 1, 2))

ms = [1 << i for i in range(l)][::-1]

rms = ms

if mc[0] > 0:
    rms = [1] + ms

print(len(rms))
print(*rms)

for ex, ey in XY:
    x, y = 0, 0
    w = ""
    if mc[0] > 0:
        w = "R"
        x += 1
    for m in ms:
        d, x, y = calc(x, y, ex, ey, m)
        w += d
    print(w)

