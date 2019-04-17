#座標を出す
def dot(a, b):
  return a.real * b.real + a.imag * b.imag

def cross(a, b):
  return a.real * b.imag - a.imag * b.real

def cross_point(p0,p1,p2,p3):
  base=p3-p2
  d1=abs(cross(base,p0-p2)/abs(base))
  d2=abs(cross(base,p1-p2)/abs(base))
  t=d1/(d1+d2)
  ans= p0+(p1-p0)*t
  return ans.real,ans.imag

n = int(input())
for i in range(n):
  x0,y0,x1,y1,x2,y2,x3,y3 = map(int,input().split())
  p0=complex(x0,y0)
  p1=complex(x1,y1)
  p2=complex(x2,y2)
  p3=complex(x3,y3)
  print(*cross_point(p0,p1,p2,p3))
