n=int(input())
mod=10**9+7

#内包表記の時は小さい成分から作っていく（新しい次元から）ls[i][j][k]←ココ
dp=[[[[0 for i in range(4)] for j in range(4)] for k in range(4)] for l in range(n+1)]

# 長さ0の文字列は1である。
# 0,1,2に関する制約しかないので、
# Sは、333Sと考えても問題がない。
dp[0][3][3][3]=1
print(dp)


#forを回す時は一番新しい次元から作っていくls[i][j][k]←ココ
for length in range(n):
  for c1 in range(4):
    for c2 in range(4):
      for c3 in range(4):
        if dp[length][c1][c2][c3]==0: #もともと0なら打ち切り
          continue
        for a in range(4):
          if a==2 and c1==1 and c2==0:
            continue
          if a==2 and c1==0 and c2==1:
            continue
          if a==1 and c1==2 and c2==0:
            continue
          if a==2 and c1==1 and c3==0:
            continue
          if a==2 and c2==1 and c3==0:
            continue
          dp[length+1][a][c1][c2]+=dp[length][c1][c2][c3]
          dp[length+1][a][c1][c2]%=mod

ans=0
for c1 in range(4):
  for c2 in range(4):
    for c3 in range(4):
       ans+=dp[n][c1][c2][c3]
       ans%=mod
print(ans)

#dpで覚えておくべきindexの話
#①内包表記は先に入れたものが一番小さい箱
#②forを回す時は一番内側のループから値が入る
# a=[[[[0]*1 for i in range(2)] for i in range(3)] for i in range(4)]
# for i in range(4):
#   for j in range(3):
#     for k in range(2):
#       for l in range(1):
#         a[i][j][k][l]=i
#         print(a)


