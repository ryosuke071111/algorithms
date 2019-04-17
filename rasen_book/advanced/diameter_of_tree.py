#直系とは木の最遠節点間の距離
from heapq import heappop, heappush
INF = 10 ** 20

def main():
  n = int(input())
  edges = [[] for _ in range(n)]
  for _ in range(n - 1):
    s,t,w = map(int, input().split())
    edges[s].append((w, t))
    edges[t].append((w, s))

  def func(start):
    cost = [INF] * n
    que = [(0, start)]
    cost[start] = 0

    while que:
      acc, num = heappop(que)
      for weight, to in edges[num]:
        if weight + acc < cost[to]:
          cost[to] = weight + acc
          heappush(que, (weight + acc, to))
    return cost

  cost1 = func(0)
  max_ind = cost1.index(max(cost1))
  cost2 = func(max_ind)

  print(max(cost2))
main()
