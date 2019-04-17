
n,m = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(m)]
x = 0
ab.sort(key = lambda x:x[1])
ans = 0
for a,b in ab:
  if x <= a:
    ans += 1
    x = b
print(ans)


