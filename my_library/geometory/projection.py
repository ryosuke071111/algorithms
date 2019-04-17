def dot(a, b):
  return a.real * b.real + a.imag * b.imag

def projection(a, b):
  return a * dot(a, b) / (abs(a) ** 2)

#複素平面の座標はクラスだから直接加算できる
def solve(p0,p1,p2):
  a=p1-p0
  b=p2-p0
  pro=projection(a,b)
  t=p0+pro
  return t

def main():
  x0,y0,x1,y1=map(float,input().split())
  p0=complex(x0,y0)
  p1=complex(x1,y1)
  q=int(input())
  for i in range(q):
    p2=complex(*map(float,input().split()))
    t=solve(p0,p1,p2)
    print("{:.10f} {:.10f}".format(t.real,t.imag))

main()



