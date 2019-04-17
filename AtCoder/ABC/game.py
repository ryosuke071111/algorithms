A,B = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

#左の山にi個、右の山にj個のものが残っている状態でその状態から終了までに先手が得られる価値の合計
#先手のスコアだけを見ている
dp = [[0 for i in range(B+1)] for i in range(A+1)]


#逆順にしてdpテーブルを埋める。その点数になるような最適行動
for i in reversed(range(0,A+1)):
  for j in reversed(range(0,B+1)):
    if i + j == A+B:
      continue

    #先攻の時は二通りあるうちのよりスコアが大きくなる方へ行動（プレイヤーAの行動をシミュレート）
    if (i+j)%2 == 0:
      if i == A:
        dp[i][j] = b[j]+dp[i][j+1]
      elif j == B:
        dp[i][j] = a[i]+dp[i+1][j]
      else:
        dp[i][j] = max(a[i]+dp[i+1][j], b[j]+dp[i][j+1])

    #後攻の時は先攻のスコアが小さくなるように行動する（プレイヤーBの行動をシミュレート）
    #後攻が先行のスコアが小さくなるように行動する=後攻の特典が最大化するように動く
    else:
      if i == A:
        dp[i][j] = dp[i][j+1]
      elif j == B:
        dp[i][j] = dp[i+1][j]
      else:
        dp[i][j] = min(dp[i+1][j],dp[i][j+1])
print(dp[0][0])

#ゲームでお互いが最善を尽くした時→片方のプレイヤー側から見た状態を考える
# dpは実際に求めたいものを設定する
#ゲームの問題は最後から決まっていくことが多い

