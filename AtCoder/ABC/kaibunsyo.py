n = int(input())
S=[]


for i in range(n):
  S.append(list(input()))

S[0].sort()
#文字列ごとにカウントする辞書
D ={}

for i in range(len(S)):
  #Sの最初の文字列を使って辞書を作る
  if i==0:
    for j in range(len(S[i])):
      #辞書にその文字列を追加
      if S[i][j] not in D:
        D[S[i][j]] =1
      #被りがあったら数を増やす
      else:
        D[S[i][j]] +=1
  else:

  #辞書の文字の中と他の文字列を照合
    for k in D:
      #その文字がなければカウントを0にする
      if k not in S[i]:
        D[k] = 0
      #その文字があればその文字列にあるその文字の中身を入れる（最小の文字の大きさに更新していく）
      else:
        D[k] = min(D[k], S[i].count(k))

D = sorted(D.items(),key=lambda x:x[0])
ans=[]

for i in range(len(D)):
  ans.append(D[i][0]*D[i][1])
ans = "".join(ans)
print(ans)
