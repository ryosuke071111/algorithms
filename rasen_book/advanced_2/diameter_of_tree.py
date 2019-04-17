def dfs(root):
  isVisited = [False] * n
  queue = [(0, root)]
  # print('queue is', queue)
  longest = (-1, -1)

  while queue:
    total_weight, u = queue.pop()
    if isVisited[u]:
      continue
    isVisited[u] = True
    longest = max(longest, (total_weight, u))
    # print("longest is", longest)
    for w, t in edges[u]:
      if not isVisited[t]:
        queue.append((total_weight + w, t))

  return longest

n = int(input())

edges =[[] for i in range(n)]

for i in range(n-1):
  s,t,w = map(int, input().split())
  edges[s].append((w, t))
  edges[t].append((w, s))

_, ln = dfs(0)
# print("ln", ln)
ld, _ = dfs(ln)
# print("ld", ld)
print(ld)
