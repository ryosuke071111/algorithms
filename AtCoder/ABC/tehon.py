# -*- coding: utf-8 -*-

"""
ダイクストラと2分探索
"""

from collections import deque
import numpy as np
from scipy.sparse.csgraph import dijkstra

H,W,T = map(int, input().split())

start,goal = None,None
# 左右上下
directions = [[0,-1],[0,1],[-1,0],[1,0]]
# 四方に一回り大きいフィールドを作る
field = [['*'] * (W+2) for i in range(H+2)]
for i in range(1,H+1):
    row = list(input())
    for j in range(1, W+1):
        field[i][j] = row[j-1]
        if row[j-1] == 'S':
            start = (i, j)
        if row[j-1] == 'G':
            goal = (i, j)
# 1次元にするマッピング
mapping = [[0] * (W+2) for i in range(H+2)]
num = 0
for i in range(H+2):
    for j in range(W+2):
        mapping[i][j] = num
        num += 1

# ダイクストラ
def dk(x):
    # 引数にするグラフの準備
    graph = [[0] * (num) for i in range(num)]
    for i in range(1,H+1):
        for j in range(1, W+1):
            cur = (i, j)
            # 4方向見る
            for direction in directions:
                nxt = tuple(map(lambda x,y: x+y, cur, direction))
                # 壁はスキップ
                if field[nxt[0]][nxt[1]] == '*':
                    continue
                elif (field[nxt[0]][nxt[1]] == '.'
                        or field[nxt[0]][nxt[1]] == 'S'
                        or field[nxt[0]][nxt[1]] == 'G'):
                    graph[mapping[cur[0]][cur[1]]][mapping[nxt[0]][nxt[1]]] = 1
                elif field[nxt[0]][nxt[1]] == '#':
                    graph[mapping[cur[0]][cur[1]]][mapping[nxt[0]][nxt[1]]] = x

    return dijkstra(graph, indices=mapping[start[0]][start[1]])[mapping[goal[0]][goal[1]]]

# 2分探索で最初にTを上回る場所を見つける
hi = 10 ** 9
low = 0
# low+1 == hi -> lowとhiが隣り合った状態なので、境界が確定する
while low+1 < hi:
    mid = (hi+low) // 2
    if dk(mid) > T:
        hi = mid
    else:
        low = mid
# hiの位置が最初にTを上回る場所、lowがTを超えない最大値
print(low)

