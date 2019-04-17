#○要するに共役複素数とは，それぞれの複素数（a+bi）の実部（a）を変えずに虚部（b）の符号だけを変えたものです


#2番目で引っかかる。なぜ？を解決しろ
def dot(a, b):
  return a.real * b.real + a.imag * b.imag

def projection(a,b):
  return a* dot(a,b)/(abs(a)**2)

def reflect(p0, p1, p2):
  a = p1 - p0
  b = p2 - p0
  v = projection(a, b)
  u = v - b
  p3 = p2 + 2 * u
  return p3

x0,y0,x1,y1 = map(float,input().split())
a = complex(x0,y0)
b = complex(x1,y1)
n=int(input())

for i in range(n):
  x,y=map(int,input().split())
  c=complex(x,y)
  p=reflect(a,b,c)
  print("{:.10} {:.10}".format(p.real, p.imag))
