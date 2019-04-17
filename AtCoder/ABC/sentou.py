n,t = map(int,input().split())
T = list(map(int,input().split()))
x = 0

for i in range(1, len(T)):
  if T[i]-T[i-1] < t:
    x += T[i]-T[i-1]
  else:
    x += t

print(x+t)
