n = int(input())

p = [0]* (n+1)
m = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n):
  p[i], p[i+1] = map(int, input().split())

for l in range(2, n+1): #計算の対象とする行列の個数(pythonの性質上 rangeの値は右半開空間なので+1)
  for i in range(1, n-l+2): #対象とする行列の個数に応じた計算の始点(pythonの性質上 rangeの値は右半開空間なので+2)
    j = i + l - 1       #計算の終点なのでiにlを足して1引く（l=2、i=1, i+ l=3だと1つ多い）
    m[i][j] = float('inf')
    for k in range(i , j):
      m[i][j] = min(m[i][j], m[i][k] + m[k+1][j] + p[i-1]* p[k]* p[j])

print(m[1][n])

