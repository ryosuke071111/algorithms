def cross(a, b):
  return a.real * b.imag - a.imag*b.real

def convex_hull(p):
  pp = sorted(p, key=lambda x:(x.imag, x.real))
  n = len(pp)
  ans = [0] * (n+1)
  j = 0

def convex_hull(p):
  pp=sorted(p,key=lambda x:(x.imag,x.real))
  n=len(pp)
  ans=[0]*(n+1)
  j=0

  #上側を入れていく
  for i in range(n):
    while j > 1 and cross(ans[j-1] - ans[j-2], pp[i]-ans[j-1]) < 0: #常に次の点が下側に
      j -= 1
    ans[j] = pp[i]
    j += 1
  k = j
  #下側を入れていく
  for i in range(n-2, -1, -1):
    while j > k and cross(ans[j-1]-ans[j-2], pp[i]-ans[j-1]) < 0: #常に次の点が下側に
      j -= 1
    ans[j] = pp[i]
    j +=1
  return ans[0:j-1]

n = int(input())
p=[]
for i in range(n):
  x,y = list(map(int, input().split()))
  p.append(complex(x,y))
ans = convex_hull(p)
print(len(ans))

for i in ans:
  print(int(i.real), int(i.imag))
