n, m = map(int, input().split())
C = list(map(int, input().split()))
T = [0]+[float('inf')]*n

for i in range(m):
  for j in range(C[i], n+1):
    T[j] = min(T[j], T[j-C[i]]+1)

print(T[j])
