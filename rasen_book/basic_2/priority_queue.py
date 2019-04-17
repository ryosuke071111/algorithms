import heapq #モジュールインポート

a = []
while True:
  inp = input().split() #スプリットで別の単語としてインポート
  if inp[0] == "insert":
    heapq.heappush(a, -int(inp[1])) #分けた0インデックス番目を取得
  elif inp[0] == "extract":
    print(-heapq.heappop(a))
  else:
    break

#数の分要素の計算を行うので計算量はO（logn） n=要素数
