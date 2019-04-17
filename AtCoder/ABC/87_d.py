import sys
sys.setrecursionlimit(1000000)

def DFS(start):
    global graph
    global zahyou

    start_num=zahyou[start]
    print("start_num",start_num)

    for w,d in graph[start]:
        print(zahyou)
        if(zahyou[w]==None):
            zahyou[w]=start_num + d
            if( not DFS(w)):
                return False
        else:
            if(start_num + d != zahyou[w]):
                return False


    return True



n,m=map(int,input().split())
graph=[[] for _ in range(n)]

zahyou=[None]*n
for i in range(m):
    l,r,d=map(int,input().split())
    graph[l-1].append((r-1,d))
    graph[r-1].append((l-1,-1*d))
print(graph)

flag=True
for i in range(n):
    if(zahyou[i]==None):
        zahyou[i]=0
        flag&=DFS(i)
        if( not flag):
            break

if(flag):
    print("Yes")
else:
    print("No")


#union-find
# class WeightedUnionFind:
#     def __init__(self, n):
#         self.par = [i for i in range(n + 1)]
#         self.rank = [0] * (n + 1)
#         # 根への距離を管理
#         self.weight = [0] * (n + 1)

#     # 検索
#     def find(self, x):  # xの親を返す
#         if self.par[x] == x:
#             return x
#         else:
#             y = self.find(self.par[x])
#             # 親への重みを追加しながら根まで走査
#             self.weight[x] += self.weight[self.par[x]]
#             # 親の値を更新(アルゴリズムの高速化)
#             self.par[x] = y
#             return y  # 親

#     # 併合
#     # (xからyへの重みがw) = (y - x = W)
#     def union(self, x, y, w):
#         rx = self.find(x)
#         ry = self.find(y)
#         # 既に同集合の場合
#         if rx == ry:
#             if self.diff(x, y) != w:
#                 print("No")
#                 exit()
#         # 木の高さで処理を変えるのは高速化(木を低くする)のため
#         # xの木の高さ < yの木の高さ
#         if self.rank[rx] < self.rank[ry]:
#             self.par[rx] = ry
#             self.weight[rx] = w - self.weight[x] + self.weight[y]
#         # xの木の高さ ≧ yの木の高さ
#         else:
#             self.par[ry] = rx
#             self.weight[ry] = -w - self.weight[y] + self.weight[x]
#             # 木の高さが同じだった場合の処理
#             if self.rank[rx] == self.rank[ry]:
#                 self.rank[rx] += 1

#     # 同じ集合に属するか
#     def same(self, x, y):
#         return self.find(x) == self.find(y)

#     # xからyへのコスト
#     def diff(self, x, y):
#         return self.weight[x] - self.weight[y]

#     def show(self):
#         for i in range(1, n + 1):
#             print("node:{} par:{} w:{}".format(i, union.par[i], union.weight[i]))


# n, m = [int(i) for i in input().split()]
# l = [0 for i in range(m)]
# r = [0 for i in range(m)]
# d = [0 for i in range(m)]

# union = WeightedUnionFind(n)
# for i in range(m):
#     l[i], r[i], d[i] = [int(i) for i in input().split()]
#     union.union(l[i], r[i], d[i])
# print("Yes")
# #union.show()

