def unit(a):
  return a/abs(a)

c1x, c1y, c1r = map(int, input().split())
c2x, c2y, c2r = map(int, input().split())
a = complex(c1x,c1y)
b = complex(c2x,c2y)
ab=abs(b-a)

#角度
ac=(c1r**2 + ab**2-c2r**2)/(2*ab)
c=a+(b-a)*(ac/ab)
pc=(c1r**2-ac**2)**0.5
p=c+pc*unit(b-a)*1j
q=c+pc*unit(b-a)*-1j

if p.real>q.real:
  p,q=q,p
if abs(p.real - q.real) < 1e-6 and p.imag > q.imag:
  p, q = q, p
print('{:.10f} {:.10f} {:.10f} {:.10f}'.format(p.real, p.imag, q.real, q.imag))
