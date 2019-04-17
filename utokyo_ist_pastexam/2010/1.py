
class Rect(object):
    x, y, w, h, flag = 0, 0, 0, 0, 0

    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h

    def set_flag(self, flag):
        self.flag = flag


def is_intersect(rect1, rect2):
    #judged by center point（実際の距離が理論的距離よりの小さければ、中に図形が入っていることになる）
    x1 = rect1.x + float(rect1.w)/2
    y1 = rect1.y + float(rect1.h)/2
    x2 = rect2.x + float(rect2.w)/2
    y2 = rect2.y + float(rect2.h)/2
    actual_dis_x=abs(x1-x2)
    logical_dis_x=float(rect1.w+rect2.w)/2
    actual_dis_y=abs(y1-y2)
    logical_dis_y=float(rect1.h+rect2.h)/2

    if actual_dis_x == logical_dis_x and actual_dis_y == logical_dis_y:
        return False
    elif actual_dis_x <= logical_dis_x and actual_dis_y <= logical_dis_y:
        return True



def find(recList, rect):
    if recList[rect.flag] == rect:
        return rect
    else:
        return find(recList, recList[rect.flag])


def union(recList, rect1, rect2):
    root1 = find(recList, rect1)
    root2 = find(recList, rect2)
    if root1 != root2:
        root1.flag = recList.index(root2)
    return 0


rectList = []
MAX_X = 1000
MAX_Y = 1000

# NOTICE "10.txt" for Q.1 & "1000.txt" for Q.3
with open("1000.txt", "r") as fin:
    for line in fin:
        tmp = line.split(" ")
        r = Rect(int(tmp[0]), int(tmp[1]), int(tmp[2]), int(tmp[3]))
        rectList.append(r)
        r.set_flag(len(rectList)-1)


# maximum thickness
maxT = 0
f = [[0 for x in range(MAX_X)] for y in range(MAX_Y)]
for rect in rectList:
    for i in range(rect.x, rect.x + rect.w):
        for j in range(rect.y, rect.y + rect.h):
            f[i][j] += 1
for i in range(0, MAX_X):
    for j in range(0, MAX_Y):
        maxT = max(maxT, f[i][j])
print( "Maximum thickness is {}".format(maxT))


# the number of clusters
for i in range(0, len(rectList)-1):
    for j in range(i+1, len(rectList)):
        rect1 = rectList[i]
        rect2 = rectList[j]
        if is_intersect(rect1, rect2):
            union(rectList, rect1, rect2)
sum = 0
for rect in rectList:
    if find(rectList, rect) == rect:
        sum += 1
print( "The number of clusters is {}".format(sum))


# the maximum number of cluster elements
dic = {}
for rect in rectList:
    tmp = find(rectList, rect)
    if tmp in dic:
        dic[tmp] += 1
    else:
        dic[tmp] = 1
# for key, value in dic.iteritems():
#    print( key, value
print( "The maximum number of cluster elements is {}".format(dic[max(dic, key=dic.get)]))


# the maximum cluster area for a single cluster
from collections import deque
ans = 0
for i in range(0, MAX_X):
    for j in range(0, MAX_Y):
        if f[i][j] > 0:
            q = deque()
            sum = 1
            f[i][j] = 0
            q.append((i, j))
            while q:
                x, y = q.pop()
                for (dx, dy) in [(-1,0), (0, -1), (1, 0), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if (nx >= 0) and (ny >= 0) and (nx <= MAX_X) and (ny <= MAX_Y):
                        if f[nx][ny] > 0:
                            sum += 1
                            f[nx][ny] = 0
                            q.append((nx, ny))

        ans = max(ans, sum)
# print(f)
print( "the maximum cluster area for a single cluster is {}".format(ans))
