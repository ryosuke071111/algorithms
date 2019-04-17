n = int(input()) #行列の個数
p = [0] * (n+1)  #各行列の次元数を入れるための箱
m = [[0 for _ in range(100)] for _ in range(100)] #DPするための表

for i in range(n):
  p[i], p[i+1] = map(int,input().split()) #行列の次元数を入力していく

for l in range(2, n+1):     #表の縦のレイヤー数
  for i in range(1, n-l+2): #表の素朴なiの数（行番号）（レイヤーが上がるにつれてしぼんでいく（参加者が乗算で切り捨てられていくから））
    j = i + l -1            #表の素朴なjの数（列番号）（レイヤーが上がるにつれて最小値が切り捨てられていく（決勝戦だから））
    m[i][j] = float('inf')
    for k in range(i, j):   #表の横の行列の幅
      m[i][j] = min(m[i][j], m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]) #漸化式

print(m[1][n])

import numpy as npo
