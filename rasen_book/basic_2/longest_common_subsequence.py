#O(n^2)のアルゴリズム　＊他にもO(nlon)のアルゴリズムがある
def lcs(x,y):
  n = len(x)
  m = len(y)
  c = [[0] * (m+1) for _ in range(n+1)]

  for i in range(1, n+1):
    for j in range(1, m+1):
      if x[i-1] == y[j-1]:
        c[i][j] = c[i-1][j-1] + 1
      else:
        c[i][j] = max(c[i-1][j], c[i][j-1])
  return c[i][j]


num = int(input())

for _ in range(num):
  x = input()
  y = input()
  print(lcs(x, y))
