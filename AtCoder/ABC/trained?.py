n = int(input())
a =[int(input()) for _ in range(n)]
b = a[0]
ans =1

for i in range(len(a)):
  if b==2:
    print(ans)
    exit()
  b = a[b-1]
  ans += 1
print(-1)
