x0,y0,x1,y1 = map(int, input().split())
p0=complex(x0,y0)
p1=complex(x1,y1)
q = int(input())

CCW = {1: 'COUNTER_CLOCKWISE',
       -1: 'CLOCKWISE',
       2: 'ONLINE_BACK',
       -2: 'ONLINE_FRONT',
       0: 'ON_SEGMENT',}

def dot(a, b):
  return a.real * b.real + a.imag * b.imag

def cross(a, b):
  return a.real * b.imag - a.imag * b.real

def ccw(p0, p1, p2):
  a = p1-p0
  b = p2-p0
  if cross(a,b) > 0:
    return 1 #couner_clockwise
  elif cross(a,b) <0:
    return -1 #clockwise
  elif dot(a,b) < 0:
    return 2 #online_back
  elif abs(a) < abs(b):
    return -2 #online_front
  else:
    return 0 #on_segment

for i in range(q):
  p2=complex(*map(int,input().split()))
  print(CCW[ccw(p0,p1,p2)])
