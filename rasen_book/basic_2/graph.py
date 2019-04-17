N = int(input())
M = [[0 for i in range(N)] for j in range(N)] #二次元配列が作られる

for i in range(N):
  nums = list(map(lambda x: int(x)-1, input().split())) #ゼロオリジンの配列なので1引いている
  print(nums)
  f = nums[0] #エッジ番号を取得
  print('f is', f)
  nums = nums[2:] #どのエッジにつながっているかを取得（2番目以降がつながっているエッジの値）
  print('nums are', nums)
  for num in nums:
    M[f][num] = 1 #二次元配列に配置した時の配置をおく

for i in range(N):
  for j in range(N):
    if(j!=N-1): #終わりは0オリジンであるため、その値-1になる
      print(M[i][j], end = ' ')
    else:
      print(M[i][j])

#頂点間の関係性を定数時間O(1)で確認できる
#辺の追加や削除は既存のテーブルに入れればいいからO(n)で処理可能
