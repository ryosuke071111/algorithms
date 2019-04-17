a,b,k = map(int,input().split())

i = k

while i > 0:
  if a % 2 == 1:
    a -=1
    b += a//2
    a -= a//2
  else:
    b += a//2
    a -= a//2
  i -= 1
  if i:
    if b % 2 == 1:
      b -=1
      a += b//2
      b -= b//2
    else:
      a += b//2
      b -= b//2
    i -=1

print(int(a),int(b))
