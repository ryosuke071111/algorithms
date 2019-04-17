V,E = map(int, input().split())
edge = [[] for _ in range(V)]

for _ in range(E):
  s,t = map(int, input().split())
  edge[s].append(t)
  edge[t].append(s)

group = [-1] * V
cnt = 0

for i in range(V):
  print('groupは',group)
  print('cntは',cnt)
  if group[i] == -1:
    group[i] = cnt
    stack = [i]
    while stack:
      v = stack.pop()
      for c in edge[v]:
        if group[c] == -1:
          group[c] = cnt
          stack.append(c)
          print('stackは',stack)
    cnt += 1

for _ in range(int(input())):
  s, t = map(int, input().split())
  print('yes' if group[s] == group[t] else 'no')

#グループの中の初での値を基準としてその値に連結しているスタックを作っていく
#スタックの中に入って入ればtruemを返す

#閉路を持たない＝帰り道がない閉じ込められる
#平炉を持つ=帰り道がある
