#9:51-
B=[list(map(int,input().split())) for i in range(2)]
C=[list(map(int,input().split())) for i in range(3)]
S=sum(sum(i) for i in B)+sum(sum(i) for i in C)

memo={}

#得点計算
def score(t):
  s=0
  for i in range(2):
    for j in range(3):
      if t[i+1][j]==t[i][j]:
        s+=B[i][j]
  for i in range(3):
    for j in range(2):
      if t[i][j+1]==t[i][j]:
        s+=C[i][j]
  return s

#状態を作成
def solve(t,turn=1):
  if str(t) in memo: #碁盤の状態がメモにあるならそれを返す
    return memo[str(t)]
  if turn == 10:     #ターンが終わったら状態の計算
    return score(t)
  bs1=0
  bs2=10**9
  print("turn:",turn,"t:",t)
  for i in range(3):
    for j in range(3):
      if not t[i][j] is None:
        continue
      t[i][j]= turn%2 #碁盤にプレイヤーの手番をおく
      s=solve(t,turn+1) #ターンを1増やしてシミュレーション継続
      print(" t:",t)
      t[i][j]=None
      bs1=max(bs1,s)
      bs2=min(bs2,s)
  ret=bs1 if turn%2 else bs2 #奇数番目なら得点の最大値/偶数番目なら得点の最長値を返す
  memo[str(t)]=ret
  return ret

ret = solve([[None]*3 for i in range(3)])
print(ret)
print(S - ret)

