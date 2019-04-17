#8:50-
n=int(input())
edges=[[0]*n for i in range(n)]
for i in range(n-1):
  b=int(input())
  edges[b-1][i+1]=1

def dfs(u):
  if 1 not in edges[u]:
    return 1
  else:
    ls=[]
    for v in range(len(edges[u])):
      if edges[u][v]==1:
        ls.append(dfs(v))
  return max(ls)+min(ls)+1
print(dfs(0))

"""
よかった点
・大方針はあっていた

悪かった点
・indexを見誤っていた
  -edgesは2次元なので2つのindex
  -再帰が終わらないのはrangeは0~n,iterableはその中身を誤認してたから
・自分の方針を信じる
"""
