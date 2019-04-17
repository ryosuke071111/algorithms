n = int(input())
p = [0] * (n+1)
m = [[0 for _ in range(100)] for _ in range(100)]

for i in range(n):
  p[i], p[i+1] = map(int, input().split())
for l in range(2, n+2):
  for i in range(1, n-l+2):
    j = i + l -1
    m[i][j] = float('inf')
    for k in range(i, j):
      m[i][j] = min(m[i][j], m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j])

print(m[1][n])
