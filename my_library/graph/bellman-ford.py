d=[]
v,e,r=list(map(int,input().split()))
edges=[list(map(int,input().split())) for i in range(e)]

def bellman_ford(s):
  global d
  d=[float('inf') for i in range(v)]
  d[s]=0

  #relax
  for i in range(v-1):
    for s,t,w in edges:
      if d[t] > d[s]+w:
        d[t] = d[s]+w
  #負の経路検出
  for s,t,w in edges:
    if d[s]+ w<d[t]:
      return False
  return True

if bellman_ford(r):
  for w in d:
    if w== float('inf'):
      print('INF')
    else:
      print(w)
else:
  print('NEGATIVE CYCLE')
