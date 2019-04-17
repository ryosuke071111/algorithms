a,b,c,d = map(int,input().split())

if a > c:
  start = a
else:
  start = c

if b < d:
  end = b
else:
  end = d

print(0 if end-start < 0 else end-start)

#別解：
a, b, c, d = map(int, input().split())
print(max(0, min(b,d) - max(a,c)))
