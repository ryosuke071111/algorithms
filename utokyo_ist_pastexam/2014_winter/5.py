from decimal import *
import math
getcontext().prec = 40
tmp0,float0=map(float,input().split())
tmp1,float1=map(float,input().split())

tmp0=tmp0/(10**float0)
tmp1=tmp1/(10**float1)

a0,b0=tmp0.as_integer_ratio()
a1,b1=tmp1.as_integer_ratio()
print((a0*a1)/(b0*b1))

