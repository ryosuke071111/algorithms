#10:09-
from collections import Counter
n=int(input())
A=list(map(int,input().split()))
Cont=Counter(A)
Cont1=Counter(A)
for k,v in Cont.items():
  Cont1[k-1]+=v
  Cont1[k+1]+=v
print(Cont1.most_common()[0][1])

"""
思考過程おさらい
-間違いパターン
⑴Counterで要素の多いものを一回取り出す
⑵最大要素の前後の数字をkeyとする辞書を作成
⑶全てのデータに対して辞書に当てはまるものがあればカウントする

-正解パターン
⑴Counterで全要素の数を取る
⑵Counter1から値を取り出してその前後の数字を既存のCounterに足していく
"""

