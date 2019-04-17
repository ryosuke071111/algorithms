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

def get_distanceLP(p0,p1,p2):
  return abs(cross(p1 - p0,p2-p0)/abs(p1-p0))

def get_distanceSP(p0,p1,p2):
  if dot(p1-p0,p2-p0)<0:
    return abs(p2-p0)
  if dot(p0-p1,p2-p1)<0:
    return abs(p2-p1)
  return get_distanceLP(p0,p1,p2)

def get_distance(a,b,c,d):
  if intersect(a,b,c,d):
    return 0
  return min(min(get_distanceSP(a,b,c),get_distanceSP(a,b,d)),min(get_distanceSP(c,d,a),get_distanceSP(c,d,b)))

def intersect(a,b,c,d):
  return ccw(a,b,c) * ccw(a,b,d) <=0 and ccw(c,d,a) * ccw(c,d,b) <=0

n=int(input())
for i in range(n):
  x0,y0,x1,y1,x2,y2,x3,y3 = map(int,input().split())
  p0=complex(x0,y0)
  p1=complex(x1,y1)
  p2=complex(x2,y2)
  p3=complex(x3,y3)
  print(get_distance(p0,p1,p2,p3))


