#既存ファイルを読み取る
with open('aaa.txt') as f:
  a = f.readlines()       #行ごとに読み込んでリスト化
  b = '✨'.join(a)        #リスト内のアイテムを結合させる
  b = b.replace('\n', '') #結合したアイテムの改行を消す
  print(b)

#新規ファイルを作成して書き込み
with open('aaab.txt', mode = 'w') as f:
  l = ['one', 'two', 'three']
  f.write('テストようううううううううううううう\n') #普通の文字列を書き込み
  f.write("\n".join(l))                        #リストの文字列を開業挟んで連結

#↑で作成したファイルを読み込み
with open('aaab.txt', mode = 'r') as f:
  a = f.read()
  print(a)
