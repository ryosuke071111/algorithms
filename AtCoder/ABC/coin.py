a, b, c, x = map(int, [input() for i in range(4)])
ans = 0
for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            if 500*i + 100*j + 50*k == x:
                ans +=1
print(ans)
