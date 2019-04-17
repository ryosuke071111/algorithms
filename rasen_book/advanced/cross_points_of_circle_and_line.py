import math
def dot(a, b):
  return a.real * b.real + a.imag * b.imag

def projection(p0,p1,p2):
  a=p1-p0
  b=p2-p0
  pro = a * dot(a, b) / (abs(a) ** 2)
  t=p0+pro
  return t

def get_cross_point(p0,p1,p2):
  pro=projection(p0,p1,p2)
  e  =(p1-p0)/abs(p1-p0)
  base = (r**2 - abs(pro-p2)**2)**0.5
  if (pro-e*base).real == (pro+e*base).real:
    if (pro-e*base).imag < (pro+e*base).imag:
      ans1=pro-e*base
      ans2=pro+e*base
    else:
      ans1=pro+e*base
      ans2=pro-e*base
  elif (pro-e*base).real < (pro+e*base).real:
    ans1=pro-e*base
    ans2=pro+e*base
  else:
    ans1=pro+e*base
    ans2=pro-e*base
  return ans1.real, ans1.imag,ans2.real,ans2.imag

cx, cy, r = map(int, input().split())
p2=complex(cx,cy)
q = int(input())
for _ in range(q):
  x0,y0,x1,y1=map(int,input().split())
  p0=complex(x0,y0)
  p1=complex(x1,y1)
  print("{:.8f} {:.8f} {:.8f} {:.8f}".format(*get_cross_point(p0,p1,p2)))


