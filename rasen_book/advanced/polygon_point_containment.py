def dot(a, b):
  return a.real * b.real + a.imag * b.imag

def cross(a,b):
  return a.real * b.imag - a.imag * b.real

n=int(input())
vs=[complex(*map(int,input().split())) for i in range(n)]
edges=[(p0,p1) for p0,p1 in zip(vs,vs[1:]+[vs[0]])]

q=int(input())

while q:
  q -= 1
  p = complex(*map(int,input().split()))
  count=0
  for p0,p1 in edges:
    a=p0-p
    b=p1-p
    if a.imag>b.imag:
      a,b=b,a
    crs=cross(a,b)
    if a.imag <= 0 and 0 < b.imag and crs < 0:
      count+=1
    if crs == 0 and dot(a,b) <= 0:
      print(1)
      break
  else:
    print(2 if count %2 else 0)
