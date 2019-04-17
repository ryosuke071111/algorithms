#内積0の場合直行している
#外積0の場合平行
def main():
  q = int(input())
  for i in range(q):
    print(parallel_orthogonal())

def parallel_orthogonal():
  xp0, yp0, xp1, yp1, xp2, yp2, xp3, yp3 = map(int, input().split())
  l1_start = complex(xp0, yp0)
  l1_end = complex(xp1, yp1)
  l2_start = complex(xp2, yp2)
  l2_end = complex(xp3, yp3)
  complex

  if dot(l1_end - l1_start, l2_end - l2_start)==0:
    return 1
  if cross(l1_end - l1_start, l2_end - l2_start)==0:
    return 2
  return 0

# p0..p3がそれぞれ座標になっている

#内積
def dot(a, b):
  return a.real * b.real + a.imag * b.imag

#外積
def cross(a, b):
  return a.real * b.imag - a.imag * b.real

main()
